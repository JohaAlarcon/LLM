# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Defines an environment variable called SCRIPT with a default value
ENV SCRIPT test.py

# Executes the script specified in the SCRIPT environment variable when the container starts up
#CMD ["sh", "-c", "python $SCRIPT"] -> this way when you have the scripts in the same root of the dockerfile

CMD ["sh", "-c", "cd projects && python $SCRIPT"]

