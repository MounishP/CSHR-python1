"""
1. Define ->
2. Call
"""


# print("before function")
#
#
# def functionName():  # function def
#     a = 6
#     b = 7
#     print(a + b)
#
#
# print("After function")
# functionName()  # function call
# functionName()
# functionName()
# functionName()
# functionName()
# functionName()
# functionName()

def addTwoNum(a, b):
    print(a + b)


# addTwoNum(5, 4)
# addTwoNum(2, 4)
# addTwoNum(3, 4)
# addTwoNum(5, 4)
# addTwoNum(8, 4)
# addTwoNum(9, 4)
# addTwoNum(3, 4)
# addTwoNum(1, 4)

for i in range(1, 11):
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    addTwoNum(a, b)
