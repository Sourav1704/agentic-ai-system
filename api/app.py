"""
FastAPI Application

Exposes the Agentic AI System as a REST API.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

from orchestrator.executor import Executor

app = FastAPI(
    title="Agentic AI System",
    version="1.0.0",
    description="Multi-Agent AI System using Planner, Retriever, Analyzer and Writer."
)


class UserRequest(BaseModel):
    request: str


@app.get("/")
async def home():

    return {
        "message": "Agentic AI System is Running"
    }


@app.post("/execute")
async def execute_task(user_request: UserRequest):

    executor = Executor()

    result = await executor.execute(user_request.request)

    return {
        "status": "success",
        "result": result
    }