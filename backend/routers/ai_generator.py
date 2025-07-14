from fastapi import APIRouter, Form
from openai import OpenAI
from dotenv import load_dotenv
import os

router = APIRouter()
load_dotenv()

@router.get("/")
async def health_check():
    return {"status": "healthy"}

@router.post("/generate-note")
async def generate_note(text: str = Form(...)):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    print(f"generating notes for {text}")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an ABA therapist assistant. Turn session notes and metadata into clear, professional therapy documentation. Maintain a clear and professional tone as well as clinical accuracy."},
                {"role": "user", "content": f"Convert the following session observations and other metadata into a detailed session note.  Session notes: {text}"}
            ],
            temperature=0.7,
        )

        return {"note": response.choices[0].message.content}

    except Exception as e:
        print("Error generating note:", str(e))
        return {"error": "AI generation failed. Please try again."}