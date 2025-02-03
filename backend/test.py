
import os
import google.generativeai as genai
from dotenv import load_dotenv

api_key=os.getenv("GEMINI_API_KEY")
print(api_key)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)