import criptography
import sys
import os.path
basedir = os.path.abspath('/')

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
        print("Conteúdo Criptografado com sucesso, Chave:")
        for letter in retorno[0]:
            print(letter, end ='')
        print("\nProcesso finalizado, basta abrir arquivoSaida.txt")

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
        print("\nProcesso finalizado, basta abrir arquivoOriginal.txt")
        return

    def init(self):
        opcao = 1
        while opcao != 0:

            opcao = input ('0- Sair \n1- Criptografar \n2-Decriptografar \n')
            
            if opcao == '1':
                string_caminho = input('Qual o caminho da pasta onde esta o arquivo??\n')
                string_arquivo = input('Qual o nome do arquivo?\n')
                string_arquivo = basedir + string_caminho + '/' + string_arquivo
                self.sendEncrypt(string_arquivo)
            elif opcao == '2':
                key = input ('Informe a chave\n')
                string_caminho = input('Qual o caminho da pasta onde esta o arquivo??\n')
                string_arquivo = input('Qual o nome do arquivo?\n')
                string_arquivo = basedir + string_caminho + '/' + string_arquivo
                self.sendDecrypt(string_arquivo, key)
            elif opcao == '0':
                sys.exit()
    
class Main:
    SendCryptography().init()