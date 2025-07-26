FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/agile-calculator/

WORKDIR /agile-calculator
ADD ./requirements.txt /agile-calculator/requirements.txt
RUN pip install -r requirements.txt
