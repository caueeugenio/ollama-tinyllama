from fastapi import FastAPI, HTTPException
import ollama
from pydantic import BaseModel

app = FastAPI()
class TextRequest(BaseModel):
    text: str
    
@app.get("/")
def read_root(request: TextRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text is required")
    try:
        response = ollama.chat(model="tinyllama", messages=[
            {"role": "user", "content": request.text}
        ])	
        llm_response = response.get('message', {}).get('content', '')
        return {"Resposta da LLM": llm_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))