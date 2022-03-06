from datetime import datetime
import socket


def main():
    # define an address
    server_address = ('localhost', 6789)  # tuple(address, port)
    max_size = 4096

    print(f'Starting the server at {datetime.now()}.')
    print('Waiting for a client to call.')

    # to establish a connection, server uses two socket methods, that was imported from socket
    # 'socket.socket' creates a socket
    # 'bind' binds to it (listening any data that comes to that IP address)
    # AF_INET parameter means that we create an internet-socket(IP)
    # SOCK_DGRAM means that we will use send and get datagrams (use UDP protocol)
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(server_address)

    # when the server get a datagram, it wakes up and get the data and info about a client
    # the client variable consists of a combination of the address and port, that needs to get the access to the client
    data, client = server.recvfrom(max_size)

    # the server sends the response, and closes the connection
    print(f'At {datetime.now()},{client} said {data}')
    server.sendto(b'Are you talking to me?', client)
    server.close()


if __name__ == '__main__':
    main()
