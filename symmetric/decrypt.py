'''
Symmetric Key Decryption using Stream Ciphers
'''

key = [1,0,1,0,1,1] # the following is a 6 bit key

cipherText = input("Enter the generated cipher text: ")
cipherText = list(map(int, str(cipherText))) # convert string to list

def xor(a, b):
  '''
  XOR implementation to generate plain text
  '''
  p = []                # empty string to hold plain text
  for i in range (0,6):
    if (a[i] == b[i]):  # if 1,1 or 0,0 then 0
      p.append(0)
    else:               # if 1,0 or 0,1 then 1
      p.append(1)
  return p              # return plain text

plainText = xor(cipherText, key) # decrypt cipher text using the key
plainText = ''.join(str(e) for e in plainText) # convert list to string

print('The generated plain text is: {}'.format(plainText))
