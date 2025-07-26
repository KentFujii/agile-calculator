FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/agile-calculator/

WORKDIR /agile-calculator
ADD . ./
RUN pip install -r requirements.txt
