FROM python:slim-buster
WORKDIR /flask-docker

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV MY_ENV=AshishBadgujar
EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]
