FROM python:3.9.0

WORKDIR /home/

RUN echo 'chunsoccute'

RUN git clone https://github.com/hale-in/web-app2.git

WORKDIR /home/web-app2/

#RUN echo "SECRET_KEY=django-insecure-jaixc&0&$)=4a-t8q--1v_aj3g(l+9o@c%0ycz+w%m=a59m7p#'" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=dgwangya2.settings.deploy && python manage.py migrate --settings=dgwangya2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=dgwangya2.settings.deploy dgwangya2.wsgi --bind 0.0.0.0:8000"]