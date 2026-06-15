# Create a program that implements a substitution cipher by mapping each letter of the alphabet to another letter. 

import string 
def substitution_cipher_encrypt(plaintext, key_map):    
    return ''.join(key_map.get(c, c) for c in plaintext)  
def substitution_cipher_decrypt(ciphertext, key_map):     
    inverse_map = {v: k for k, v in key_map.items()}   
    return ''.join(inverse_map.get(c, c) for c in ciphertext) 

# Sample key map 
alphabet = string.ascii_lowercase 
substituted = string.ascii_lowercase[::-1] 
key_map = dict(zip(alphabet, substituted))  

plaintext = "cryptography" 
encrypted = substitution_cipher_encrypt(plaintext, key_map) 
decrypted = substitution_cipher_decrypt(encrypted, key_map) 
print("Encrypted:", encrypted) 
print("Decrypted:", decrypted)