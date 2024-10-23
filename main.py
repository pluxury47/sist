import socket
import threading

clients = []

def client_thread(con, addr):
    print(f"Клиент {addr} подключился")

    while True:
        try:
            data = con.recv(1024)
            if not data:
                break

            message = data.decode()
            print(f"Сообщение от {addr}: {message}")
            for client in clients:
                if client != con:
                    client.send(data)
        except:
            break

    print(f"Клиент {addr} отключился")
    con.close()
    clients.remove(con)


def start_server():
    server = socket.socket()
    hostname = socket.gethostname()
    port = 12345
    server.bind((hostname, port))
    server.listen(5)

    print("Сервер запущен")

    while True:
        con, addr = server.accept()
        clients.append(con)
        threading.Thread(target=client_thread, args=(con, addr)).start()


if __name__ == "__main__":
    start_server()
