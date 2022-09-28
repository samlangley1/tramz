FROM python:3.9

ADD config.py /
ADD main.py /
ADD requirements.txt /
ADD ./images/ /images/

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

