# Write a Program to Implement one block cipher mode (e.g., CBC).  
from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes 
from Crypto.Util.Padding import pad, unpad


key = get_random_bytes(16) 
iv = get_random_bytes(16) 
cipher = AES.new(key, AES.MODE_CBC, iv) 

plaintext = b'CBC Mode Test' 
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size)) 
cipher2 = AES.new(key, AES.MODE_CBC, iv) 
decrypted = unpad(cipher2.decrypt(ciphertext), AES.block_size) 
 
print("Encrypted:", ciphertext.hex())
print("Decrypted:", decrypted.decode())