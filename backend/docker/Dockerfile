FROM python:3.9-slim


ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

ENV \
    USER_DB=test \
    PASS_DB=test \
    SERV_DB=test

WORKDIR /backend

COPY ./requirements.txt /backend/

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY . .

RUN rm ./.env ./.env.exemple

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "15000"]
