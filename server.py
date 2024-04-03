import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established from {client_address}")

        data = client_socket.recv(1024).decode()
        print(f"Received message: {data}")

        client_socket.close()

if __name__ == "__main__":
    target_ip = "<your_ip_here>" # Adjust IP here
    target_port = 9999

    start_server("0.0.0.0", target_port)
