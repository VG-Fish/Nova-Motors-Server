from flask import Flask
import google.generativeai as genai, sys, os
from dotenv import load_dotenv

# Create Flask App
app = Flask(__name__)

# Get Gemini Key
load_dotenv(".env")
genai.configure(api_key=os.getenv("KEY"))
# The model
model = genai.GenerativeModel('gemini-1.5-flash')

# To get gemini responses
@app.route("/")
def get_response(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text