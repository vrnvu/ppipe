FROM python:3.8-slim

WORKDIR /ppipe
COPY poetry.lock pyproject.toml /ppipe/


RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

COPY . /ppipe