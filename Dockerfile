FROM ubuntu:bionic
MAINTAINER Tejashri Parurkar "tparurkar@gmail.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
