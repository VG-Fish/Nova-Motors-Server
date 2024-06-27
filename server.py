from flask import Flask
import google.generativeai as genai, os
from dotenv import load_dotenv

# Create Flask App
app = Flask(__name__)

# Get gemini key
load_dotenv(".env")
genai.configure(api_key=os.getenv("KEY"))
# The model
model = genai.GenerativeModel('gemini-1.5-flash')

# To get gemini responses
@app.route("/gemini")
def get_gemini_response(prompt: str = "Say 'Generating...'") -> dict:
    response =  model.generate_content(prompt)
    return response.to_dict()