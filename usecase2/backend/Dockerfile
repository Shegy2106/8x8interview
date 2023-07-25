# Use the official Python image as the base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application files into the container
COPY . .

# Expose the port that Uvicorn will run on (by default, Uvicorn uses port 8000)
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "src.spreadsheet_api:app", "--host", "0.0.0.0", "--port", "8000"]
