import sys
import string
import random


class Cryptography:

    def encrypt(self,arquivo):
        ref_arquivo = open(arquivo, "r")
        arquivo2 = open("arquivoSaida.txt", "w+")

        tam = 26
        print (tam)
        key = random.sample(string.ascii_uppercase, tam)
        key2=[]
        key1=[]
        for i in range(13,25):
            key2.append(key[i])
        for i in range(0,12):
            key1.append(key[i])

        print(key1)
        print(key2)


        print(key)
        for line in ref_arquivo:

            for i in list(line):
                i = i.upper()

                if i == key1:
                    arquivo2.write(key2)
                elif i == key2:
                    arquivo2.write(key1)
                else:
                    arquivo2.write(i.upper())




                # if i == key[0]:
                #     arquivo2.write(key[1])
                # elif i == key[2]:
                #     arquivo2.write(key[3])
                # elif i == key[4]:
                #     arquivo2.write(key[5])
                # elif i == key[6]:
                #     arquivo2.write(key[7])
                # elif i == key[8]:
                #     arquivo2.write(key[9])
                # elif i == key[10]:
                #     arquivo2.write(key[11])
                # elif i == key[1]:
                #     arquivo2.write(key[0])
                # elif i == key[3]:
                #     arquivo2.write(key[2])
                # elif i == key[5]:
                #     arquivo2.write(key[4])
                # elif i == key[7]:
                #     arquivo2.write(key[6])
                # elif i == key[9]:
                #     arquivo2.write(key[8])
                # elif i == key[11]:
                #     arquivo2.write(key[10])
                # else:
                #     arquivo2.write(i.upper())

    def decrypt(self,arquivo,key):
        ref_arquivo = open(arquivo, "r")
        arquivo2 = open("arquivoOriginal.txt", "w+")
        for line in ref_arquivo:

            for i in list(line):
                i = i.upper()
                if i == key[0]:
                    arquivo2.write(key[1])
                elif i == key[2]:
                    arquivo2.write(key[3])
                elif i == key[4]:
                    arquivo2.write(key[5])
                elif i == key[6]:
                    arquivo2.write(key[7])
                elif i == key[8]:
                    arquivo2.write(key[9])
                elif i == key[10]:
                    arquivo2.write(key[11])
                elif i == key[1]:
                    arquivo2.write(key[0])
                elif i == key[3]:
                    arquivo2.write(key[2])
                elif i == key[5]:
                    arquivo2.write(key[4])
                elif i == key[7]:
                    arquivo2.write(key[6])
                elif i == key[9]:
                    arquivo2.write(key[8])
                elif i == key[11]:
                    arquivo2.write(key[10])
                else:
                    arquivo2.write(i.upper())


class Main:

    string_arquivo = "arquivoEntrada.txt"
    cripto= Cryptography()
    cripto.encrypt(string_arquivo)
    string_arquivo2="arquivoSaida.txt"
    #cripto.decrypt(string_arquivo2,"FRCMDGXSPOYI")




