#To start the app you need to:
#Build it - sudo docker build . -t app
#Run it - sudo docker run -it -p 8000:8000 app
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

CMD flask --app app run --host 0.0.0.0
