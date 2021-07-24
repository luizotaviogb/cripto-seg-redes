import os
import sys
import time
import subprocess

class Main:
    print('Inicializando...')
    time.sleep(2)
    print('Seja bem-vindo ao inicializador de cripto-redes, existem duas formas de executar esse programa:')
    opcao = input ('1 - Modo Terminal \n2 - Modo Gráfico \n3 - Sair\n')
    print('OK, aguarde um momento enquanto preparamos a aplicação...')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcao == '1':
        subprocess.run(["python3", "criptographyDesktop.py"])
    elif opcao == '2':
        subprocess.run(["python3", "criptographyWeb.py"])
    elif opcao == '0':
        sys.exit()

        subprocess.run(["ls", "-l"])