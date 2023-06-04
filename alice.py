# alice.py
import socket
from Alicefunctions import Alice, generate_random_prime_with_n_bits
from hand_shake import hand_shake_sever_bob
from connections import *

alice_Union_socket = Init_Alice_connection()
bob_socket = Init_Bob_connection()

while True:
    if hand_shake_sever_bob(bob_socket):
        Alicebit = alice_Union_socket.recv(1024).decode()
        print("Alice bit -- ", Alicebit)
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
        alice_Union_socket.send(str(result).encode())

bob_socket.close()
server_socket.close()
