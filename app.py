from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route("/",methods = ["GET", "POST"