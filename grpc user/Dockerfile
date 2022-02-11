#FROM python:3-alpine
#
#RUN apk update && apk upgrade
#RUN apk add build-base linux-headers
#RUN apk add --no-cache gcc\
#                       musl-dev\
#                       libffi-dev
#
#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app
#
#COPY . /usr/src/app
#
#RUN pip install --upgrade pip
#RUN pip3 install --no-cache-dir -r requirements.txt
##RUN python -m pip install grpcio
##RUN python -m pip install grpcio-tools

FROM python-grpc-image
RUN cd /usr
RUN mkdir /src
WORKDIR /src
COPY . /src

EXPOSE 50000

ENTRYPOINT ["python3", "user_server.py"]