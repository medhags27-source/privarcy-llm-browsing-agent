from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Privacy-Preserving LLM Browsing Agent backend is running!"}