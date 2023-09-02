"""Strong -> sum of the factorial == given number
1. Take input as a number
2. Separate the digits
3. Factorial of the digit -> (5*4*3*2*1)
4. sum the factorials
5. sum == number
"""

n = int(input("Enter the number: "))    #145,14,1,0
temp = n                                #145
sum = 0
while n > 0:                            #145>0,14>0,1>0,0>0
    digit = n % 10                      #145%10=5,14%10=4,1%10=1
    print(digit)
    fact = 1                            #1
    for i in range(1,digit + 1):        #1,
        fact = fact * i                 #1*1=1
    sum = sum + fact                    #0+120=120,120+24=144,144+1=145
    n = n//10                           #145//10=14,14//10=1,1//10=0


if sum == temp:           #145==145
    print("the number is a Strong number")
else:
    print("the number is not a Strong number")


