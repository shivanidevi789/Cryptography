# Write a Program to Create a calculator for modular arithmetic operations

def modular_calculator(a, b, mod):     
    return {         
            'add': (a + b) % mod,         
            'sub': (a - b) % mod,         
            'mul': (a * b) % mod,         
            'div': (a * pow(b, -1, mod)) % mod if b != 0 else 'undefined'     
            }  
result = modular_calculator(7, 5, 11) 
print(result) 