FROM python:3.11-slim

WORKDIR /app

# Install system deps needed for sentence-transformers & FAISS
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the model during build
RUN python -c "from sentence_transformers import SentenceTransformer; \
               print('Downloading all-MiniLM-L12-v2...'); \
               model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2'); \
               print('Model downloaded.')"

COPY . /app

EXPOSE 5000

CMD ["python", "./app.py"]