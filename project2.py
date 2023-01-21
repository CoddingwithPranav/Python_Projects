# How To Find Factorial & No Of Trailing Zeros In A Factorial Of A Number In Python?
def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)
def factorialTrailingZero(num):
    count = 0
    i = 5
    while (num//i != 0):
        count += int(num/i)
        i = i*5
    return count    

if __name__ == '__main__':
    num = int(input("Enter a number to find factorial :\n"))
    # fact = factorial(num)
    # print(fact)
    print(factorialTrailingZero(num))
