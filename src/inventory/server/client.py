import socket

HOST = "127.0.0.1"
PORT = 4434


class Client:
    def __init__(self, host: str | None = None, port: int | None = None) -> None:
        self.ip = host or HOST
        self.port = port or PORT

    def connect(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.port))
            s.sendall(b'{"method": "get_items"}')
            data = s.recv(1024)

            print(data)


def main():
    client = Client("127.0.0.1", 4434)
    client.connect()


if __name__ == "__main__":
    main()
