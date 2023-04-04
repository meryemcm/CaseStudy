import socket

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()

    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print('HOST IP:', host_ip)
    print('HOST Name:', host_name)
    port = 1025
    socket_address = (host_ip, port)
    server.bind(socket_address)
    server.listen()
    print("Listening at", socket_address)
    conn, address = server.accept()  
    print("Connection from: " + str(address))
    while True:
       
        data = conn.recv(1024).decode()
        if not data:
           
            break
        print("from connected user: " + str(data))
        data = str(data).upper()
        conn.send(data.encode()) 

    conn.close() 




if __name__ == '__main__':
    server()