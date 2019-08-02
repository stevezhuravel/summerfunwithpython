#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
import urllib.request
import json

## Define APOD
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey ='api_key=DEMO_KEY'

##Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

##read the file-like object
apodread = apodurlobj.read()

##decide json to python data strutcure
decodeapod = json.loads(apodread.decode('utf-8'))


