'''
Asymmetric Key Decryption using RSA
'''
e = int(input("Enter the first value of your generated public key: "))
N = int(input("Enter the second value of your generated public key: "))

plainText = int(input("Enter number to be encrypted: "))

cipherText =  pow(plainText, e, N) # (pT ^ e) mod N

print('The encrypted text is: {}'.format(cipherText))