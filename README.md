A production-grade multi-agent AI system capable of answering user queries in real time.
Built with Flask, Gemini API, Docker & a custom orchestrator — deployed locally with a modern chat UI.

Overview:-

This project is a multi-agent AI architecture where each agent can independently process tasks such as knowledge-based answers, reasoning, summarization, or general chat.
It features:

#Orchestrator Service – routes user prompts to the appropriate AI agent

#Knowledge Agent (Gemini) – generates responses using Google Gemini AI

#Web-based Chat UI – modern interactive interface for real-time chat

#Docker-ready microservices architecture

#Voice Input + Text-to-Speech output

#Environment-based API key security

-> Architecture Diagram
 ┌──────────────┐       POST /query        ┌────────────────────┐
 │  Frontend UI │  ─────────────────────▶  │   Orchestrator API │
 └──────────────┘                           │  (Flask – port 8000│
                                            └──────┬─────────────┘
                                                   │
                                                   ▼
                                         ┌──────────────────────────┐
                                         │ Knowledge Agent (Gemini) │
                                         │ Flask – port 8001        │
                                         │ Generates final response │
                                         └──────────────────────────┘

🛠️ Tech Stack
Component	Technology
Frontend	HTML, JavaScript, Speech-to-Text, Text-to-Speech
Backend APIs	Flask, Python
AI Model	Google Gemini API
Deployment	Docker Compose
Communication	REST API

  Features
Feature	Status
🔹 User chat input	✔️
🔹 Gemini AI text generation	✔️
🔹 Text-to-Speech human-like voice output	✔️
🔹 Optional voice recognition input	✔️
🔹 Microservice orchestration	✔️
🔹 Docker-ready	✔️
🔹 Developer-friendly modular code	✔️

🏁 Getting Started – Run Locally
1️⃣ Clone Repository
git clone https://github.com/<your-username>/multi-agent-adk.git
cd multi-agent-adk

2️⃣ Install Dependencies
pip install -r infra/orchestrator/requirements.txt
pip install -r infra/knowledge_agent/requirements.txt

3️⃣ Add API Key

Create a .env file (NOT committed to GitHub)

GEMINI_API_KEY=your_key_here

4️⃣ Run Services
cd infra/knowledge_agent
python main.py

cd infra/orchestrator
python main.py

5️⃣ Open Frontend
cd project-folder
python -m http.server 5500


Open 👉 http://localhost:5500/frontend.html

