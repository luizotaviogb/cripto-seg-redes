import sys


class Cryptography:

    def encrypt(self,arquivo):
        ref_arquivo = open(arquivo, "r")
        arquivo2 = open("arquivoSaida.txt", "w+")
        for line in ref_arquivo:

            for i in list(line):
                i=i.lower()
                if i == "l":
                    arquivo2.write("J")
                elif i == "b":
                    arquivo2.write("O")
                elif i == "r":
                    arquivo2.write("H")
                elif i == "e":
                    arquivo2.write("A")
                elif i == "y":
                    arquivo2.write("N")
                elif i == "j":
                    arquivo2.write("L")
                elif i == "o":
                    arquivo2.write("B")
                elif i == "h":
                    arquivo2.write("R")
                elif i == "a":
                    arquivo2.write("E")
                elif i == "n":
                    arquivo2.write("Y")
                else:
                    arquivo2.write(i.upper())

    def decrypt(self,arquivo):
        ref_arquivo = open(arquivo, "r")
        arquivo2 = open("arquivoOriginal.txt", "w+")
        for line in ref_arquivo:

            for i in list(line):
                i=i.lower()
                if i == "l":
                    arquivo2.write("J")
                elif i == "b":
                    arquivo2.write("O")
                elif i == "r":
                    arquivo2.write("H")
                elif i == "e":
                    arquivo2.write("A")
                elif i == "y":
                    arquivo2.write("N")
                elif i == "j":
                    arquivo2.write("L")
                elif i == "o":
                    arquivo2.write("B")
                elif i == "h":
                    arquivo2.write("R")
                elif i == "a":
                    arquivo2.write("E")
                elif i == "n":
                    arquivo2.write("Y")
                else:
                    arquivo2.write(i.upper())


class Main:
    string_arquivo = "arquivoEntrada.txt"
    cripto= Cryptography()
    cripto.encrypt(string_arquivo)
    string_arquivo2="arquivoSaida.txt"
    cripto.decrypt(string_arquivo2)




