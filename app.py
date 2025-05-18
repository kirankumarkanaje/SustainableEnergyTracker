from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# Setup your OpenAI API key (store it securely in production!)
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-xxxxxxxxxxxxxxxxxxxx")

app = FastAPI(title="🧠 AI Quote Generator")

class QuoteResponse(BaseModel):
    quote: str

@app.get("/", response_model=QuoteResponse)
async def generate_quote():
    prompt = (
        "Give me one original, short inspirational quote in under 20 words."
        "It should sound wise, uplifting, and modern."
    )
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=60,
            temperature=0.8,
        )
        quote = response.choices[0].text.strip().strip('"')
        return {"quote": quote}
    except Exception as e:
        return {"quote": f"Oops! Something went wrong: {e}"}
