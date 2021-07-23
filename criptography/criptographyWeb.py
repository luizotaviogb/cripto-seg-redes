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
    retorno = cripto.encrypt(text)
    chave = ""
    for i in retorno[0]:
        chave = chave + i

    return jsonify((chave, retorno[1]))

@app.route('/decrypt/', methods=['POST'])
def decrypt():
    key = request.json['key']
    text = request.json['text']
    cripto = criptography.Cryptography()
    retorno = cripto.decrypt(text, list(key))
    return jsonify(retorno[1])


app.run(debug = True)
