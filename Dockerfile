FROM python:3.9-slim
COPY ./requirements.txt /deploy/
COPY ./deploy/models /deploy/models/
WORKDIR /deploy/
RUN pip install -r requirements.txt
COPY ./templates /deploy/templates/
COPY ./static /deploy/static/
COPY ./server.py /deploy/
EXPOSE 80
CMD ["gunicorn","-w","4","-b","0.0.0.0:80","server:app"]
#ENTRYPOINT ["python", "server.py"]