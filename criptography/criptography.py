import sys
import string
import random
import os
from flask import Flask, request, make_response, Response, send_file, jsonify, json
from werkzeug.utils import secure_filename
app = Flask (__name__)
app.config['UPLOAD_FOLDER'] = "~/Área de trabalho/cripto-trabalho"
app.config['MAX_CONTENT_PATH'] = "9090000"
# class Cryptography:

@app.route('/encrypt/', methods=['POST'])
def encrypt():
    arquivo = request.files['file']
    arquivo.save(arquivo.filename)
    ref_arquivo = open(arquivo.filename, "r")
    arquivo2 = open("arquivoSaida.txt", "w+")

    tam = 26
    key = random.sample(string.ascii_uppercase, tam)
    key2=[]
    key1=[]
    for i in range(13,26):
        key2.append(key[i])
    for i in range(0,13):
        key1.append(key[i])

    for line in ref_arquivo:

        for i in list(line):
            i = i.upper()
            j=0
            contador = 0
            x = 0
            while contador != 1:
                if i == key2[j]:
                    arquivo2.write(key1[j])
                    contador = 1
                elif i == key1[j]:
                    arquivo2.write(key2[j])
                    contador = 1
                elif j == 12:
                    arquivo2.write(i.upper())
                    contador=1
                j = j+1
    print("\n" * 130)
    chave = "".join(key)
    for letter in key:
        print(letter, end ='')

    print("\n")
    #return send_file(path_or_file="arquivoSaida.txt")
    return send_file(path_or_file="arquivoSaida.txt"), chave


@app.route('/decrypt/', methods=['POST'])
def decrypt(self,request):
    key = request.data['key']
    arquivo = request.files['file']
    ref_arquivo = open(arquivo, "r")
    arquivo2 = open("arquivoOriginal.txt", "w+")

    tam = 26
    key2 = []
    key1 = []
    for i in range(13, 26):
        key2.append(key[i])
    for i in range(0, 13):
        key1.append(key[i])

    for line in ref_arquivo:

        for i in list(line):
            i = i.upper()
            j = 0
            contador = 0
            x = 0
            while contador != 1:
                if i == key2[j]:
                    arquivo2.write(key1[j])
                    contador = 1
                elif i == key1[j]:
                    arquivo2.write(key2[j])
                    contador = 1
                elif j == 12:
                    arquivo2.write(i.upper())
                    contador = 1
                j = j + 1
    print("\n" * 130)

    return arquivo2

app.run(debug = True)

# class Main:

    # opcao = 1
    # while opcao != 0:
    #
    #     opcao = input ('0- Sair \n 1- Criptografar \n 2-Decriptografar \n')
    #     string_arquivo = "arquivoEntrada.txt"
    #     cripto = Cryptography()
    #     string_arquivo2 = "arquivoSaida.txt"
    #
    #     if opcao == '1':
    #         print(cripto.encrypt(string_arquivo))
    #     elif opcao == '2':
    #         key = input ('Informe a chave\n')
    #         cripto.decrypt(string_arquivo2, key)
    #     elif opcao == '0':
    #         sys.exit()