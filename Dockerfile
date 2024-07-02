FROM python:3.11

COPY requirements.txt /requirements.txt

COPY core /core

COPY main.py / main.py

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/main.py"]