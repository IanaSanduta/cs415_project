FROM ubuntu:22.04

COPY . /app

#RUN python manage.py runserver
RUN echo "Hello World"