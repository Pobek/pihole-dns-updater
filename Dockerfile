FROM python:3.8-alpine

ADD . /app

WORKDIR /app

EXPOSE 9090

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
