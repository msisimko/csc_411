'''
Kerberos, with single KDC module

FILE:     alice.py (client)
'''

from Crypto.Cipher import AES                       # AES symmetric key encryption
import base64
import socket                                       # socket module

def receive_shared_key_from_kdc(secret_key, port_kdc):
  '''
  connect to kdc, receive shared key from in return
  '''
  s = socket.socket()                               # create socket object
  host = socket.gethostname()                       # get local machine name

  cipher = AES.new(secret_key, AES.MODE_ECB)
  message = 'alice/client@kerberos'.rjust(64)       # alice's message, padded to make it a multiple of 16
                                                    # as per AES encryption block requirements
  encoded = base64.b64encode(cipher.encrypt(message))
  
  s.connect((host, port_kdc))                       # connect to kdc
  s.send(encoded)                                   # send message
  receipt = s.recv(1024)                            # receive response
  s.close()                                         # Close the socket when done

  secret_key_s = decode_kdc(secret_key, receipt)
  print('Received shared key: {}'.format(secret_key_s))

  return secret_key_s

def decode_kdc(secret_key, receipt):
  cipher = AES.new(secret_key, AES.MODE_ECB)
  decoded = cipher.decrypt(base64.b64decode(receipt))
  return decoded

if __name__ == "__main__":
  secret_key = '4t26pdrhrp3gq4rp'                   # secret key, shared with KDC

  port_bob = 27257                                  # port, for bob
  port_kdc = 44922                                  # port, for kdc

  secret_key_s = receive_shared_key_from_kdc(secret_key, port_kdc)