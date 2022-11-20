FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip
RUN pip install poetry==1.2.2

RUN poetry config virtualenvs.create false --local

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000

EXPOSE 8000