FROM python:3.6

ADD ./code /app 

WORKDIR   /app/code

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","manage.py runserver"]
