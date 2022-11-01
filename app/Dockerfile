FROM python:3.8.2

COPY ./ /app/

RUN pip3.8 install -r /app/requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app/"
WORKDIR /app

EXPOSE 80

CMD [ "python", "./app/server.py", "--config=./app/config.txt"]