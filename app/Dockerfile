# Sets a pre-built package/base image for the Docker image
FROM python:3.7-alpine  
# Creates a new folder called 'app' and makes it the working directory inside the container
WORKDIR /app
# Copies everything on the current directory onto the 'app' directory inside the container
COPY . /app
# Installs the Python dependencies listed in the requirements.txt file.
RUN pip install -r requirements.txt 
# Exposes port 5000 to the operating system and informs Docker that the container will listen on port 5000 at runtime 
EXPOSE 5000
# Specifies the command that will be executed when the container starts
CMD ["python", "app.py"]