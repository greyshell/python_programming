import socket

if __name__ == '__main__':
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    #
    server_address = ('localhost', 1000)
    client_socket.connect(server_address)
    print(f"Connected to {server_address}")

    # Send data to the server
    message = "xyz"
    client_socket.sendall(message.encode())
    print(f"Sent data: {message}")

    # Receive the echoed data from the server
    data = client_socket.recv(1024)
    print(f"Received echoed data: {data.decode()}")

    # Close the connection
    client_socket.close()
