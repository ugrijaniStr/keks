import os

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class cryptography():
    def decrypto_message(*arguments) -> int:
        for number in arguments:
            print(characters[number], end = '')

    def crypto_message(x) -> str:
        pos = -1
        length = len(x)
        keks = ''

        for i in range(length):
            if(x[i] in characters):
                for j in range(len(characters)):
                    if(characters[j] == x[i]):
                        pos = j
                        break

                if(pos != -1):
                    keks += (f'{pos},')

        print(keks[:-1])


if(__name__ == '__main__'):
    os.system("cls")
    #start
