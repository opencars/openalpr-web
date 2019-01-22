FROM debian
LABEL maintainer Ali Shanaakh <github@shanaakh.pro>

RUN apt-get update && apt-get install -y python-pip python-openalpr
RUN pip install flask

COPY . .

EXPOSE 8080

CMD ["python", "openalpr_web.py"]
