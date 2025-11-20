# Dockerfile
FROM python:3.12-slim

# Don’t buffer stdout/stderr, easier logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

EXPOSE 5001

# Start the Flask app
CMD ["python", "app.py"]