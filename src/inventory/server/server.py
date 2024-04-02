import json
import socket

from inventory.controler.controler import InventoryControler

HOST = "127.0.0.1"
PORT = 4434


class Server:
    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        inventory_controler: InventoryControler | None = None,
    ) -> None:
        self.host = host or HOST
        self.port = port or PORT
        self.inventory_controler = inventory_controler or InventoryControler()

    def start(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            client, address = s.accept()
            with client:
                print(f"Connection ostablished with: {client, address}")
                while True:
                    data = client.recv(1024)
                    if not data:
                        break

                    status = 0
                    error = None
                    result = None
                    command = None

                    try:
                        command = json.loads(data)
                        result = self.inventory_controler.execute(command)

                        if isinstance(result, Exception):
                            status = 1
                            error = result

                    except json.decoder.JSONDecodeError as e:
                        status = 2
                        error = e
                        command = data.decode()

                    response = {
                        "status": status,
                        "result": result,
                        "command": command,
                        "origin": list(address),
                        "error": error,
                    }

                    client.sendall(f"{response}\n".encode())


def main():
    server = Server("127.0.0.1", 4434)
    server.start()


if __name__ == "__main__":
    main()
