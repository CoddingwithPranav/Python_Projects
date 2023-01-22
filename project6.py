#This is our own password generator
import string
import random

if __name__ =='__main__':
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    plen = int(input("Enter password length\n"))
    s = []
    s.extend(list(s1)) 
    s.extend(list(s2)) 
    s.extend(list(s3)) 
    s.extend(list(s4)) 
    # Alternative MEthod
    # random.shuffle(s)
    # print(s)
    # password = "".join(s[0:plen])  
    # print(password)
    
    password = "".join(random.sample(s,plen))
    print(password)
    