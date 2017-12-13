 FROM python:3.5

 ENV PYTHONPATH /mysite
 ENV PYTHONUNBUFFERED 1

 RUN mkdir /mysite
 WORKDIR /mysite

 COPY requirements.txt /mysite/
 RUN pip install -r requirements.txt

 COPY . /mysite/