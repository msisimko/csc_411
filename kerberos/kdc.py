'''
Kerberos, with single KDC module

FILE:     kdc.py (key distribution center)
'''

from Crypto.Cipher import AES                     # AES symmetric key encryption
import base64
import socket                                     # socket module

def receive_request_from_alice(secret_key_a, secret_key_s):
  '''
  receive request from alice, send her the shared key, encrypted
  '''
  s = socket.socket()                               # create socket object
  host = socket.gethostname()                       # get local machine name
  port = 44922                                      # reserve port for service
  s.bind((host, port))                              # bind socket object to host, port

  s.listen(5)                                       # wait for client connection

  active = True

  while active:
    c, addr  = s.accept()                           # establish connection with client
    receipt = c.recv(1024)

    decoded= decode_alice_request(secret_key_a, receipt)
    print('From address: {}, received request from: {}'.format(addr, decoded))

    encoded_a = encode_secret_key_alice(secret_key_a, secret_key_s)
    c.send(encoded_a)                               # send shared key to alice
    print('Sent shared key to: Alice')
    c.close                                         # close socket

    active = False

  return True

def decode_alice_request(secret_key_a, receipt):
  '''
  decode alice's request using her secret key
  '''
  cipher = AES.new(secret_key_a, AES.MODE_ECB)
  decoded = cipher.decrypt(base64.b64decode(receipt))
  return decoded

def encode_secret_key_alice(secret_key_a, secret_key_s):
  '''
  encrypt shared key with alice's secret key
  '''
  cipher = AES.new(secret_key_a, AES.MODE_ECB)
  encoded = base64.b64encode(cipher.encrypt(secret_key_s))
  return encoded

def encode_secret_key_bob(secret_key_b, secret_key_s):
  '''
  encrypt shared key with bob's secret key
  '''
  cipher = AES.new(secret_key_b, AES.MODE_ECB)
  encoded = base64.b64encode(cipher.encrypt(secret_key_s))
  return encoded

def send_bob_shared_key(secret_key_s, secret_key_b, port_bob):
  '''
  send bob the shared key, encryted
  '''
  s = socket.socket()                               # create socket object
  host = socket.gethostname()                       # get local machine name
  
  s.connect((host, port_bob))
  encoded_b = encode_secret_key_bob(secret_key_b, secret_key_s)
  s.send(encoded_b)
  print('Sent shared key to: Bob')
  s.close()

if __name__ == "__main__":
  secret_key_s = '7bkzycr5ax548jzn'                 # secret key, shared with both alice & bob
  secret_key_a = '4t26pdrhrp3gq4rp'                 # secret key, shared with alice
  secret_key_b = 'fy2qafmv32zw8zhg'                 # secret key, shared with bob

  port_bob = 27257                                  # port, for bob

  '''
  receive request from alice, send alice shared key
  '''
  request = receive_request_from_alice(secret_key_a, secret_key_s)

  '''
  if request from alice has been received & shared key sent back to her, send bob the same shared key
  '''
  if request:
    send_bob_shared_key(secret_key_s, secret_key_b, port_bob)
  