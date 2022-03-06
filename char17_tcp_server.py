from datetime import datetime
import socket


def main():
    address = ('localhost', 6789)
    max_size = 1000

    print(f'Starting the server at {datetime.now()}.')
    print('Waiting for a client to call.')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen(5)

    client, address = server.accept()
    data = client.recv(max_size)

    print(f'At {datetime.now()} {client} said {data}')
    client.sendall(b'Are you talking to me?')
    client.close()
    server.close()

    
if __name__ == '__main__':
    main()
