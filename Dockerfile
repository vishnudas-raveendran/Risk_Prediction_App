FROM python:3.9-slim
COPY ./requirements.txt /deploy/
COPY ./deploy/models /deploy/models/
WORKDIR /deploy/
RUN pip install -r requirements.txt
COPY ./templates /deploy/templates/
COPY ./static /deploy/static/
COPY ./server.py /deploy/
COPY ./dl_predict.py /deploy/
COPY ./customResponse.py /deploy/
CMD ["gunicorn","-b","0.0.0.0:5000","server:app"]
#ENTRYPOINT ["python", "server.py"]