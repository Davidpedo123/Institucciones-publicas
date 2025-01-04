FROM python:3.11-slim


WORKDIR /src


COPY ../src /src
RUN ls -la 

RUN pip install --no-cache-dir -r /src/lib/requirements.txt


CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--workers", "16", "--bind", "0.0.0.0:8080"]


