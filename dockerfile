FROM python:3.12.6

WORKDIR /app
COPY . /app

RUN pip install Flask 

EXPOSE 80

CMD [ "python", "./app.py" ]