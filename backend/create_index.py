import os
from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()  # loads your .env file

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = os.getenv("PINECONE_INDEX")

# Check if index exists, if not create it
if index_name not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=1536,   # required for text-embedding-3-small
        metric="cosine"
    )
    print(f"✅ Created index: {index_name}")
else:
    print(f"ℹ️ Index {index_name} already exists.")
