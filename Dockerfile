FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.lock /app/
RUN pip install -r requirements.lock
COPY . /app/
