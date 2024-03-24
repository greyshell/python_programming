# variable name can't begin with digit
# descriptive names are better than short name
# use camel case(class name) or snake case(function / variable name)
# PEP => python enhancement proposal

# strings are used to represent text
print(type("hello"))
# string literals => when we create a string surrounding with quotation marks, means
#   a string that is literally written out in your code
print("Corner's")
# string delimiters => single quote and double quote, escape chars is backslash
print("Corner\"s")
# best practice use double chars as string delimiters
# string can contain valid unicode chars
print("×Pýŧħøŋ×")
# break the string in multiline
paragraph = "This planet has—or rather had—a problem, which was \
            the small green pieces of paper that were unhappy."

paragraph_alt = """This planet has—or rather had—a problem, which was
the small green pieces of paper that were unhappy."""

# string - concatenation with + operator
first_name = "abhijit"
last_name = "sinha"
full_name = "mr" + " " + first_name + " " + last_name
print(full_name)

# string indexing -> index starts with 0, get IndexError if trying to access beyond the length
print(first_name[0])
# negative indexing: last char is the -1
# get the last char of a string without using len() and typing less code
print(first_name[-1])

# string slicing: extract a portion of a string / substring
# if you omit the first index in the slice then default = 0
print(first_name[:3])
# if you omit the second index in the slice then default = last
print(first_name[1:])
# it does not include the last char in the slice
# python does not raise error when you try to extract outside the boundary, it just returns empty string

# slice[start_index, end_index, step], end_index => item on index not included
# reverse a string: last arg = step, determines the increment between each index for slicing
print(first_name[::-1])

# string manipulation methods
print(first_name.upper())  # returns a copy of the original string coz strings are immutable
print(first_name.lower())
# removing the white space from both left and right side of the string, does not remove anything in the middle
address = "    this      is      "
print(address.strip())
address = "english"
print(address.startswith("en"))
print(address.find("en"))  # return the index

# interaction with user
# num = input("enter a number: ")
# print(num)

# strings supports + and *
num = "12"
num = num * 3
print(num)

# convert string to a number
print(int(num))  # you can't convert floating point string "12.0" to integer

num = 10_000_00  # this is integer literal, whereas int("10") => this is not
# group the numbers with _
print(num)  # max value = no limit

# E notation float representation
num2 = 1e6
num3 = float(2e7)
print(num2, num3)  # max value = depends on the system, when max is reached then python returns inf
print(2e400)  # inf

# add int and float => result is float
# division returns float, so convert that to int
num = 6 / 2  # result is float
print(type(num))

num = 6 // 2  # ensure that result is int, floor division operator
print(type(num))

print(-5 // 2, 5 // 2)  # -3, 2 => both results are not same

# raise a power of 2
print(3**2)

# returning the reminder
print(3 % 2)
print(-5 % 2, 5 % -2)  # 1, -1 both results are not same


num = 0.1 + 0.2
print(num)  # output= 0.30000000000000004, floating point numbers are stored in the memory

# example of round()
print(round(2.4), round(2.5), round(2.6))
print(f"{num:.2f}")  # display as fixed point number upto 2 decimal places

complex_num = 1 + 2j  # j => denotes the imaginary part
print(complex_num.real, complex_num.imag)
