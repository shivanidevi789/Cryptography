# Write a Program to Implement a transposition cipher for rearranging letters. 

def transposition_encrypt(text):     
    return text[1::2] + text[0::2] 
def transposition_decrypt(cipher):    
    half = len(cipher) // 2    
    if len(cipher) % 2:         
        first = cipher[:half+1]         
        second = cipher[half+1:]     
    else:         
        first = cipher[:half]         
        second = cipher[half:] 
    result = ''.join(s + f for s, f in zip(second, first)) + (first[-1] if len(first) > len(second) else '')     
    return  result
plaintext = "Hello" 
encrypted = transposition_encrypt(plaintext) 
decrypted = transposition_decrypt(encrypted) 
print("Encrypted:", encrypted)
print("Decrypted:", decrypted) 