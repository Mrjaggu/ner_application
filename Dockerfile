# Use the official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install pip and upgrade it to the latest version
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*
    
# Install SpaCy and the English model
RUN pip install spacy && \
    python -m spacy download en_core_web_sm

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port that Flask runs on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
