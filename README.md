# Agentic AI Multi-Step Task System

## Overview

This project is a simple Agentic AI system that demonstrates how complex user requests can be broken into smaller tasks and solved using multiple specialized AI agents.

Instead of relying on an external agent framework, the entire orchestration logic is implemented manually to clearly demonstrate how an agent pipeline works internally.

The system accepts a user request, creates an execution plan, retrieves information, analyzes the results, generates a final report, and exposes the complete workflow through a FastAPI API.

---

## Features

- Accepts complex user requests
- Automatically decomposes tasks into multiple steps
- Uses specialized agents:
  - Planner Agent
  - Retriever Agent
  - Analyzer Agent
  - Writer Agent
- Async task execution using asyncio
- Manual batching implementation
- Graceful failure handling with retries
- Streaming progress updates
- FastAPI REST API
- Interactive Swagger documentation

---

## Project Structure

```
agentic-ai-system/
│
├── agents/
│   ├── planner.py
│   ├── retriever.py
│   ├── analyzer.py
│   └── writer.py
│
├── orchestrator/
│   ├── executor.py
│   ├── batcher.py
│   └── failure_handler.py
│
├── api/
│   └── app.py
│
├── docs/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. The user submits a request.
2. The Planner Agent creates an execution plan.
3. Retriever Agents collect required information asynchronously.
4. The Analyzer Agent compares and summarizes the retrieved data.
5. The Writer Agent generates the final report.
6. The Executor coordinates the entire workflow.

---

## Installation

```bash
git clone <repository-url>

cd agentic-ai-system

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Run

```bash
python3 main.py
```

or

```bash
uvicorn api.app:app --reload
```

---

## API Documentation

```
http://127.0.0.1:8000/docs
```

---

## Technologies Used

- Python 3
- Asyncio
- FastAPI
- Uvicorn
- Pydantic

---

## Future Improvements

- Integrate real LLM APIs
- Add database support
- Support additional agent types
- Real-time web search
- Distributed task execution

## 🎥 Demo Video

📹 **Project Demonstration Video**

[Watch the Demo Video](https://drive.google.com/file/d/1vujpJHO0fFmCI9rsxMa4AME0g-qCHFgK/view?usp=sharing)

---

## Author

Sourav Kumar