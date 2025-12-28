from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Knowledge agent endpoint (correct port)
KNOWLEDGE_AGENT_URL = "http://127.0.0.1:8001/query"

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.get_json()
    query_text = data.get("query", "")

    print("Received query:", query_text)

    try:
        print("Forwarding to knowledge agent...")
        response = requests.post(KNOWLEDGE_AGENT_URL, json={"query": query_text})
        print("Knowledge agent response:", response.text)

        if response.status_code == 200:
            return jsonify({"result": response.json()})
        else:
            return jsonify({
                "error": "Knowledge agent returned error",
                "details": response.text
            }), 500

    except Exception as e:
        print("❌ ERROR IN ORCHESTRATOR:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return jsonify({"status": "orchestrator running"})


if __name__ == "__main__":
    # ✅ ORCHESTRATOR MUST RUN ON PORT 8000
    app.run(host="0.0.0.0", port=8000, debug=True)
