import string
import random
import os
import criptography
import sys


class SendCryptography:
    
    def sendEncrypt(self,arquivo):
        print("Lendo arquivo...")
        ref_arquivo = open(arquivo, "r")
        
        cripto = criptography.Cryptography()
        text = ""

        for line in ref_arquivo:
            text = text + line

        print("Encriptando conteudo do arquivo...")
        retorno = cripto.encrypt(text)
        file2 = open("arquivoSaida.txt", "w+")
        file2.write(retorno[1])
        print("Conteúdo Criptografado, Chave:")
        for letter in retorno[0]:
            print(letter, end ='')

        print ("\n")

    def sendDecrypt(self,arquivo,key):
        print("Lendo arquivo...")
        ref_arquivo = open(arquivo, "r")
        arquivo2 = open("arquivoOriginal.txt", "w+")
        cripto = criptography.Cryptography()
        if len(list(key)) != 26:
            print("Chave de tamanho inválido.")
            return

        text = ""
        for line in ref_arquivo:
            text = text + line

        print("Decriptando conteudo do arquivo...")
        retorno = cripto.decrypt(text, key)
        arquivo2.write(retorno[1])
        return
    
class Main:

    opcao = 1
    while opcao != 0:

        opcao = input ('0- Sair \n 1- Criptografar \n 2-Decriptografar \n')
        string_arquivo = "arquivoEntrada.txt"
        cripto = SendCryptography()
        string_arquivo2 = "arquivoSaida.txt"

        if opcao == '1':
            print(cripto.sendEncrypt(string_arquivo))
        elif opcao == '2':
            key = input ('Informe a chave\n')
            cripto.sendDecrypt(string_arquivo2, key)
        elif opcao == '0':
            sys.exit()