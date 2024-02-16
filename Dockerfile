# Use the official Python image with version 3.12
FROM python:3.12.2

# Install Poetry
RUN pip install poetry

RUN mkdir -p /app/clab_prototype/
# Set the working directory
WORKDIR /app

# Copy the local folder 'clab_protoype' to the container
COPY clab_prototype /app/clab_prototype
COPY pyproject.toml /app/pyproject.toml

# Run poetry install during build
RUN poetry install

# Set the default command to start your application
CMD ["poetry"]