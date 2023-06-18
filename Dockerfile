FROM python:3.8


WORKDIR /app


ADD . /app


RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "entrypoint.py"]