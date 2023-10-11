import socket
import threading

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 8889))
    print("UDP Server is running...")

    clients = {}  

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()

        
        if addr not in clients:
            clients[addr] = server_socket
            print("\nNew client connected: {}".format(addr))

        for client_addr, client_socket in clients.items():
            if client_addr != addr:
                client_socket.sendto(data, client_addr)

        print("Received from {}: {}".format(addr, message))
        print("Message Input:")

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = raw_input("Message Input: ")  
        client_socket.sendto(message.encode(), ("127.0.0.1", 8889))
        print("Sent: {}".format(message))

if __name__ == "__main__":
    server_thread = threading.Thread(target=udp_server)
    server_thread.start()

    client_thread = threading.Thread(target=udp_client)
    client_thread.start()
