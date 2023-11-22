import socket

if __name__ == '__main__':
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections (maximum 5 connections in the queue)
    server_socket.listen(5)
    print(f"Server is listening on {server_address}")

    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Receive and send back the data
        data = client_socket.recv(1024)
        print(f"Received data: {data.decode()}")

        # Echo the data back to the client
        client_socket.sendall(data)

        # Close the connection
        client_socket.close()
