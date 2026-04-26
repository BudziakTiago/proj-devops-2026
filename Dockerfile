FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
COPY . .
CMD [ "fastapi", "run", "./src/main.py", "--port", "80" ]
