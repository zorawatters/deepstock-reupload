from flask import Flask
from flask_cors import CORS
from flask import request
from flask_pymongo import pymongo
from pymongo import MongoClient
import yfinance as yf
from datetime import tzinfo, timedelta, datetime


app = Flask(__name__)

CONNECTION_STRING = "mongodb://deep-stock-cu:deep2020stock@deep-stock-cluster-shard-00-00-bwk5a.gcp.mongodb.net:27017,deep-stock-cluster-shard-00-01-bwk5a.gcp.mongodb.net:27017,deep-stock-cluster-shard-00-02-bwk5a.gcp.mongodb.net:27017/test?ssl=true&replicaSet=deep-stock-cluster-shard-0&authSource=admin&retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('deep-stock')
collection = db['companies']


CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/message')
def get_message():
  return 'Hello Stonks'

@app.route('/stock_data')
def get_stock_data():
	msft = yf.Ticker("MSFT")
	return (str(msft.info))


@app.route('/test')
def test():
    #collection.insert_one({"name" : "test5" , "ticker" : "test5"})
    #addmetadata()
    #addFundamentals('msft')
    addMetadata('msft')
    return ("added metadata now")


# appends tweets to company tweets
@app.route("/<string:company>/tweets", methods=['PUT'])
def addTweet(company):
    new_tweet = request.get_json()
    collection.update({"ticker" : company}, {'$push': {'tweets': new_tweet}})

@app.route("/<string:company>/historicaldata", methods=['PUT'])
def addhist():
    new_hist = request.get_json()
    collection.update({"ticker" : company}, {'$push': {'historical_data': new_hist}})

@app.route("/company", methods=['POST'])
def addcompany():
    meta = yf.Ticker("company")
    companyObj = request.get_json()
    collection.insert_one(companyObj)
    #metadata, needs to trim info
    collection.update({"ticker" : "test5"}, {'$set': {'metaldata': amd.info}})
    #metadata, needs to trim fundamentals
    collection.update({"ticker" : "test5"}, {'$push': {'fundamentals': amd.info}})

def addFundamentals(company):
    comp = yf.Ticker(company)
    jsonY = comp.info
    data = {}
    print(type(jsonY))
    data.update({'shortName' : jsonY['shortName']})
    data.update({'logo_url' : jsonY['logo_url']})
    data.update({'website' : jsonY['website']})
    data.update({'symbol' : jsonY['symbol']})
    data.update({'city' : jsonY['city']})
    data.update({'phone' : jsonY['phone']})
    data.update({'industry' : jsonY['industry']})
    data.update({'country' : jsonY['country']})
    data.update({'state' : jsonY['state']})
    data.update({'currency' : jsonY['currency']})
    data.update({'longBusinessSummary' : jsonY['longBusinessSummary']})
    data.update({'zip' : jsonY['zip']})
    data.update({'sector' : jsonY['sector']})
    data.update({'fullTimeEmployees' : jsonY['fullTimeEmployees']})
    data.update({'address1' : jsonY['address1']})
    data.update({'longName' : jsonY['longName']})
    collection.update({"ticker" : "test5"}, {'$set': {'fundamentals': data}}) #for now test5 but change later

def addMetadata(company):
    comp = yf.Ticker(company)
    jsonY = comp.info
    td = datetime.now()
    td = td - timedelta(hours=5)
    data = {'date' : td}
    data.update({'sharesShort' : jsonY['sharesShort']})
    data.update({'trailingPE' : jsonY['trailingPE']})
    data.update({'trailingEps' : jsonY['trailingEps']})
    data.update({'enterpriseToRevenue' : jsonY['enterpriseToRevenue']})
    data.update({'fiftyDayAverage' : jsonY['fiftyDayAverage']})
    data.update({'averageDailyVolume10Day' : jsonY['averageDailyVolume10Day']})
    data.update({'bookValue' : jsonY['bookValue']})
    data.update({'volume' : jsonY['volume']})
    data.update({'SandP52WeekChange' : jsonY['SandP52WeekChange']})
    data.update({'fiftyTwoWeekHigh' : jsonY['fiftyTwoWeekHigh']})
    data.update({'netIncomeToCommon' : jsonY['netIncomeToCommon']})
    data.update({'averageVolume10days' : jsonY['averageVolume10days']})
    data.update({'regularMarketVolume' : jsonY['regularMarketVolume']})
    data.update({'earningsQuarterlyGrowth' : jsonY['earningsQuarterlyGrowth']})
    data.update({'52WeekChange' : jsonY['52WeekChange']})
    data.update({'sharesShortPriorMonth' : jsonY['sharesShortPriorMonth']})
    data.update({'heldPercentInsiders' : jsonY['heldPercentInsiders']})
    data.update({'marketCap' : jsonY['marketCap']})
    data.update({'beta' : jsonY['beta']})
    data.update({'priceToSalesTrailing12Months' : jsonY['priceToSalesTrailing12Months']})
    data.update({'shortRatio' : jsonY['shortRatio']})
    data.update({'averageVolume' : jsonY['averageVolume']})
    data.update({'shortPercentOfFloat' : jsonY['shortPercentOfFloat']})
    data.update({'fiftyTwoWeekLow' : jsonY['fiftyTwoWeekLow']})
    data.update({'forwardPE' : jsonY['forwardPE']})
    data.update({'profitMargins' : jsonY['profitMargins']})
    data.update({'heldPercentInstitutions' : jsonY['heldPercentInstitutions']})
    data.update({'forwardEps' : jsonY['forwardEps']})
    data.update({'twoHundredDayAverage' : jsonY['twoHundredDayAverage']})
    collection.update({"ticker" : "test5"}, {'$push': {'metadata': data}})

app.run(host='0.0.0.0')
