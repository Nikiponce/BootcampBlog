FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create code folder.
RUN mkdir /code

# Set working dir.
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY ./src/requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

        
