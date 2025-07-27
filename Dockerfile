FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH="/agile-calculator/"
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

RUN pip install uv
WORKDIR /agile-calculator
ADD . ./
RUN uv sync
