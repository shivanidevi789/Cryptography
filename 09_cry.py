# Write a Program to Implement Euclid's algorithm for finding GCD.  
def gcd(a, b):    
    while b:       
        a, b = b, a % b    
    return a  
    
print("GCD of 54 and 24:", gcd(54, 24)) 