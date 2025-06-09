from agent.rag import SimpleRAG


def test_retrieve():
    docs = ["sky is blue", "grass is green"]
    rag = SimpleRAG(docs)
    assert rag.query("color of grass") == "grass is green"
