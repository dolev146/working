# alice.py
from unionA import union, orFunc
import socket
from Alicefunctions import Alice, generate_random_prime_with_n_bits

Alice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Alice_host = "0.0.0.0"  # listen on all available network interfaces
Alice_port = 1235  # choose a port number
Alice_socket.bind((Alice_host, Alice_port))
Alice_socket.listen()
print("Waiting for unionA connection...")
unionA_socket, unionA_address = Alice_socket.accept()
print("union Connected to:", unionA_address)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "0.0.0.0"  # listen on all available network interfaces
server_port = 1234  # choose a port number
server_socket.bind((server_host, server_port))
server_socket.listen()
print("Waiting for bob connection...")
# client_socket is the connection to bob.py
client_socket, client_address = server_socket.accept()
print("bob Connected to:", client_address)

while True:
    # send "Ready" to unionA_socket
    unionA_socket.send(b"Ready")
    Alicebit = unionA_socket.recv(1024).decode()
    Alicebit = int(Alicebit)
    print(Alicebit)
    client_socket.send(b"Ready")
    response = client_socket.recv(1024).decode()
    if response == "Ready":
        q = generate_random_prime_with_n_bits(30)
        alice = Alice(Alicebit, q)
        cA_q_g_gk = (
            str(alice.cA)
            + ","
            + str(alice.q)
            + ","
            + str(alice.g)
            + ","
            + str(alice.gk)
        )
        client_socket.send(b"Acknowledged")
        response = client_socket.recv(1024).decode()
        if response == "Acknowledged":
            client_socket.send(cA_q_g_gk.encode())
            cB = client_socket.recv(1024).decode()
            cB_tuple = tuple(map(int, cB.strip("()").split(",")))
            decrypted_result = alice.decrypt_message(cB_tuple)
            result = 0
            if decrypted_result == 1:
                result = 0
            else:
                result = 1
            print(result)
            client_socket.send(str(result).encode())
            unionA_socket.send(str(result).encode())

client_socket.close()
server_socket.close()
