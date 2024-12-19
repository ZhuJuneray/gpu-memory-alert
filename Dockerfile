FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# Set working directory
WORKDIR /app

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY requirements.txt .
COPY src/ ./src/
COPY config/ ./config/
COPY main.py .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python3", "main.py"]
