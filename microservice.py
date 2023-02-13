import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    receiverSocket, address = s.accept()
    print('New connection established from {}'.format(address))
    try:
        while 1:
            msg = json.loads(receiverSocket.recv(2048).decode())
            if not msg:
                break
            else:
                to_celsius = str("%.2f" % (float(msg["val"]) - 273.15))
                print("Conversion request received...")
                receiverSocket.send(bytes(to_celsius, "utf-8"))
                print("Conversion processed.")
                receiverSocket.close()
    except:
        print("Connection from {} closed.".format(address))
        continue

