from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is missing.")

# NEW Gemini API client
client = genai.Client(api_key=GEMINI_API_KEY)

# FIXED MODEL NAME
MODEL_NAME = "models/gemini-2.0-flash"    # <-- use this

app = Flask(__name__)
CORS(app)

@app.route("/query", methods=["POST"])
def query_agent():
    data = request.get_json()
    query_text = data.get("query", "")

    if not query_text.strip():
        return jsonify({"error": "Query cannot be empty"}), 400

    try:
        # New API request format
        result = client.models.generate_content(
            model=MODEL_NAME,
            contents=query_text
        )

        return jsonify({"answer": result.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    return jsonify({"status": "knowledge agent running (Gemini new API)"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
