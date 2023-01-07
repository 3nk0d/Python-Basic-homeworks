FROM tiangolo/uwsgi-nginx-flask:python3.9

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN pip install poetry==1.2.2

RUN poetry config virtualenvs.create false --local

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root --without dev

COPY ./app /app
