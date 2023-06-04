# bob.py
import socket
from Bobfunctions import Bob
from hand_shake import hand_shake_client_bob

    
        
alice_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "localhost"  # Replace with the server's IP address
server_port = 1234  # Replace with the server's port number
alice_server_socket.connect((server_host, server_port))
for i in range(1000):
    if hand_shake_client_bob(alice_server_socket):
        Bobbit = 0
        bob = Bob(Bobbit)
        response = alice_server_socket.recv(1024).decode()
        cA_q_g_gk = response.split(",")
        cA = (int(cA_q_g_gk[0][1:]), int(cA_q_g_gk[1][:-1]))
        q = int(cA_q_g_gk[2])
        g = int(cA_q_g_gk[3])
        gk = int(cA_q_g_gk[4])
        bob.cB = bob.calc_encrypted_bit(cA, q, g, gk)
        alice_server_socket.send(str(bob.cB).encode())
        result = alice_server_socket.recv(1024).decode()
        print(result)

alice_server_socket.close()
