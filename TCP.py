import socket
import threading

# TCP Server
def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8888))
    server_socket.listen(5)
    print("TCP Server is running...")

    clients = []

    while True:
        client_socket, addr = server_socket.accept()
        clients.append((client_socket, addr))

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# TCP Client
def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8888))

    while True:
        message = raw_input("Enter a message: ") 
        client_socket.send(message.encode())

# Handle individual clients in separate threads
def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received:", data.decode())

if __name__ == "__main__":
    server_thread = threading.Thread(target=tcp_server)
    server_thread.start()

    client_thread = threading.Thread(target=tcp_client)
    client_thread.start()
