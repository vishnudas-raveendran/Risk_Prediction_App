FROM python:3.9-slim
COPY ./requirements.txt /deploy/
COPY ./models /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
COPY ./templates /deploy/
COPY ./server.py /deploy/
EXPOSE 5000
ENTRYPOINT ["python", "server.py"]