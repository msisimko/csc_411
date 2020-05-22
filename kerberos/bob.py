'''
Kerberos, with single KDC module

FILE:     bob.py (server)
'''

from Crypto.Cipher import AES                       # AES symmetric key encryption
import base64
import socket                                       # socket module

def receive_shared_key_from_kdc(secret_key):
  s = socket.socket()                               # create socket object
  host = socket.gethostname()                       # get local machine name
  port = 27257                                      # reserve port for service
  s.bind((host, port))                              # bind socket object to host, port

  s.listen(5)                                       # wait for client connection
  
  active = True
  
  while active:
    c, addr  = s.accept()                           # establish connection with client
    receipt = c.recv(1024)
    secret_key_s = decode_kdc(secret_key, receipt)
    print('From address: {}, received shared key: {}'.format(addr, secret_key_s))
    c.close                                         # close socket

    active = False
  
  return secret_key_s

def decode_kdc(secret_key, receipt):
  cipher = AES.new(secret_key, AES.MODE_ECB)
  decoded = cipher.decrypt(base64.b64decode(receipt))
  return decoded

if __name__ == "__main__":
  secret_key = 'fy2qafmv32zw8zhg'                   # secret key, shared with KDC

  secret_key_s = receive_shared_key_from_kdc(secret_key)