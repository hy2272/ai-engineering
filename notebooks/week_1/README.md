# Week 1 — end-to-end RAG + eval pipeline

Build a RAG system over an Amazon products dataset, make it observable, and evaluate it. Setup & run commands are in the [repo README](../../README.md); this page is the Week 1 detail.

## Notebooks (run in order)

| # | Notebook | What it does |
|---|----------|--------------|
| 01 | `01-explore-amazon-dataset` | explore & sample the Amazon dataset — keep 2022–23 items with ≥100 ratings, random-sample 1000 |
| 02 | `02-RAG-preprocessing-items` | preprocess title/features → embed (`text-embedding-3-small`, 1536d) → create Qdrant collection (cosine) → upsert PointStructs |
| 03 | `03-RAG-pipeline` | RAG pipeline: query → embed → retrieve top-k → format context → prompt → generate |
| 04 | `04-Observability-foundations` | same pipeline + `@traceable` → LangSmith traces |
| 05 | `05-RAG-Eval-Dataset` | dump Qdrant → LLM generates synthetic question + reference ids → LangSmith dataset |
| 06 | `06-RAG-Evals` | evaluate with RAGAS: ID-based precision/recall (retrieval) + faithfulness/relevancy (generation) |

## Productionized

The same pipeline + eval also live as runnable modules:

- `apps/api/src/api/agents/retrieval_generation.py` — the RAG pipeline
- `apps/api/evals/eval_retriever.py` — the RAGAS eval, run with `make run-eval-retriever`

## Key concepts

- Qdrant collection `size` must equal the embedding dimension (1536); cosine distance for text.
- A point's `payload` stores metadata alongside the vector, so retrieval returns ids/descriptions, not just vectors.
- Metrics split two ways: **ID-based** (precision/recall — local, instant, free) vs **LLM-based** (faithfulness/relevancy — slow, costs tokens).

Snapshot: tag `week-1-complete`.
