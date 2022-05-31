import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org',80))
# HOst :: data.pr4e.org
# Port :: 80