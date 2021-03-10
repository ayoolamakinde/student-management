FROM python:3.7-alpine

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt
RUN pip install connexion[swagger-ui]

WORKDIR /

COPY . /

EXPOSE 8080

CMD ["python", "server.py"]
