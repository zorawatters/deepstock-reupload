from flask import Flask
from flask_cors import CORS
import yfinance as yf
import json
from flask_jsonpify import jsonpify

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/message')
def get_message():
  return 'Hello Stonks'

@app.route('/stock_data')
def get_stock_data():
	msft = yf.Ticker("MSFT")
	
	dataframe = msft.history(period="1")
	print(dataframe)
	#dataframe['Date'] = dataframe['Date'].dt.strftime('%Y-%m-%d')
	return dataframe.reset_index().to_json(orient='records', date_format='iso')	


app.run(host='0.0.0.0')
 	