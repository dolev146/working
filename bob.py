# bob.py
import socket
from Bobfunctions import Bob
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "localhost"  # Replace with the server's IP address
server_port = 1234  # Replace with the server's port number
client_socket.connect((server_host, server_port))
for i in range(1000):
    client_socket.send(b"Ready")
    response = client_socket.recv(1024).decode()
    if response == "Acknowledged":
        client_socket.send(b"Acknowledged")
        Bobbit = 0
        bob = Bob(Bobbit)
        response = client_socket.recv(1024).decode()
        cA_q_g_gk = response.split(",")
        cA = (int(cA_q_g_gk[0][1:]), int(cA_q_g_gk[1][:-1]))
        q = int(cA_q_g_gk[2])
        g = int(cA_q_g_gk[3])
        gk = int(cA_q_g_gk[4])
        bob.cB = bob.calc_encrypted_bit(cA, q, g, gk)
        client_socket.send(str(bob.cB).encode())
        result = client_socket.recv(1024).decode()
        print(result)

client_socket.close()
