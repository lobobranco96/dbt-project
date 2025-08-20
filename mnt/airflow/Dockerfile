FROM quay.io/astronomer/astro-runtime:13.1.0

RUN pip install dbt-core dbt-postgres

COPY ../python/src/ /usr/local/airflow/src/

WORKDIR /usr/local/airflow