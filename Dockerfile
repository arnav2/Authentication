# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

COPY backend/requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY backend /app/

# Expose port 8000 to allow communication to/from the container
EXPOSE 8000

# Run the Falcon application when the container launches
CMD ["python", "app.py"]
