#!/bin/bash

while ! </dev/tcp/db/5432; do sleep 1; done
echo "Generate schema"
python generate_schema.py
echo "Ending generate schema"
gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --reload --bind=0.0.0.0:8000
