from datetime import datetime
import socket


def main():
    address = ('localhost', 6789)
    max_size = 1000

    print(f'Starting the client at {datetime.now()}')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the stream
    client.connect(address)
    client.sendall(b'Hey')
    data = client.recv(max_size)

    print(f'At {datetime.now()}, someone replied {data}')
    client.close()


if __name__ == '__main__':
    main()
