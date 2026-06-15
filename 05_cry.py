#  Write a Program to Demonstrate Triple DES encryption and decryption. 
from Crypto.Cipher import DES3 
from Crypto.Random import get_random_bytes  
from Crypto.Util.Padding import pad, unpad


key = DES3.adjust_key_parity(get_random_bytes(24)) 
cipher = DES3.new(key, DES3.MODE_ECB)  

plaintext = b'TripleDES!!'
encrypted = cipher.encrypt(pad(plaintext, 8)) 
decrypted = unpad(cipher.decrypt(encrypted), 8)  
print("Encrypted:", encrypted.hex())
print("Decrypted:", decrypted.decode()) 