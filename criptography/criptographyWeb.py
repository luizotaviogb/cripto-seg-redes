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
    text = request.data['text']
    cripto = criptography.Cryptography()
    retorno = cripto.encrypt(text)
    return jsonify(retorno)

@app.route('/decrypt/', methods=['POST'])
def decrypt(self,request):
    key = request.data['key']
    text =  request.data['text']
    cripto = criptography.Cryptography()
    retorno = cripto.encrypt(text)
    return jsonify(retorno)

app.run(debug = True)
