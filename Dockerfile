FROM python:3.10.0-bullseye

COPY ./Pipfile ./Pipfile.lock ./
RUN apt-get update && apt-get install --no-install-recommends -y \
pipenv && pipenv install --system --dev --deploy

WORKDIR /code
