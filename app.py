from flask import Flask, request
import google.generativeai as genai, os
from dotenv import load_dotenv

# Create Flask App
app = Flask(__name__)
# App is in Production Mode
app.debug = False

# Get gemini key
load_dotenv(".env")
genai.configure(api_key=os.getenv("KEY"))
# The model
model = genai.GenerativeModel("gemini-2.0-flash-exp")


# Base route
@app.route("/")
def index():
    return "Flask app is running!"


# To get gemini responses
@app.route("/gemini", methods=["GET", "POST"])
def get_gemini_response(prompt: str = "Say 'Generating...'") -> dict:
    prompt = request.args.get("prompt")
    prompt = prompt if prompt else "Say 'Generating...'"
    response = model.generate_content(prompt)
    return response.to_dict()


if __name__ == "__main__":
    app.run()
