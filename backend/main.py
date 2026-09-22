from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PageData(BaseModel):
    content: str


@app.get("/")
def home():
    return {
        "message": "Privacy-Preserving LLM Browsing Agent backend is running!"
    }


@app.post("/api/capture")
def capture_page(data: PageData):
    return {
        "message": "Page received successfully",
        "content_length": len(data.content)
    }