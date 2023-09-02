# n = int(input("Enter the number: "))  # 5

# n%2==0   -> true -> even
#          -> false -> odd
# Ctrl + Alt + L   -> for formatting the file

# if n % 2 == 0:
#     print("n is even")
# else:
#     print("n is odd")

# if n == 2:
#     print("n is 2")
# elif n == 3:
#     print("n is 3")
# elif n == 4:
#     print("n is 4")
# else:
#     print("n is not in the above")


# check input with boolean

# n = int(input("Enter a number: "))

# if n >= 0:
#     print("n is positive")
#     if n % 2 == 0:
#         print("n is even")
#     else:
#         print("n is odd")
# else:
#     print("n is negative number")


# if 'g' in "string":
#     print("value is present")
# else:
#     print("value is not present")

prelims = bool(input("passed prelims"))
mains = input("passed mains")
interview = input("passed interview")
training = input("passed taining")

if prelims:
    print("prelims passed")
    if mains == "True":
        print("passed mains")
        if interview == "True":
            print("passed interview")
            if training == "True":
                print("Training completed")
            else:
                print("Training not completed")
        else:
            print("failed interview")
    else:
        print("failed mains")
else:
    print("failed prelims")
