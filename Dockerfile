FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /stars
WORKDIR /stars
COPY requirements.txt /stars/
RUN pip install -r requirements.txt
COPY . /stars/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080