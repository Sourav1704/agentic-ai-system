# System Architecture

## Overview

The system follows an agent-based pipeline architecture.

```
User Request
      │
      ▼
Planner Agent
      │
      ▼
Execution Plan
      │
      ▼
Batcher
      │
      ▼
Retriever Agents (Async)
      │
      ▼
Analyzer Agent
      │
      ▼
Writer Agent
      │
      ▼
Final Report
```

---

## Components

### Planner Agent

Responsible for understanding the user request and generating an execution plan.

---

### Retriever Agent

Collects the required information for each task.

Multiple Retriever Agents can execute simultaneously using asyncio.

---

### Analyzer Agent

Processes retrieved information and generates a structured comparison.

---

### Writer Agent

Converts the structured analysis into a readable report.

---

### Executor

Coordinates communication between all agents.

---

### Failure Handler

Retries failed tasks before stopping the pipeline gracefully.

---

### Batcher

Groups tasks into fixed-size batches for controlled execution.

---

## Data Flow

User Request

↓

Planner

↓

Execution Plan

↓

Batch Creation

↓

Retriever Agents

↓

Analysis

↓

Report Generation

↓

Response