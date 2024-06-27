from flask import Flask
import google.generativeai as genai, os
from dotenv import load_dotenv
from portpicker import pick_unused_port

# Create Flask App
app = Flask(__name__)

# Get Gemini Key
load_dotenv(".env")
genai.configure(api_key=os.getenv("KEY"))
# The model
model = genai.GenerativeModel('gemini-1.5-flash')

# To get gemini responses
@app.route("/")
def get_gemini_response(prompt: str = "Say 'Generating...'") -> str:
    response = model.generate_content(prompt)
    return response.text
