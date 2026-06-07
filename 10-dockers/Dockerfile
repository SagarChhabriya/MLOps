# Start from the official python base image
FROM python:3.9

# Set the current working directory to /code
# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /code


COPY ./requirements.txt /code/requirements.txt

# Install the package dependencies in the requirements file.
# The --no-cache-dir option tells pip to not save the downloaded packages locally, as that is only if pip was going to be run again to install the same packages, but that's not the case when working with containers.

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the ./app directory inside the /code directory.
COPY ./app  /code/app

# Set the command to use fastapi run, which uses Uvicorn underneath.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# docker build -t myimage .
# dockerfile parse error on line 2: COPY requires at least two arguments, but only one was provided. Destination could not be determined

# docker run -d --name mycontainer -p 80:80 myimage
