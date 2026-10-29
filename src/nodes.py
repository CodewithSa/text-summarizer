from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from src.state import SummarizerState

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
groq_model = os.getenv("GROQ_MODEL")

if not os.getenv("GROQ_API_KEY"):
    raise ValueError(
        "groq api key not found"
    )

if not os.getenv("GROQ_MODEL"):
    raise ValueError(
        "groq model not found"
    )

llm = ChatGroq(
    api_key = api_key,
    model = groq_model
)


def edited_text_node(state: SummarizerState) -> dict:
    prompt = (
        "You are a professional copyeditor. "
        "Correct grammar, spelling, and punctuation. "
        "Preserve the original meaning and important details. "
        "Do not add new information. Return only the edited text.\n\n"
        f"Original text:\n{state.text}"
    )

    response = llm.invoke(prompt)
    return {
        "edited_text": response.content
    }

def summarizer_node(state: SummarizerState) -> dict:
    prompt = (
        "You are a professional text summarizer. "
        "Summarize the text clearly and concisely. "
        "Preserve the main ideas and important facts. "
        "Do not invent information. Return only the summary.\n\n"
        f"Text to summarize:\n{state.edited_text}"
    )

    response = llm.invoke(prompt)
    return {
        "result": response.content
    }