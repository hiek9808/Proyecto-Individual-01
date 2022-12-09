FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app_fast_api /app_fast_api

CMD ["uvicorn", "app_fast_api.main:app", "--host", "0.0.0.0", "--port", "80"]