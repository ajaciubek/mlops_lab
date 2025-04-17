# Dockerfile

# Use a minimal Python image as the base
FROM python:3.12.8-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    curl libsnappy-dev make gcc g++ libc6-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz \
    | tar xz && mv uv-x86_64-unknown-linux-gnu/uv /usr/local/bin/

# Copy only dependency files first (to leverage caching)
COPY pyproject.toml .
COPY uv.lock .

# Install project dependencies using uv
RUN uv pip install --system -r pyproject.toml

# Copy the rest of the application code
COPY . . 

# Expose the application port
EXPOSE 8000

# Run the application with uv
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
