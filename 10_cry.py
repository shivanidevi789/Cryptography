#  Write a Program to Compute MD5 hash for a given string. 
import hashlib 

data = "hello" 
hash_result = hashlib.md5(data.encode()).hexdigest() 
print("MD5 Hash:", hash_result)