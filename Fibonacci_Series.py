import time
init = time.time()
def fibonacciRec(num):
    if num==0 :
        return 0
    elif num ==1:
        return 1
    return  fibonacciRec(num-1) + fibonacciRec(num -2)
def fibonacciItr(num):
    previousnum = 0
    currentnum = 1
    for i in range(0, num):
        prevPrevNum = previousnum
        previousnum = currentnum
        currentnum = previousnum + prevPrevNum
    return currentnum
if __name__ == "__main__":
    n = int(input("Enter how much fibonacci series you want :"))
    for i in range(n):
        fibRec =  fibonacciRec(i) # dont use recursion because it use most of memeory in computer
        print(fibRec)
    print("***************************************")
    for i in range(n):
        fibItr =  fibonacciItr(i)
        print(fibItr)
    print(f"It took {time.time() -init} second")