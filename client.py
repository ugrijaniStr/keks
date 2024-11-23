import os
import socket
from colorama import Fore

characters = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class Info():
    red = Fore.LIGHTRED_EX
    green = Fore.LIGHTGREEN_EX
    black = Fore.LIGHTBLACK_EX
    yellow = Fore.LIGHTYELLOW_EX
    white = Fore.LIGHTWHITE_EX
    BOLD = '\033[1m'
    END = '\033[0m'

    sent = f'{black}[{green}sent{black}]{white}'
    message = f'{black}[{green}{BOLD}TYPE{END}{black}]{white}'

class Main(object):
    def main():
        os.system("cls")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            host = '127.0.0.1'
            port = 6070
            s.connect((host,port))

            try:
                while True:
                    message = input(f"{Info.message}: ")
                    pos = -1
                    length = len(message)
                    keks = ''

                    for i in range(length):
                        if(message[i] in characters):
                            for j in range(len(characters)):
                                if(characters[j] == message[i]):
                                    pos = j
                                    break

                            if(pos != -1):
                                keks += (f'{pos},')

                    keks[:-1]

                    if message.lower() == 'exit':
                        break
                    s.send(keks[:-1].encode('utf-8'))

                    response = s.recv(1024).decode('utf-8')
                    print(f'{Info.sent}{response}')
            finally:
                s.close()

if __name__ == "__main__":
    Main.main()
