FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/agile-calculator/

# uvとruffをインストール
# --no-cache-dir オプションでレイヤーサイズを削減
RUN pip install --no-cache-dir uv ruff

WORKDIR /agile-calculator
ADD . ./
