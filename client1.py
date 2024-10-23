import socket
import threading

def receive_messages(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                print("Соединение с сервером потеряно.")
                break
            print("\nНовое смс:", data.decode())
        except:
            print("Ошибка при получении сообщения.")
            break

client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))

receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

try:
    while True:
        message = input("\nНапиши текст: ")
        if message.lower() == "exit":
            break
        client.send(message.encode())
except KeyboardInterrupt:
    print("\nОтключение...")

client.close()
receive_thread.join()
