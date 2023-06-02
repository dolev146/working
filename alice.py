# alice.py
import socket
from Alicefunctions import (Alice,generate_random_prime_with_n_bits )

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Choose a port and bind the socket to it
server_host = '0.0.0.0'  # listen on all available network interfaces
server_port = 1234  # choose a port number
server_socket.bind((server_host, server_port))

# Listen for incoming connections
server_socket.listen(1)
print('Waiting for a connection...')

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print('Connected to:', client_address)


received_number=1



for i in range(1000):
    
    # Receive the "Ready" signal from Computer 2
    response = client_socket.recv(1024).decode()
    if response == 'Ready':
        Alicebit = 0
        q = generate_random_prime_with_n_bits(30)
        alice = Alice(Alicebit, q)
        i=i+1
        # Send Alice cA, q, g, gk to Bob string format (cA,q,g,gk) in one send command together
        cA_q_g_gk = str(alice.cA) + ',' + str(alice.q) + ',' + str(alice.g) + ',' + str(alice.gk)
        client_socket.send(b'Acknowledged')

        # Receive the acknowledgment from Computer 2
        response = client_socket.recv(1024).decode()
        if response == 'Acknowledged':
            client_socket.send(cA_q_g_gk.encode())
            # print('iteration: ' , i)
            # Receive Bob cB
            cB = client_socket.recv(1024).decode()
            # print('cB: ' , cB)
            cB_tuple = tuple(map(int, cB.strip("()").split(",")))
            # print(cB_tuple)  # Output: (3, 5)
            decrypted_result = alice.decrypt_message(cB_tuple)
            result = 0
            if decrypted_result == 1:
                result = 0
            else:
                result = 1
            print(result)
            # send result to Bob
            client_socket.send(str(result).encode())

  

# Close the sockets
client_socket.close()
server_socket.close()
