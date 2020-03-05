from flask import Flask
from flask_cors import CORS
import yfinance as yf
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/message')
def get_message():
  return 'Hello Stonks'

@app.route('/stock_data')
def get_stock_data():
	msft = yf.Ticker("MSFT")
	print(msft.info)

app.run(host='0.0.0.0')
