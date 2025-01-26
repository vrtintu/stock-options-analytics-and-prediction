import yfinance as yf
import boto3
from datetime import datetime

def lambda_handler(event, context):
    ticker = event.get('ticker', 'AAPL')
    start_date = event.get('start_date', '2023-01-01')
    end_date = event.get('end_date', '2023-12-31')

    data = yf.download(ticker, start=start_date, end=end_date)
    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{ticker}_{today}.csv"

    s3_client = boto3.client('s3')
    bucket_name = event['bucket_name']
    local_path = f"/tmp/{file_name}"
    data.to_csv(local_path)
    s3_client.upload_file(local_path, bucket_name, f"daily_data/{file_name}")

    return {"statusCode": 200, "message": f"Uploaded to s3://{bucket_name}/daily_data/{file_name}"}
