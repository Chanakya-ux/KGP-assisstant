"""Main assistant logic."""

from typing import List

from .rag import SimpleRAG


class KGAssistant:
    """A small assistant that retrieves relevant info."""

    def __init__(self, docs: List[str]):
        self.rag = SimpleRAG(docs)

    def ask(self, question: str) -> str:
        """Answer a question by retrieving a document."""
        return self.rag.query(question)
