FROM python:3.8-slim

WORKDIR /wikiqueue
COPY poetry.lock pyproject.toml /wikiqueue/


RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /wikiqueue