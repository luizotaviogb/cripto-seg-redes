import sys
import string
import random
import os


class Cryptography:

    def encrypt(self,arquivo):
        ref_arquivo = open(arquivo, "r")
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
        for letter in key:
            print(letter, end ='')

        print ("\n")

    def decrypt(self,arquivo,key):
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
class Main:

    opcao = 1
    while opcao != 0:

        opcao = input ('0- Sair \n 1- Criptografar \n 2-Decriptografar \n')
        string_arquivo = "arquivoEntrada.txt"
        cripto = Cryptography()
        string_arquivo2 = "arquivoSaida.txt"

        if opcao == '1':
            print(cripto.encrypt(string_arquivo))
        elif opcao == '2':
            key = input ('Informe a chave\n')
            cripto.decrypt(string_arquivo2, key)
        elif opcao == '0':
            sys.exit()




