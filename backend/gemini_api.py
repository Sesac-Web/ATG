#AIzaSyAqDsFxOVICEuEAqV4r9OHAXlEY7r_NYPA

import os
import google.generativeai as genai
from dotenv import load_dotenv

genai.configure(api_key=os.getenv("GEMINI_API_KEY")) #이전에 인증된 세션 정보가 캐시(cache)에 남아있음 

def request_gemini_api(prompt: str="test"):

  # Create the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-exp-1206",
    generation_config=generation_config,
  )

  chat_session = model.start_chat(
    history=[
    ]
  )

  #메세지 보내기
  response = chat_session.send_message(prompt)

  #print(response.text)
  return response.text