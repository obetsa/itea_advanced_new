import socket
import sys
import datetime

from logging import getLogger, StreamHandler


logger = getLogger(__name__)
stdout_handler = StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel("DEBUG")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 10002))
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
conn.settimeout(5)

with conn, sock:
    while True:
        received_data = conn.recv(1024)
        if received_data == b'':
            break
        with open('server.txt', 'a') as f:
            logger.info(f"received data: {received_data}")
            f.write(f'{datetime.datetime.now()} {received_data.decode("utf-8")}')
            print(f'{datetime.datetime.now()} {received_data.decode("utf-8")}', file=f)