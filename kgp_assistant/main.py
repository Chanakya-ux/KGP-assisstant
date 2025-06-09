"""Command line interface for the assistant."""

from agent import KGAssistant

DOCS = [
    "IIT Kharagpur was established in 1951.",
    "The institute has two main semesters each year.",
    "The central library houses thousands of books."
]


def main() -> None:
    """Run a simple CLI loop."""
    assistant = KGAssistant(DOCS)
    print("Type 'exit' to quit")
    while True:
        question = input("Ask: ")
        if question.lower() in {"exit", "quit"}:
            break
        print(assistant.ask(question))


if __name__ == "__main__":
    main()
