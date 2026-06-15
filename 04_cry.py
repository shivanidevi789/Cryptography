
# Write a basic version of the DES encryption and decryption. 

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad  

key = b'8bytekey' 
cipher = DES.new(key, DES.MODE_ECB)  

plaintext = b'HelloDES' 
encrypted = cipher.encrypt(pad(plaintext, 8)) 
decrypted = unpad(cipher.decrypt(encrypted), 8)  

print("Encrypted:", encrypted.hex()) 
print("Decrypted:", decrypted.decode()) 