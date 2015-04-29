FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/misc/requirements.txt
RUN pip install -r misc/requirements.txt
ADD . /code/
