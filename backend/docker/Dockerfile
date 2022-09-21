FROM python:3.9-slim

WORKDIR /junosapp

COPY ./requirements.txt /junosapp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /junosapp/requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "15000"]