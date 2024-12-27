import socket
import threading

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received from client: {data}")
        message = input("Server: ")
        conn.send(message.encode())
    conn.close()

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65432))
    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f"Received from server: {data}")
    client_socket.close()

if __name__ == "__main__":
    server_thread = threading.Thread(target=server_program)
    client_thread = threading.Thread(target=client_program)
    server_thread.start()
    client_thread.start()
    server_thread.join()
    client_thread.join()