FROM python:3

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt
RUN pip install connexion[swagger-ui]

WORKDIR /

COPY . /

CMD ["python", "server.py"]
