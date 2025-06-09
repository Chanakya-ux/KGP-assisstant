"""FastAPI routes."""

from fastapi import FastAPI
from pydantic import BaseModel

from agent import KGAssistant

app = FastAPI()

# Example documents. In real use, load academic materials here.
DOCS = [
    "IIT Kharagpur was established in 1951.",
    "The institute has two main semesters each year.",
    "The central library houses thousands of books."
]

assistant = KGAssistant(DOCS)


class Query(BaseModel):
    text: str


@app.post("/ask")
async def ask(q: Query):
    """Return an answer from the assistant."""
    return {"answer": assistant.ask(q.text)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
