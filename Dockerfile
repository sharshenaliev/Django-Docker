FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt &&\
    apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
ADD . /code/
