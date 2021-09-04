FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/hale-in/web-app2.git

WORKDIR /home/web-app2/

RUN echo "SECRET_KEY=django-insecure-jaixc&0&$)=4a-t8q--1v_aj3g(l+9o@c%0ycz+w%m=a59m7p#'" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]