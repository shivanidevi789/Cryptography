#  Write a program to implement the Caesar cipher for encryption and decryption of a given plaintext. 
def caesar_encrypt(text, shift):   
        result = ""   
        for char in text:      
            if char.isalpha():    
                base = 'A' if char.isupper() else 'a'          
                result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))        
            else:            
                result += char   
        return result 
def caesar_decrypt(text, shift):    
    return caesar_encrypt(text, -shift) 

plaintext = "Hello World" 
shift = 3 
encrypted = caesar_encrypt(plaintext, shift) 
decrypted = caesar_decrypt(encrypted, shift)  
print("Encrypted:", encrypted) 
print("Decrypted:", decrypted) 