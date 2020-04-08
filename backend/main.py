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
    db.order.find({"OrderDateTime":{ $gte:ISODate("2019-02-10"), $lt:ISODate("2019-02-21") }}).pretty();

    return ("added metadata now")


# appends tweets to company tweets
@app.route("/<string:company>/tweets", methods=['PUT'])
def addTweet(company):
    new_tweet = request.get_json()
    collection.update({"ticker" : company}, {'$push': {'tweets': new_tweet}})

# adds historicaldata to ticker
@app.route("/<string:company>/historicaldata", methods=['PUT'])
def addhist():
    new_hist = request.get_json()
    collection.update({"ticker" : company}, {'$push': {'historical_data': new_hist}})

# adds new company with it's current metadata
@app.route("/company", methods=['POST'])
def addcompany():
    companyObj = request.get_json()
    collection.insert_one(companyObj)
    addMetadata("company")

def addmetadata(company): # needs update like addFundamentals
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
    collection.update({"ticker" : "test5"}, {'$set': {'metadata': data}}) #for now test5 but change later

# route to add Fundamentals with current timestamp in NY
@app.route("/<string:company>/Fundamentals", methods=['PUT'])
def addFundamentals(company):
    comp = yf.Ticker(company)
    jsonY = comp.info
    td = datetime.now()
    td = td - timedelta(hours=5)
    data = {'date' : td}
    data = (tryObj('sharesShort', jsonY, data))
    data = (tryObj('trailingPE', jsonY, data))
    data = (tryObj('trailingEps', jsonY, data))
    data = (tryObj('enterpriseToRevenue', jsonY, data))
    data = (tryObj('fiftyDayAverage', jsonY, data))
    data = (tryObj('averageDailyVolume10Day', jsonY, data))
    data = (tryObj('bookValue', jsonY, data))
    data = (tryObj('volume', jsonY, data))
    data = (tryObj('SandP52WeekChange', jsonY, data))
    data = (tryObj('fiftyTwoWeekHigh', jsonY, data))
    data = (tryObj('netIncomeToCommon', jsonY, data))
    data = (tryObj('averageVolume10days', jsonY, data))
    data = (tryObj('regularMarketVolume', jsonY, data))
    data = (tryObj('earningsQuarterlyGrowth', jsonY, data))
    data = (tryObj('52WeekChange', jsonY, data))
    data = (tryObj('sharesShortPriorMonth', jsonY, data))
    data = (tryObj('heldPercentInsiders', jsonY, data))
    data = (tryObj('marketCap', jsonY, data))
    data = (tryObj('beta', jsonY, data))
    data = (tryObj('priceToSalesTrailing12Months', jsonY, data))
    data = (tryObj('shortRatio', jsonY, data))
    data = (tryObj('averageVolume', jsonY, data))
    data = (tryObj('shortPercentOfFloat', jsonY, data))
    data = (tryObj('fiftyTwoWeekLow', jsonY, data))
    data = (tryObj('forwardPE', jsonY, data))
    data = (tryObj('profitMargins', jsonY, data))
    data = (tryObj('heldPercentInstitutions', jsonY, data))
    data = (tryObj('forwardEps', jsonY, data))
    data = (tryObj('twoHundredDayAverage', jsonY, data))
    collection.update({"ticker" : company}, {'$push': {'Fundamentals': data}})
    return "Fundamentals added for date: " + str(td)

# def for trying to add object in Fundamentals, as some don't exist in other tickers
def tryObj(name , jsonY, data):
    try:
        data.update({name : jsonY[name]})
        return data
    except:
        return data

@app.route("/testt", methods=['PUT'])
def testt():
    td = datetime.now()
    for i in range(31):
        data = {'date' : td - timedelta(hours=(i*24 + 5))}
        data.update({'test1' : 'obj' + str(i)})
        data.update({'test2' : 'obj' + str(i)})
        collection.update({"ticker" : 'test5'}, {'$push': {'testt': data}})






app.run(host='0.0.0.0')
