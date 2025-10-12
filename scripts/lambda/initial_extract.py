import pandas as pd
import yfinance as yf
import boto3
from botocore.exceptions import NoCredentialsError
 
tickers = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "BRK-B", "JPM", "JNJ",
    "V", "UNH", "PG", "MA", "HD", "XOM", "LLY", "ABBV", "MRK", "PEP",
    "AVGO", "COST", "KO", "ADBE", "CSCO", "TMO", "WMT", "ACN", "CVX", "MCD",
    "DHR", "NKE", "AMD", "CRM", "TXN", "AMGN", "QCOM", "UNP", "LIN", "INTC",
    "NEE", "LOW", "MS", "GS", "PM", "UPS", "BMY", "HON", "IBM", "SBUX",
    "RTX", "BLK", "CAT", "GE", "DE", "ISRG", "AMAT", "SPGI", "PLD", "SYK",
    "NOW", "CB", "MDT", "TGT", "LRCX", "ELV", "ADI", "MO", "MU", "PGR",
    "C", "ZTS", "USB", "REGN", "ADP", "MDLZ", "VRTX", "T", "BKNG", "GM",
    "F", "APD", "GILD", "FDX", "KLAC", "PANW", "CSX", "GD", "ATVI", "MNST",
    "EA", "AON", "MAR", "ROST", "AEP", "KMB", "ORLY", "IDXX", "ROK", "AZO",
    "ECL", "MET", "HCA", "PSA", "EXC", "KMI", "PCAR", "CTAS", "PAYX", "HPQ"
]
 
data = []
 
for ticker in tickers:
    try:
        info = yf.Ticker(ticker).info
        data.append({
            "Ticker": ticker,
            "Company Name": info.get("shortName"),
            "Sector": info.get("sector"),
            "P/E Ratio": info.get("trailingPE"),
            "Beta": info.get("beta"),
            "Website": info.get("website"),
            "Industry": info.get("industry"),
            "Exchange": info.get("exchange"),
            "Market Cap": info.get("marketCap"),
            "Last Price": info.get("regularMarketPreviousClose"),
            "52-Week High": info.get("fiftyTwoWeekHigh"),
            "52-Week Low": info.get("fiftyTwoWeekLow"),
            "Volume": info.get("regularMarketVolume"),
            "Average Volume": info.get("averageVolume"),
            "Open": info.get("regularMarketOpen"),
            "Bid": info.get("bid"),
            "Ask": info.get("ask"),
            "Change": info.get("regularMarketChange")
        })
    except Exception:
        data.append({
            "Ticker": ticker,
            "Company Name": None,
            "Sector": None,
            "P/E Ratio": None,
            "Beta": None
        })
 
df = pd.DataFrame(data)
df.to_csv("stock_raw.csv", index=False)



local_file = 'stock_raw.csv'
bucket_name = 'snfk-gtm'
s3_key = 'path/stock_raw.csv'  

s3 = boto3.client('s3') 

try:
    s3.upload_file(local_file, bucket_name, s3_key)
    print(f"Uploaded {local_file} → s3://{bucket_name}/{s3_key}")
except FileNotFoundError:
    print("Local file not found.")
except NoCredentialsError:
    print("AWS credentials not found.")
except Exception as e:
    print("Upload failed:", e)