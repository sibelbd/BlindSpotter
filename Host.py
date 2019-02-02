import socket

HOST_RPI =  # '10.104.99.110'
HOST_SERVER=  # '10.104.127.47'
PORT_OUT= 65432
PORT_IN= 65431

""" Sample socket communication to receive data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST_SERVER,PORT_IN))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        data = data.decode()
        data = int(data)
"""