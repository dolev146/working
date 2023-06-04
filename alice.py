# alice.py
import socket
from Alicefunctions import Alice, generate_random_prime_with_n_bits

def hand_shake_sever_bob(server_socket):
    msg = server_socket.recv(1024).decode()
    if  msg == "Ready":
        server_socket.send(b"Acknowledged")
        msg = server_socket.recv(1024).decode()
        if msg == "Acknowledged":
            return True
    
    return False

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "0.0.0.0"  # listen on all available network interfaces
server_port = 1234  # choose a port number
server_socket.bind((server_host, server_port))
server_socket.listen()
print("Waiting for a connection...")
bob_socket, client_address = server_socket.accept()
print("Connected to:", client_address)
i = 0

while True:
    if hand_shake_sever_bob(bob_socket):
        Alicebit = 1
        q = generate_random_prime_with_n_bits(30)
        alice = Alice(Alicebit, q)
        i = i + 1
        print(i)
        cA_q_g_gk = (
            str(alice.cA)
            + ","
            + str(alice.q)
            + ","
            + str(alice.g)
            + ","
            + str(alice.gk)
        )
        bob_socket.send(cA_q_g_gk.encode())
        cB = bob_socket.recv(1024).decode()
        cB_tuple = tuple(map(int, cB.strip("()").split(",")))
        decrypted_result = alice.decrypt_message(cB_tuple)
        result = 0
        if decrypted_result == 1:
            result = 0
        else:
            result = 1
        print(result)
        bob_socket.send(str(result).encode())

bob_socket.close()
server_socket.close()
