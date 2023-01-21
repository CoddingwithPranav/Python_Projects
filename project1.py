# How to Create An Indian Kirana Store Calculator & Receipt Generator In Basic Python?
userName = input("Enter customer name :")

with open("bill.txt","w") as f:
    f.write(userName + "Bill Details" + "\n")
product_l =[]
Sum = 0
i = 1
while True:
    prize = input("Enter prize of  product or press q to quit :\n")
    if prize!='q':
        product_l.append(prize)
        Sum = Sum + int(prize)
        with open("bill.txt", "a") as f:
            f.write(str(i) + " . " + prize +"\n")
        i +=1
    else:
        print("Thanks for using our App")
        break

print(f"Your total prize is {Sum}")