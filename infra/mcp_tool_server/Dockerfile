# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirement file first (for Docker cache efficiency)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt --timeout=300 --retries=10 --progress-bar off

# Copy the rest of the application code
COPY . .

# Expose port 8002 for this service
EXPOSE 8002

# Command to run the Flask app
CMD ["python", "mcp_tool.py"]
