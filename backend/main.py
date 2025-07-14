from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    return {"status": "healthy"}

@app.post("/generate-note")
async def generate_note(text: str = Form(...)):
    print(f"generating notes for {text}")
    return {"note": "These are the ai placeholder notes. Replace with ai call response."}