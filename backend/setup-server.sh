#! /bin/bash
pip3 install -r requirements.txt
python3 -m venv venv
source venv/bin/activate
gunicorn main:app
