 FROM python:3.7.0-alpine3.8
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev bash
 ADD requirements/base.txt requirements.txt
 RUN pip install -r requirements.txt