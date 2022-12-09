FROM tiangolo/uvicorn-gunicorn:python3.10

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY app /app_fast_api

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]