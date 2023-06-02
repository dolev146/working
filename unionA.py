# unionA.py
import math
import numpy as np
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "localhost"  # Replace with the server's IP address
server_port = 1235  # Replace with the server's port number
client_socket.connect((server_host, server_port))

def orFunc(AliceBit):
    AliceBit = int(AliceBit)
    print(AliceBit)
    # wait to recieve aknowledgement from alice
    response = client_socket.recv(1024).decode()
    if response == "Ready":
        #  send alice the bit
        client_socket.send(str(AliceBit).encode())
        response = client_socket.recv(1024).decode()
        # the response is the result of the union
        print(response)


def union(list, worldSize):
    P = ["0", "1"]  # live bits
    bitsList = []
    for i in range(len(list)):
        temp = format(list[i], f"0{int(math.log2(worldSize))}b")
        bitsList.append(temp)
    for i in range(int(math.log2(worldSize))):
        P_check = np.zeros(len(P))
        for p_index in range(len(P)):
            if P_check[p_index] == 1:
                continue
            for j in range(len(bitsList)):
                if bitsList[j].startswith(P[p_index]):
                    P_check[p_index] = 1
                    break
        for j in range(len(P_check) - 1, -1, -1):
            bit_check = orFunc(P_check[j])
            if bit_check == 0:
                P.pop(j)
        if i == math.log2(worldSize) - 1:  # last round, no new live p
            break
        tempP = []
        for p in P:
            tempP.append(p + "0")
            tempP.append(p + "1")
        P = tempP
    int_list = [int(binary, 2) for binary in P]
    client_socket.close()
    return int_list


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6]
    print(union(list, 16))
