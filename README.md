# stock-data-load

Your Selected Project Automated Stock Market Data ETL Pipeline using Apache airflow 

Objective:

Fetch daily stock prices, process the data, and generate a summary dashboard. Workflow:Fetch Data: Use an API like Alpha Vantage or Yahoo Finance. Transform Data: Clean and compute metrics (daily returns, moving averages). Load Data: Save to a PostgreSQL database or S3. Generate Report: Create a CSV/Excel report or push to a dashboard tool. Notify: Send a daily email with the latest report.Airflow Concepts: DAGS, PythonOperator, scheduling, and email notifications. -- Create a Architecture for the above datapipeline description using aws tools , in which we should only be using the free trial account in aws.