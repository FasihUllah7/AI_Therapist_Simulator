import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize Pinecone client
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Setup Pinecone index
index_name = os.getenv("PINECONE_INDEX", "therapy-sessions")
if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_text(text: str):
    """Generate embeddings using OpenAI."""
    emb = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return emb.data[0].embedding

def store_message(text: str):
    """Store a message in Pinecone with its embedding."""
    vector = embed_text(text)
    index.upsert([
        {"id": str(hash(text)), "values": vector, "metadata": {"text": text}}
    ])

def retrieve_history(query: str, top_k: int = 5) -> str:
    """Retrieve top_k similar past messages from Pinecone."""
    vector = embed_text(query)
    search = index.query(vector=vector, top_k=top_k, include_metadata=True)
    return "\n".join([match["metadata"]["text"] for match in search["matches"]])
