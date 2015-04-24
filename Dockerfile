FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-scaffold
WORKDIR /django-scaffold
ADD requirements.txt /django-scaffold/
RUN pip install -r requirements.txt
ADD . /django-scaffold/
