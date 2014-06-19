#encoding=utf8
from flask import *
import flask
import route
import re
from werkzeug.contrib.cache import SimpleCache
import time
app = Flask(__name__)
cache = SimpleCache()
# app.config['SEND_FILE_MAX_AGE_DEFAULT']=-1

import log

logger = log.getloger()

@app.route('/api/score/<int:id>')
def getScore(id):
    return route.getScore(id)
    try:
        pass
    except Exception,e:
        logger.error('%s %s'%(id,e) )
        raise e
        return "{'error':true}"

@app.route('/api/status')
def getStatus():
    return route.getStatus()

@app.route('/')
def index():
    # import ipdb;ipdb.set_trace()    
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True,use_debugger=True,host='0.0.0.0',port=3000)
    # app.run(debug=False,use_debugger=False,host='0.0.0.0',port=8100)

    

