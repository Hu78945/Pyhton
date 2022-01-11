"""Get all the sub string of a value
value = input("Enter A Value: ")
for i in range(len(value)):
    print(value[i])
for j in range(len(value) - 1):
    print(value[j] + value[j+1])
print(value)
"""
"""Binary of the number
num = int(input("Enter a number: "))
i = 0
while(i <=num):
    print(num % 2)
    if(num != 0):
        num = num //2
    i+=1
"""
"""Dont Know
num = int(input("Enter a Nnumber: "))
for i in range(num + 1):
    fold1 = 1
    fold2 = 1
    fnew = fold2 + fold1
    fold2 = fold1
    fold1 = fnew
print(fold2)
"""


"""Reverse of the name
name = input("Enter your name: ")
j = len(name) - 1
while(j>=0):
     print(name[j])
     j-=1
"""

"""
num1 = int(input("Enter any Number: "))
num2 = int(input("Enter any Number: "))
num3 = int(input("Enter any Number: "))
if((num1 > num2) and (num2 > num3)):
    print("dECRESING")
elif((num1 < num2) and (num2 < num3)):
    print("Increasing")
else:
    print("neither")

"""


#Print the number of digits of the number
num = int(input("Enter any Number: "))
digit = 0
while(num >= 100):
    digit+=1
    num = num // 10
while(num >= 10):
    digit+=1
    num = num //10
while(num >= 1):
    digit+=1
    num = num // 10
print(digit)



        


