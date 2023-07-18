FROM python:3.11.1-slim

# set work directory
RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

WORKDIR app

#CMD gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker  --bind=0.0.0.0:8000