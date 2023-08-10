FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY ./src ./src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT python ./src/manage.py runserver 0.0.0.0:8000
