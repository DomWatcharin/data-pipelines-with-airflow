FROM --platform=linux/amd64 apache/airflow:2.8.0

RUN pip install ccxt==4.1.100 \
  apache-airflow-providers-mongo==4.0.0 \
  pip install apache-airflow-providers-oracle==3.9.2 \
  airflow-provider-great-expectations==0.2.7
