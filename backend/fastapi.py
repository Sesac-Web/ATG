import gemini_api
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def call_gemini_api():
    response_text = gemini_api.request_gemini_api("테스트")
    
    result = {
        "response_text" : response_text 
    }

    return result
