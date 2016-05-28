FROM python:3.5-slim

WORKDIR /opt/instameals

RUN mkdir instameals

RUN apt-get update && apt-get install -y --no-install-recommends \
        libproj-dev \
        gdal-bin \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN set -ex \
    && buildDeps=' \
        gcc \
    ' \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
    && pip install psycopg2 \
    && apt-get purge -y --auto-remove $buildDeps

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Diagnostic command for checking dependencies
RUN pip list --outdated

COPY ./ /opt/instameals
CMD python manage.py migrate && python manage.py runserver