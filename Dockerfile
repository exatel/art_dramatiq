FROM python:3.10.0-buster

RUN apt-get update && apt-get install --no-install-recommends -y \
    pipenv

COPY ./Pipfile ./Pipfile.lock ./
RUN pipenv install --system --dev --deploy
WORKDIR /code

