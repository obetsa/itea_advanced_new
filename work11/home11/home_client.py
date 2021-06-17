import socket
from time import sleep
import sys

from logging import getLogger, StreamHandler

logger = getLogger(__name__)
stdout_handler = StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel("DEBUG")

sock = socket.create_connection(("127.0.0.1", 10002), timeout=5)
sock.settimeout(2)

with sock:
    with open('client.txt', 'r') as f:
        for i in f.readlines():
            data_for_sending = i.strip('\n').encode("utf-8")
            sock.sendall(data_for_sending)
            logger.info(f"send data {data_for_sending}")
            sleep(1)