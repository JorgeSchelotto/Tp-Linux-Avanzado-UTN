FROM python:buster
WORKDIR /app
COPY script.py .
CMD ["python", "/app/script.py"]

