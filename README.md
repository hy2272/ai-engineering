# End-to-End AI Engineering Bootcamp — Week 1

My work for Week 1 of the [End-to-End AI Engineering Bootcamp](https://maven.com/swirl-ai/end-to-end-ai-engineering): an end-to-end RAG system over an Amazon products dataset, made observable with LangSmith and evaluated with RAGAS.

## What's in here

The RAG system is built and evaluated step by step:

- `notebooks/week_1/` — the build, notebook by notebook:
  - `01` — explore & sample the Amazon products dataset
  - `02` — preprocess & embed items, index them into Qdrant
  - `03` — RAG pipeline (retrieve → augment → generate)
  - `04` — observability with LangSmith tracing
  - `05` — build a synthetic eval dataset in LangSmith
  - `06` — evaluate retrieval & generation with RAGAS
- `apps/api/` — the pipeline + eval productionized as runnable modules (FastAPI service + `evals/`)
- `apps/chatbot_ui/` — Streamlit frontend

## Stack

Qdrant (vector DB) · OpenAI (embeddings + LLM) · LangSmith (tracing + eval datasets) · RAGAS (eval metrics) · FastAPI · Streamlit · uv · Docker Compose

## Setup

```bash
cp env.example .env
```

Then fill in `.env`. Keys used in Week 1:

```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
LANGSMITH_API_KEY=your_langsmith_api_key   # for tracing + eval datasets
LANGSMITH_TRACING=true
```

## Run

```bash
make run-docker-compose      # Qdrant + FastAPI + Streamlit
make run-eval-retriever      # run the RAGAS eval over the LangSmith dataset
```

- Streamlit UI: http://localhost:8501
- FastAPI docs: http://localhost:8000/docs
- Qdrant: http://localhost:6333

---

Built by coding along the bootcamp by Aurimas Griciunas ([SwirlAI](https://www.newsletter.swirlai.com/)). Scaffolding (Streamlit UI + FastAPI split) is based on the course prerequisites repo.
