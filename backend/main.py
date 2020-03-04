from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/message')
def get_message():
    return 'Hello Stonks'

app.run(host='0.0.0.0')
