FROM python:3.10.4

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --nocache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicron", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
