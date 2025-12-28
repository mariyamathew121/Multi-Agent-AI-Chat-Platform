from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY missing in environment variables.")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/tool", methods=["POST"])
def tool_response():
    data = request.get_json()
    task = data.get("task", "")
    return jsonify({"tool_result": f"Tool Server handled task '{task}' successfully."})


@app.route("/health")
def health():
    return jsonify({"status": "tool server running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
