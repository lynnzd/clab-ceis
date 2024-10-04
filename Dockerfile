# Use the official Python image with version 3.12
FROM python:3.12.2

# Install Poetry
RUN pip install poetry

RUN mkdir -p /app/clab_ceis/
# Set the working directory
WORKDIR /app
COPY . /app/

# Run poetry install during build
RUN poetry install
