FROM python:3.9-buster

WORKDIR /var/app

RUN pip install --upgrade pip
RUN pip install poetry==1.2.2

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8000