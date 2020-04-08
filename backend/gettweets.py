import json

f = open('companies.json',) 
data = json.load(f) 
for i in data['companies']: 
	# make call to tweepy api here and store in mongodb for each company
    print(i) 
  
f.close() 
