FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /white_ip_test
WORKDIR /white_ip_test
ADD requirements.txt /white_ip_test/
RUN pip install -r requirements.txt
ADD . /white_ip_test

CMD [ "python", "-u", "./index.py" ]