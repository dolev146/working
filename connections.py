import socket

def Init_Alice_connection():
    Alice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Alice_host = "0.0.0.0"  # listen on all available network interfaces
    Alice_port = 1235  # choose a port number
    Alice_socket.bind((Alice_host, Alice_port))
    Alice_socket.listen()
    print("Waiting for unionA connection...")
    unionA_socket, unionA_address = Alice_socket.accept()
    print("union Connected to:", unionA_address)
    return unionA_socket

def Init_Bob_connection():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = "0.0.0.0"  # listen on all available network interfaces
    server_port = 1234  # choose a port number
    server_socket.bind((server_host, server_port))
    server_socket.listen()
    print("Waiting for a connection...")
    bob_socket, client_address = server_socket.accept()
    print("Connected to:", client_address)
    return bob_socket