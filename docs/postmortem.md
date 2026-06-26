# Post-Mortem

## Scaling Challenge

One challenge is scaling the Retriever Agent when handling a large number of independent tasks. Running too many asynchronous tasks simultaneously could increase memory usage and reduce overall performance.

A future improvement would be introducing dynamic worker pools or task queues to better distribute workload.

---

## Design Improvement

If I were redesigning the project, I would separate agent communication using an event-driven architecture instead of direct function calls.

This would make it easier to add new agents without modifying the Executor.

---

## Trade-offs

### 1. Simplicity vs Flexibility

I chose a simple manually implemented orchestration pipeline instead of using frameworks like LangGraph or CrewAI.

This makes the system easier to understand and clearly demonstrates the internal execution flow, although it requires writing more orchestration logic.

---

### 2. Simulated Retrieval vs Live APIs

The Retriever Agent currently returns simulated information instead of calling external APIs.

This keeps the project lightweight, predictable, and easier to evaluate, but limits access to real-time information.