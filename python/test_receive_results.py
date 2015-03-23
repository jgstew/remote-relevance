
import sys
sys.dont_write_bytecode = True

from flask import Flask
import requests
import json
# http://stackoverflow.com/questions/1761744/python-read-password-from-stdin
import getpass

# config file where BES_ROOT_SERVER_DNS and similar are set
from BES_CONFIG import *

BES_PASSWORD = getpass.getpass()

app = Flask(__name__)

# http://stackoverflow.com/questions/19995/is-there-some-way-to-push-data-from-web-server-to-browser
# https://flask-socketio.readthedocs.org/en/latest/
# http://software.bigfix.com/download/bes/misc/BESImport-ExportReference71_080906.pdf


# https://en.wikipedia.org/wiki/Base64
# http://stackoverflow.com/questions/3470546/python-base64-data-decode
#  concatenations "~" of (base64 encode it) of unique values of (it as string) of (names of regapps)
@app.route('/remote/results/<path:bes_result>')
def rest_bes_query_result(bes_result):
    result = ""
    for string in bes_result.split("~"):
        result = result + "<br/>" + string.decode('base64')
    print result
    #return "thanks!"
    return "<b>result:</b> " + bes_result + " <br/><b>base64decode:</b> " + result


#http://isbullsh.it/2012/06/Rest-api-in-python/
@app.route('/remote/query/<path:bes_query>')
def rest_bes_query(bes_query):
    print "https://" + BES_ROOT_SERVER_DNS + ":" + BES_ROOT_SERVER_PORT + "/api/"
    return bes_query + " "

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080)
    print "doing nothing, just testing"
else:
    app.run(host='0.0.0.0', port=80)
