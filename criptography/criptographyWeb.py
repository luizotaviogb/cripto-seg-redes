import sys
import string
import random
import os
import criptography
from flask import Flask, request, make_response, Response, send_file, jsonify, json
from werkzeug.utils import secure_filename

app = Flask (__name__)
app.config['UPLOAD_FOLDER'] = "~/Área de trabalho/cripto-trabalho"
app.config['MAX_CONTENT_PATH'] = "9090000"

@app.route('/encrypt/', methods=['POST'])
def encrypt():
    text = request.json['text']
    cripto = criptography.Cryptography()
    ret = cripto.encrypt(text)
    key = ""
    for i in ret[0]:
        key = key + i
    return jsonify(key=key, text=ret[1])

@app.route('/decrypt/', methods=['POST'])
def decrypt():
    key = request.json['key']
    text = request.json['text']
    cripto = criptography.Cryptography()
    ret = cripto.decrypt(text, list(key))
    return jsonify(text=ret[1])


app.run(debug = True)
