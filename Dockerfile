FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

COPY . .

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "80"]