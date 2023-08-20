import os
import sys
import iniconfig
from flask import Flask, render_template, url_for, request, jsonify, flash
from flask_bootstrap import Bootstrap
import uuid
import json
import datetime as dt
import boto3
import db

ROUTE_PATH = sys.path[1] if 2 == len(sys.path) else '.'
TEMPLATES_PATH = ROUTE_PATH + '/templates'

dpath = os.path.dirname(sys.argv[0])
ini = iniconfig.IniConfig(dpath + '/config.ini')

app = Flask(__name__, template_folder=TEMPLATES_PATH)

s3 = boto3.client('s3', region_name='ap-northeast-1')


@app.route('/', methods=['GET'])
def index():
    datas = db.get()
    try:
        with open(ini['DEFAULT']['FsPath'] + '/' + str(uuid.uuid1()), 'w') as f:
            f.write(json.dumps(datas))
    except:
        pass
    return render_template('index.html', datas=datas)


@app.route('/add', methods=['POST'])
def post():
    _text = request.json['text']
    try:
        _logData = {"text": _text, "timestamp": str(dt.datetime.now())}
        s3.put_object(Body=json.dumps(_logData), Bucket=ini['DEFAULT']['S3Bucket'], Key=str(uuid.uuid1()))
    except:
        pass
    db.post(_text)
    return jsonify({"message": "ok"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

