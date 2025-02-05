# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
