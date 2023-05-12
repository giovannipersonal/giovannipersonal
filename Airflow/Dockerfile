FROM apache/airflow:2.5.1
USER root
RUN apt-get update \
  && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
  && echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc \
  && source ~/.bashrc \
  && sudo apt-get install -y unixodbc-dev \
  && sudo apt-get install -y libgssapi-krb5-2\
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* 
USER airflow
RUN pip install --no-cache-dir --user pandas
RUN pip install --no-cache-dir --user apache-airflow-providers-microsoft-mssql[common.sql]
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --user pyodbc
RUN pip install --no-cache-dir --user pymssql
