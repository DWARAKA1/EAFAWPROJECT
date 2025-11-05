# Use Python 3.13.5 slim image as base
FROM python:3.13.5-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better cache utilization
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Create necessary directories
RUN mkdir -p logs

# Set Python path
ENV PYTHONPATH=/app

# Expose ports (FastAPI: 8000, Streamlit: 8501)
EXPOSE 8000 8501

# Create a script to run both services
RUN echo '#!/bin/bash\n\
uvicorn src.main:app --host 0.0.0.0 --port 8000 & \
streamlit run src/frontend/streamlit_app.py --server.port 8501 --server.address 0.0.0.0\
' > /app/start.sh && chmod +x /app/start.sh

# Set the entry point
ENTRYPOINT ["/app/start.sh"]