
"""
#Reverse purmid using while loop
outer = 5
i = 1
while(i <= outer):
    j=outer
    while(j >= i):
        print(j, end="")
        j-=1
    i+=1
    print()
"""

''''
#To calculate summ of all numbers
num = int(input("Enter any Number: "))
i = 1 
sum=0
while(i<=num):
    sum+=i
    i+=1
print(sum)
'''
'''
#To calculate the table
num = int(input("Ener Num: "))
i=1
while(i<= 10):
    print(num * i)
    i+=1
    '''

#To calclute number of digits
'''
num = int(input("Enter Num: "))
counter = 0
while(num != 0 ):
    num //= 10
    counter+=1
print(counter)
'''
#To print reverse pyramid
"""
num = int(input("Enter nUm: "))
for i in range(0, num + 1):
    for j in range(num - i, 0, -1):
        print("*",end="")
    print()
"""



#To Get Prime Number betwwena range
'''
for i in range(25, 50 + 1):
    if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            print(i)
'''