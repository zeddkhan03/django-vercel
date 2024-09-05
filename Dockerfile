# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the app
EXPOSE 8000

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run the command to start your app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tasklist.wsgi:application"]
