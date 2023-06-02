# bob.py
import socket
from Bobfunctions import (Bob)
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify the server's IP address and port number
server_host = 'localhost'  # Replace with the server's IP address
server_port = 1234  # Replace with the server's port number

# Connect to the server
client_socket.connect((server_host, server_port))

is_ready = False

# Send a number to the server
for i in range(1000):
    # Send the "Ready" signal to Computer 1
    client_socket.send(b'Ready')
    # Receive the acknowledgment from Computer 1
    response = client_socket.recv(1024).decode()
    if response == 'Acknowledged':
        # Send an acknowledgment to Computer 1
        client_socket.send(b'Acknowledged')


        Bobbit = 0
        bob = Bob(Bobbit)
        response = client_socket.recv(1024).decode()
        # print('iteration: ' , i)
        # print(f"Response received: {response}")
        # cA=(number , number) , q=number , g=number , gk=number
        cA_q_g_gk = response.split(',')
        cA = (int(cA_q_g_gk[0][1:]), int(cA_q_g_gk[1][:-1]))
        q = int(cA_q_g_gk[2])
        g = int(cA_q_g_gk[3])
        gk = int(cA_q_g_gk[4])
        # print('cA: ' , cA , 'q: ' , q , 'g: ' , g , 'gk: ' , gk)  
        bob.cB = bob.calc_encrypted_bit(cA, q, g, gk)
        # print('cB: ', bob.cB)
        
        client_socket.send(str(bob.cB).encode())
        result = client_socket.recv(1024).decode()
        print("result : " , result)





# Close the socket
client_socket.close()
