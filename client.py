import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

req = {"val": 273.15, "conv_from": "k", "conv_to": "c"}
req_json = json.dumps(req)

s.send(bytes(req_json, "utf-8"))
msg = s.recv(2048).decode()
print(msg)
