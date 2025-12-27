FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy application
COPY . .

# Expose port
EXPOSE 7860

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
