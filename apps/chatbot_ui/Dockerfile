FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# copy workspace root files for dependency resolution
COPY pyproject.toml uv.lock ./

# Copy package files and source
COPY apps/chatbot_ui ./apps/chatbot_ui


# Enable bytecode compilation and Python optimization
ENV UV_COMPILE_BYTECODE=1

# Install dependencies including workspace packages
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --package chatbot_ui

# Enable bytecode compilation and python optimization
ENV PYTHONOPTIMIZE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# set PATH to use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/apps/chatbot_ui/src:$PYTHONPATH"

# Create non-root user and set permissions
RUN addgroup --system app && \
    adduser --system --ingroup app app && \
    chown -R app:app /app && \
    mkdir -p /home/app && \
    chown -R app:app /home/app && \
    mkdir -p /home/app/.streamlit && \
    mkdir -p /home/app/.streamlit/data && \
    mkdir -p /home/app/.streamlit/cache && \
    chown -R app:app /home/app/.streamlit

#set home directory for the user
ENV HOME=/home/app

#switch to non-root user
USER app

#Expose the streamlit port
EXPOSE 8501

WORKDIR /app/apps/chatbot_ui/src

# COmmand to run the application
CMD ["streamlit", "run", "chatbot_ui/app.py", "--server.address=0.0.0.0"]