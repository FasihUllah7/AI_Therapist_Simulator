from fastapi import APIRouter
from .models.chat_models import ChatRequest, ChatResponse
from .services.openai_service import get_gpt_response
from .services.pinecone_service import store_message, retrieve_history

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Retrieve history
    history = retrieve_history(request.message)

    # Get GPT response
    reply = get_gpt_response(user_message=request.message, history=history)

    # Store new message
    store_message(request.message)

    return ChatResponse(reply=reply)
