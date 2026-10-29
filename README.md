
# AI Text Summarizer

A Python application that uses Groq LLMs and LangGraph to edit text and generate concise summaries from `.txt` files.

## Tech Stack

- Python
- LangGraph
- LangChain Groq
- Pydantic

## Workflow

```text
Text File → Edit Text → Summarize → Output
```

## Project Structure

```text
src/
├── main.py
├── nodes.py
├── state.py
└── graph.py
```

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_api_key
   GROQ_MODEL=your_supported_model
   ```

## Run

```bash
python -m src.main
```

Enter the path to your `.txt` file when prompted.

## Features

- Grammar and spelling correction
- AI-powered text summarization
- Sequential workflow using LangGraph
- Environment-based API configuration
