from flask import Flask, render_template
#import notify2
#import requests
# import hw1
import json
import urllib.request

app = Flask(__name__)
@app.route("/")
def hello():


    ## Define APOD
    apodurl = 'https://api.nasa.gov/planetary/apod?'
    mykey = 'api_key=DEMO_KEY'

    ##Call the webservice
    apodurlobj = urllib.request.urlopen(apodurl + mykey)

    ##read the file-like object
    apodread = apodurlobj.read()

    ##decide json to python data strutcure
    decodeapod = json.loads(apodread.decode('utf-8'))

    ## creates a variable where the images is being stored
    image = decodeapod ['hdurl']
    ## returns the image
    return render_template("index.html", hello = image)

if __name__ == '__main__':
   app.run(debug = True)


