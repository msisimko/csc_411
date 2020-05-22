'''
Symmetric Key Encryption using Stream Ciphers
'''

key = [1,0,1,0,1,1] # the following is a 6 bit key

plainText = input("Enter a binary string of size 6: ")
plainText = list(map(int, str(plainText))) # convert string to list

def xor(a, b):
  '''
  XOR implementation to generate cipher text
  '''
  c = []                # empty string to hold cipher text
  for i in range (0,6):
    if (a[i] == b[i]):  # if 1,1 or 0,0 then 0
      c.append(0)
    else:               # if 1,0 or 0,1 then 1
      c.append(1)
  return c              # return cipher text

cipherText = xor(plainText, key) # encrypt plain text using the key
cipherText = ''.join(str(e) for e in cipherText) # convert list to string

print('The generated cipher text is: {}'.format(cipherText))
