import os
import socket
import threading
from colorama import Fore

class Info():
    red = Fore.LIGHTRED_EX
    green = Fore.LIGHTGREEN_EX
    black = Fore.LIGHTBLACK_EX
    yellow = Fore.LIGHTYELLOW_EX
    white = Fore.LIGHTWHITE_EX
    BOLD = '\033[1m'
    END = '\033[0m'

    disconnect = f'{black}[{red}{BOLD}DISCONNECT{END}{black}]{white}'
    connect = f'{black}[{green}{BOLD}CONNECTED{END}{black}]{white}'
    message = f'{black}[{green}+{black}]{white}'
    start = f'{black}[{yellow}{BOLD}STARTED{END}{black}]{white}'


class Main(object):
    def handle_client(client_socket, client_address):
        print(f"{Info.connect} {client_address} has connected to the server.")
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                client_socket.send(message.encode('utf-8'))
                print(f"{Info.message} {client_address}: {message}")
            except ConnectionResetError:
                break

        print(f"{Info.disconnect} {client_address} has disconnected from server.")
        client_socket.close()

    def main(host, port):
        os.system("cls")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host,port))
            s.listen(2)

            print(f"""{Info.white}

                ░█─▄▀ ░█▀▀▀ ░█─▄▀ ░█▀▀▀█ 　 ── 　 ░█▀▀▀█ ░█▀▀▀ ░█▀▀█ ░█──░█ ░█▀▀▀ ░█▀▀█ 
                ░█▀▄─ ░█▀▀▀ ░█▀▄─ ─▀▀▀▄▄ 　 ▀▀ 　 ─▀▀▀▄▄ ░█▀▀▀ ░█▄▄▀ ─░█░█─ ░█▀▀▀ ░█▄▄▀ 
                ░█─░█ ░█▄▄▄ ░█─░█ ░█▄▄▄█ 　 ── 　 ░█▄▄▄█ ░█▄▄▄ ░█─░█ ──▀▄▀─ ░█▄▄▄ ░█─░█
                  

            """)
            print(f"{Info.start} Server has started on: {Info.BOLD}{host}:{port}{Info.END}")

            while True:
                client_socket, client_address = s.accept()
                client_handler = threading.Thread(target=Main.handle_client, args=(client_socket, client_address))
                client_handler.start()

if __name__ == "__main__":
    Main.main('127.0.0.1',6070)
