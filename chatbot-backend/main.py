from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# --- Configuration ---
load_dotenv()  # Load environment variables from .env file

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY environment variable is not set.")

genai.configure(api_key=GOOGLE_API_KEY)

# --- Model Initialization ---
try:
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    raise RuntimeError(f"Failed to initialize Gemini model: {e}") from e

# --- FastAPI App ---
app = FastAPI(
    title="AI Chatbot API",
    description="API for interacting with a Gemini chatbot.",
    version="1.0.0",
)

# --- CORS Configuration ---
# NOTE: No trailing slashes in origins
origins = [
    "http://localhost:5173",               # local dev frontend
    "https://basic-chatbot-xi.vercel.app", # deployed Vercel frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # allow OPTIONS, POST, GET, etc.
    allow_headers=["*"],
)

# --- Data Models ---
class ChatInput(BaseModel):
    user_message: str

# --- API Endpoints ---
@app.get("/", tags=["Health"])
async def health_check():
    """Endpoint to check the API's health status."""
    return {"status": "ok"}


@app.post("/chat", tags=["Chat"])
async def chat(chat_input: ChatInput):
    """Endpoint for chatting with the AI model."""
    try:
        response = model.generate_content(chat_input.user_message)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating content: {e}")
