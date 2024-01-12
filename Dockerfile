FROM python:slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
RUN pip3 install django




RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
