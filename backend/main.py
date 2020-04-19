from flask import Flask
from flask_cors import CORS
from alpha_vantage.timeseries import TimeSeries
from flask import request
from flask_pymongo import pymongo
from pymongo import MongoClient
import yfinance as yf
from datetime import tzinfo, timedelta, datetime
from alpha_vantage.timeseries import TimeSeries
import json
from flask_jsonpify import jsonpify


from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)

CONNECTION_STRING = "mongodb://deep-stock-cu:" + os.getenv('d_pass') + "@deep-stock-cluster-shard-00-00-bwk5a.gcp.mongodb.net:27017,deep-stock-cluster-shard-00-01-bwk5a.gcp.mongodb.net:27017,deep-stock-cluster-shard-00-02-bwk5a.gcp.mongodb.net:27017/test?ssl=true&replicaSet=deep-stock-cluster-shard-0&authSource=admin&retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('deep-stock')
collection = db['companies']

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/message')
def get_message():
  return 'Hello Stonks'

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

@app.route("/<string:company>/metadata", methods=['GET'])
def getMetadata(company):
    obj = collection.find_one({'ticker' : company})
    return obj['metadata']


@app.route("/<string:company>/prediction", methods=['GET']) # MAYBE CHANGE RETURN FROM LIST TO SOMETHING ELSE
def get_2weekhist(company):
    comp = yf.Ticker(company)
    hist = comp.history(period="14d")
    hist2 = hist.to_dict('index')
    pred = []
    for i in hist2:
      tmp = {'date' : i}
      tmp.update(hist2[i])
      pred.append(tmp)
    return pred

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
    return "Fundamentals added to: " +  company +  " for date: " + str(td)

# def for trying to add object in Fundamentals, as some don't exist in other tickers
def tryObj(name , jsonY, data):
    try:
        data.update({name : jsonY[name]})
        return data
    except:
        return data

def getOne(ticker, date):
    date2 = date - timedelta(hours=24)
    startdate = datetime.strptime(date,'%Y-%m-%d')
    enddate = datetime.strptime(date2 ,'%Y-%m-%d')
    obj = collection.find_one({"ticker": ticker})
    for i in obj['historical']:
        if i['date'] > startdate and i['date'] < enddate:
            return i

def getlist(ticker, days): # Make sure is days
    enddate = datetime.now()
    startdate = enddate - timedelta(hours=24*days)
    obj = collection.find_one({"ticker": ticker})
    hist = []
    for i in obj['historical']:
        if i['date'] > startdate and i['date'] < enddate:
            hist.append(i)
    return hist

def addhist2year(company):
  comp = yf.Ticker(company)
  hist = comp.history(period="24mo")
  hist2 = hist.to_dict('index')
  for i in hist2:
    tmp = {'date' : i}
    tmp.update(hist2[i])
    collection.update({"ticker" : company}, {'$push': {'historical': tmp}})
  return ("added")


'''
  Storing stock data api

  Gets json data from response body and stores it into database
'''

@app.route('/users/store_data', methods=['POST'])
def insert_document():
    req_data = request.get_json()

    collection.insert_one(req_data).inserted_id
    return ('', 204)


'''
  Diplaying stock data api

  Gets all the sotored data in the database and retruns a json file
'''


@app.route('/<string:company>/intraday', methods=['GET'])
def get_intraday(company):


    key = 'CYNCL6X4FUN4SE0K'

    ts = TimeSeries(key= key)

    intraday_data, data_info = ts.get_intraday(symbol=company, outputsize='compact', interval='5min')


    daily_data = {}
    days_list = []
    convert_daytime = 0
    day = 0

    # Convert string dates to datetime format and append to list
    for key, value in intraday_data.items():
        convert_daytime = datetime.datetime.strptime(key, "%Y-%m-%d %H:%M:%S")
        days_list.append(convert_daytime.day)


    # Get latest day
    latest_day = max(days_list)

    # Add filtered data to new dictionary
    for key, value in intraday_data.items():
        convert_daytime = datetime.datetime.strptime(key, "%Y-%m-%d %H:%M:%S")
        day = convert_daytime.day

        if day == latest_day:
            if key not in daily_data:
                daily_data[key] = []
            daily_data[key].append(value)

    return json.dumps(daily_data)


@app.route('/users/display_data')
def get_documents():

    documents = collection.find()

    response = []

    for doc in documents:
        doc['_id'] = str(doc['_id'])
        response.append(doc)

    return json.dumps(response)



if os.getenv('environment') == 'dev':
    app.run(host='0.0.0.0')
elif __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
