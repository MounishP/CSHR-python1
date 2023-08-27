str = "micrOsoft is tHe best coMpaNy.?/@!@#$%^&*() mounish is teaching"

# print(str[-4])
# s2 = "school"

# print(s1 + " " + s2)
"""String slicing"""
s1 = slice(0,50,2)  # 0,1,2,3,4
print(str[s1])  # give me a slice of 5 from str

"""String methods"""
# Assignment 2 -> pratice all string methods
print(str.lower())  # convert everything into lower case
print(str.upper())
print(str.title())
print(str.swapcase())
print(str.capitalize())

"""String replace """
words = "Happy Happy Happy Happy Happy Happy Happy Happy Happy Happy Birthday"
print(words.replace("Happy", "Great"))
print(words.replace("Happy", "Great", 3))


"""String Splitting"""

numbers = "1,2,3,4,5,6,7,8"
nums = numbers.split(',')
print(nums)

print(str.split('o'))
