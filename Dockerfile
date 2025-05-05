FROM python:3.12-alpine AS base

RUN python -m venv .venv

FROM python:3.12-alpine AS dependencies

ENV PATH="/.venv/bin:$PATH"

COPY --from=base .venv .venv
COPY requirements requirements

RUN pip install -r requirements/backend.in

FROM python:3.12-alpine AS app

COPY --from=dependencies .venv .venv

WORKDIR /app
COPY build build
COPY spaceship spaceship

ENV PATH="/.venv/bin:$PATH"
ENTRYPOINT ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]