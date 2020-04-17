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

@app.route('/test')
def test():
    return ("all added")

# adds historicaldata to ticker and retrieves all historical data from db
@app.route("/<string:company>/historicaldata", methods=['PUT' , 'GET'])
def addhist(company):
    if request.method == 'PUT': ## NEDS UPDATING
        new_hist = request.get_json()
        collection.update({"ticker" : company}, {'$push': {'historical': new_hist}})
        return ("Historical data added to: " + company)
    if request.method == 'GET':
        obj = collection.find_one({"ticker": company})
        return obj['historical']


# adds new company with it's current metadata
@app.route("/company", methods=['POST'])
def addcompany():
    companyObj = request.get_json()
    collection.insert_one(companyObj)
    addMetadata(companyObj['ticker'])
    addhist2year(companyObj['ticker'])

# Adds the metadata to database base on ticker
def addMetadata(company):
    comp = yf.Ticker(company)
    jsonY = comp.info
    data = {}
    data = tryObj('shortName', jsonY, data)
    data = tryObj('logo_url', jsonY, data)
    data = tryObj('website', jsonY, data)
    data = tryObj('symbol', jsonY, data)
    data = tryObj('city', jsonY, data)
    data = tryObj('phone', jsonY, data)
    data = tryObj('industry', jsonY, data)
    data = tryObj('country', jsonY, data)
    data = tryObj('state', jsonY, data)
    data = tryObj('currency', jsonY, data)
    data = tryObj('longBusinessSummary', jsonY, data)
    data = tryObj('zip', jsonY, data)
    data = tryObj('sector', jsonY, data)
    data = tryObj('fullTimeEmployees', jsonY, data)
    data = tryObj('address1', jsonY, data)
    data = tryObj('longName', jsonY, data)
    collection.update({"ticker" : company}, {'$set': {'metadata': data}}) #for now test5 but change later

# route to add Fundamentals with current timestamp in NY
@app.route("/<string:company>/Fundamentals", methods=['PUT'])
def addFundamentals(company):
    comp = yf.Ticker(company)
    jsonY = comp.info
    td = datetime.now()
    td = td - timedelta(hours=5)
    data = {'date' : td}
    data = tryObj('sharesShort', jsonY, data)
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
    return "Fundamentals added to: " +  comapny +  " for date: " + str(td)

# def for trying to add object in Fundamentals, as some don't exist in other tickers
def tryObj(name , jsonY, data):
    try:
        data.update({name : jsonY[name]})
        return data
    except:
        return data

def getOne(ticker, ):
    startdate = datetime(2020,4,4)
    enddate = datetime(2020,4,5)
    obj = collection.find_one({"ticker": "test5"})
    for i in obj['testt']:
        if i['date'] > startdate and i['date'] < enddate:
            return i

def getlist(ticker, ): # DAY TO today
    startdate = datetime(2020,4,4)
    enddate = datetime(2020,4,5)
    obj = collection.find_one({"ticker": "test5"})
    for i in obj['testt']:
        if i['date'] > startdate and i['date'] < enddate:
            return i

def addhist2year(company):
  comp = yf.Ticker(company)
  hist = comp.history(period="24mo")
  hist2 = hist.to_dict('index')
  for i in hist2:
    tmp = {'date' : i}
    tmp.update(hist2[i])
    collection.update({"ticker" : company}, {'$push': {'historical': tmp}})
  return ("added")

app.run(host='0.0.0.0')
