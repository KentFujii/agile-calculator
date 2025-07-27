FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/agile-calculator/

# uvとruffをインストール
RUN pip install --no-cache-dir uv ruff

WORKDIR /agile-calculator
ADD . ./

# uvを使って依存関係をインストール
RUN uv pip install --system -r requirements.txt
