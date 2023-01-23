def armstrogFind(num):
    length = len(str(num))
    newNum = 0
    for i in range(length):
        single_num = num%10 
        newNum += single_num**length
        # num = int(num/10) # or use num = num//10
        num = num//10
    return newNum
    
for i in range(10,1000):
    fucNum = armstrogFind(i+1)
    if i+1 == fucNum:
        print(fucNum )