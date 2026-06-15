#  Write a Program to Generate RSA keys using two prime numbers.  
import sympy  

p = sympy.randprime(100, 300) 
q = sympy.randprime(100, 300) 
n = p * q 
phi = (p - 1) * (q - 1) 
e = 65537
d = pow(e, -1, phi)  

print(f"p={p}, q={q}") 
print(f"Public key: (e={e}, n={n})") 
print(f"Private key: (d={d}, n={n})")  