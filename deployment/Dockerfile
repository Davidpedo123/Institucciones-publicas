FROM python:3.11-slim


WORKDIR /src


COPY ../src /src
RUN ls -la 

RUN pip install --no-cache-dir -r /src/lib/requirements.txt


CMD ["python3", "app/main.py"]