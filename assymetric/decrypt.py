'''
Asymmetric Key Decryption using RSA
'''
d = int(input("Enter the first value of your generated private key: "))
N = int(input("Enter the second value of your generated private key: "))

cipherText = int(input("Enter number to be decrypted: "))

plainText =  pow(cipherText, d, N) # (cT ^ d) mod N

print('The decrypted text is: {}'.format(plainText))