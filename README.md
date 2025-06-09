# KGP Assistant

A smart assistant for IIT Kharagpur students. It combines a tiny Retrieval-Augmented Generation (RAG) pipeline, a REST API and a simple Streamlit UI. The goal is to keep the project minimal and fully open source.

## Project Structure

- `agent/` – RAG components and assistant logic
- `api/` – FastAPI routes
- `frontend/` – Streamlit interface
- `kgp_assistant/` – command line entry point
- `utils/` – small helpers
- `tests/` – basic test coverage

## Getting Started

```bash
# install dependencies
pip install -r requirements.txt

# run the assistant in the terminal
python kgp_assistant/main.py
```

To start the API server:

```bash
python api/server.py
```

Run the Streamlit demo:

```bash
streamlit run frontend/app.py
```

## Testing

Run the tests with `pytest`:

```bash
pytest
```
