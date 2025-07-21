FROM python:3.11-slim

WORKDIR /workspace
ADD ./requirements.txt /workspace/requirements.txt
RUN pip install -r requirements.txt
