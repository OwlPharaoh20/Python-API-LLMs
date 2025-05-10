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


@app.post("/generate")
def generate(prompt:str):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content" : prompt }])
    return {"response" : response["message"] ["content"]}