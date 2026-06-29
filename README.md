# End-to-End AI Engineering Bootcamp — my work

My work across the [End-to-End AI Engineering Bootcamp](https://maven.com/swirl-ai/end-to-end-ai-engineering) by Aurimas Griciunas ([SwirlAI](https://www.newsletter.swirlai.com/)).

**Stack:** Qdrant (vector DB) · OpenAI (embeddings + LLM) · LangSmith (tracing + eval datasets) · RAGAS (eval metrics) · FastAPI · Streamlit · uv · Docker Compose

## Weeks

| Week | What I built | Code |
|------|--------------|------|
| 1 | End-to-end RAG over an Amazon products dataset: explore/sample → index into Qdrant → RAG pipeline → LangSmith observability → synthetic eval dataset → RAGAS evaluation | [`notebooks/week_1`](notebooks/week_1) · tag `week-1-complete` |

> Each week's code accumulates on `main`; a `week-N-complete` tag freezes that week's snapshot. Browse a week by its tag, e.g. `git checkout week-1-complete`.

## Repo layout

- `notebooks/<week>/` — the build, notebook by notebook
- `apps/api/` — pipeline + eval productionized as runnable modules (FastAPI service + `evals/`)
- `apps/chatbot_ui/` — Streamlit frontend

## Setup

```bash
cp env.example .env   # then fill in your keys
```

Keys used so far:

```
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
LANGSMITH_API_KEY=your_langsmith_api_key   # tracing + eval datasets
LANGSMITH_TRACING=true
```

## Run

```bash
make run-docker-compose      # Qdrant + FastAPI + Streamlit
make run-eval-retriever      # RAGAS eval over the LangSmith dataset (Week 1)
```

- Streamlit UI: http://localhost:8501
- FastAPI docs: http://localhost:8000/docs
- Qdrant: http://localhost:6333

## Data & citation

This project uses the Amazon Reviews 2023 dataset (McAuley Lab, UC San Diego). The dataset is **not** included in this repo (it's gitignored — download it separately). If you use this work, please cite:

```
@article{hou2024bridging,
  title={Bridging Language and Items for Retrieval and Recommendation},
  author={Hou, Yupeng and Li, Jiacheng and He, Zhankui and Yan, An and Chen, Xiusi and McAuley, Julian},
  journal={arXiv preprint arXiv:2403.03952},
  year={2024}
}
```

---

Built by coding along the bootcamp. Scaffolding (Streamlit UI + FastAPI split) is based on the course prerequisites repo.
