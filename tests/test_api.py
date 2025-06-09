from fastapi.testclient import TestClient

from api.server import app


client = TestClient(app)


def test_ask():
    resp = client.post("/ask", json={"text": "when was iit kgp established"})
    assert resp.status_code == 200
    assert "answer" in resp.json()
