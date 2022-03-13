FROM python:3.9-slim
COPY ./requirements.txt /deploy/
COPY ./models /deploy/models/
WORKDIR /deploy/
RUN pip install -r requirements.txt
COPY ./templates /deploy/templates/
COPY ./server.py /deploy/
EXPOSE 5000
ENTRYPOINT ["python", "server.py"]