"""Simple retrieval module using TF-IDF."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List


class SimpleRAG:
    """A very small retrieval system."""

    def __init__(self, docs: List[str]):
        self.docs = docs
        self.vec = TfidfVectorizer()
        self.doc_vecs = self.vec.fit_transform(docs)

    def query(self, text: str) -> str:
        """Return the most relevant document for the query."""
        q_vec = self.vec.transform([text])
        sims = cosine_similarity(q_vec, self.doc_vecs)[0]
        idx = sims.argmax()
        return self.docs[idx]
