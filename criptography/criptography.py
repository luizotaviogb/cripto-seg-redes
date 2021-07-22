import string
import random
import os

class Cryptography:
    def encrypt(self,text): 
        return self.alg(text, None)

    def decrypt(self,text,key):
        return self.alg(text, key)[1]

    def alg(self, text, key):
        tam = 26
        result = ""
        key2=[]
        key1=[]
        if key is None:
            key = random.sample(string.ascii_uppercase, tam)

        for i in range(13, 26):
            key2.append(key[i])
        for i in range(0, 13):
            key1.append(key[i])

        for i in list(text):
            i = i.upper()
            j=0
            contador = 0
            x = 0
            while contador != 1:
                if i == key2[j]:
                    result = result + key1[j]
                    contador = 1
                elif i == key1[j]:
                    result = result + key2[j]
                    contador = 1
                elif j == 12:
                    result = result + i.upper()
                    contador=1
                j = j+1
        retorno = (key, result)
        return retorno