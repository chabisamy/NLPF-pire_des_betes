 FROM python:3.5

 ENV PYTHONPATH /nlpf
 ENV PYTHONUNBUFFERED 1

 RUN mkdir /nlpf
 WORKDIR /nlpf

 COPY requirements.txt /nlpf/
 RUN pip install -r requirements.txt

 COPY . /nlpf/