# Use an official Python runtime as a parent image
FROM ubuntu

# Copy the current directory contents into the container at /app
#ADD . /app

# Install software 
RUN apt-get update
RUN apt-get install -y git

# Clone the conf files into the docker container
RUN git clone https://github.com/AlexShkunov/experiments.git

# Set the working directory to /app
WORKDIR /experiments/r-base

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["./run.sh"]

