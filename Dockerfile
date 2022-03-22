# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /drf_react_postgres_docker

# Install dependencies
COPY Pipfile Pipfile.lock /drf_react_postgres_docker/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /drf_react_postgres_docker/