# How To Create A Currency Converter In Python? | Nepali to all
with open('currencyData.txt') as f:
	lines = f.readlines()

currencyDict = {}   #initializing Dictonary
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]  #keys as parsed[0] and value as parsed[1]
 
amount = int(input("Enter a amount:\n"))
print(f"Enter the name of Curreny you want to convert this amount to ? Available options :\n,")
# print(currencyDict.keys())  #This will not work for item in dictonary
[print(item) for item in currencyDict.keys()]
curreny = input("Please enter one of these values:\n")
print(f"{amount} nepali is equal to {amount* float(currencyDict[curreny]) } {curreny}")
 
   
