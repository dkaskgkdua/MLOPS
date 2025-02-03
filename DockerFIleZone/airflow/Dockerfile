FROM python:3.12-slim

ENV AIRFLOW_HOME=/usr/local/airflow

RUN apt-get update && \
    apt-get install -y gcc libc-dev vim && \
    rm -rf /var/lib/apt/lists/*

RUN pip install apache-airflow
RUN pip install pandas
RUN pip install scikit-learn

RUN mkdir -p $AIRFLOW_HOME
WORKDIR $AIRFLOW_HOME
RUN airflow db init

COPY hello_airflow_dag.py $AIRFLOW_HOME/dags/
COPY ml_airflow_dag.py $AIRFLOW_HOME/dags/

EXPOSE 8080

CMD airflow webserver -p 8080 & airflow scheduler

# airflow 계정생성 명렁어
# airflow users create --username admin --firstname admin --lastname song --role Admin --email dkaskgkdua@gmail.com
# airflow dags reserialize
# pip install scikit-learn