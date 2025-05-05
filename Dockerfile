FROM python:3.12-bullseye

WORKDIR /app
COPY . .

RUN python -m venv ./.venv
RUN . .venv/bin/activate
RUN pip install -r requirements/backend.in

ENTRYPOINT exec uvicorn spaceship.main:app --host=0.0.0.0 --port=8080