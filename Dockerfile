FROM python:2-slim-buster

LABEL maintainer Ali Shanaakh <ashanaakh@gmail.com>

RUN apt-get update

RUN apt-get install -y python-pip python-openalpr

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "server.py"]
