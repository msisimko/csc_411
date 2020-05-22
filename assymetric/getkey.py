'''
Asymmetric Key Decryption using RSA
'''
import random
from math import gcd

def coprime(a, b):
  '''
  Determine if 'a' is a coprime of 'b'
  '''
  return gcd(a, b) == 1                         # if the gcd of a & b is 1, they are coprimes

p = int(input("Enter a prime number: "))        # get a first prime number
q = int(input("Enter another prime number: "))  # get a second prime number
N = p * q                                       # get N
pN = (p-1) * (q-1)                              # get the phi of N

def getPublicKey(N, pN):
  '''
  Generate the public key
  '''
  loop = True
  
  while(loop):
    e = random.randrange(1, pN)                                 # pick random number between 1 & pN
    if coprime(e, N) and coprime(e, pN) and e > 1 and  e < pN:  # if number is a coprime of N & pN, continue
      loop = False                                              # stop the loop
      return e                                                  # return e

e = getPublicKey(N, pN)                                         # get public key, e

def getPrivateKey(e, pN):
  '''
  Generate the private key
  '''
  d = 1                                   # initialize d = 1
  loop = True

  while(loop):
    result = (e*d) % pN                   # store the product of: e.d mode pN
    if result == 1 and d > 1 and d != e:  # check if result is 1, d > 1 & d != e
      loop = False                        # stop loop
      return d                            # return d
    else:
      d = d + 1                           # increase d by 1

d = getPrivateKey(e, pN)                  # get private key, d

print('The public key is: ({}, {}) and the private key is: ({}, {})'.format(e,N,d,N))
