from flask import Flask
from flask_cors import CORS
from alpha_vantage.timeseries import TimeSeries
#import yfinance as yf
app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/message')
def get_message():
  return 'Hello Stonks'

@app.route('/stock_data')
def get_stock_data():
	msft = yf.Ticker("MSFT")
	print(msft.info)



'''
  Storing stock data api

  Gets json data from response body and stores it into database
'''

@app.route('/users/store_data', methods=['POST'])
def insert_document():
    req_data = request.get_json()
    collection_stock = mongo.db.stocks
    collection_stock.insert_one(req_data).inserted_id
    return ('', 204)


'''
  Diplaying stock data api

  Gets all the sotored data in the database and retruns a json file
'''


@app.route('/company/info/<string:company>', methods=['PUT'])
def update_historical_data(company):
    # msft = yf.Ticker("MSFT")
    #
    # data = msft.info


    key = 'CYNCL6X4FUN4SE0K'

    ts = TimeSeries(key)

    aapl, meta = ts.getdaily(symbol='TSL')

    return json.dumps(aapl['2020-12-03'])



@app.route('/users/display_data')
def get_documents():
    collection_stock = mongo.db.stocks
    documents = collection_stock.find()
    response = []

    for doc in documents:
        doc['_id'] = str(doc['_id'])
        response.append(doc)

    return json.dumps(response)


app.run(host='0.0.0.0')
