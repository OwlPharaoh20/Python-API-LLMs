# to use fastapi for api setup and requests handling. like in javascript we have express
from fastapi import FastAPI
#import ollama to use ollama for chat 
import ollama 
#import os to use environment variables 
import os 
from dotenv import load_dotenv

load_dotenv() 
API_KEY_CREDITS = {os.getenv("API_KEY"): 5}
print(API_KEY_CREDITS)
app = FastAPI()


def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits")

    return x_api_key



@app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}

