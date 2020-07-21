'''
Topic #2: Strings (Chuỗi Ký Tự) - a sequence of characters
'''
# String: ordered, immutable, text presentation

# Immutable which means they cannot be changed after they are created.
'''
mutable: Thay Đổi Được

list
dict
set
bytearray
Các class được định nghĩa bởi code (mặc định)

immutable: Không Thay Đổi Đc - hi đuợc tạo ra sẽ chứa toàn bộ các phần tử của nó, và nó "đóng băng" ở đó memory address đó
Khi chúng ta muốn thay đổi giá trị của biến gán cho tuple đó, một tuple khác, ở một vùng nhớ khác sẽ được tạo ra.

int
float
decimal
complex
bool
string
tuple
range
frozenset
bytes
'''
# tạo các chuỗi trong Python bằng cách bao một text trong dấu nháy đơn/kép
# use singe or double quotes
my_string = 'Hello World!'
my_string = "Hello World!"

my_string = "My name's CodeXplore"

# escaping backslash
my_string = 'I\' m  a "Cuu Du Hoc Sinh Sing"'
my_string = 'I\' m living in \'Singapore\''

# backslash if you want to continue in the next line
my_string = "Voi mong muon tao nen mot platform \
chia Se nhung Kien Thuc Lap Trinh"
# print(my_string)

'''
Access characters and substrings
'''
my_string = "Hello World"
# get character by referring to index
char = my_string[0]  # H
char = my_string[-1]  # d
char = my_string[-2]  # l
# print(char)
# Cannot be changed
# my_string[0] = 'h' #As String is immutable -> Cannot be changed

# Substrings with slicing
# stringName[startIndex:endIndex]
# start at index 1 and go until index 5 (not include #5)
substring = my_string[1:5]
substring = my_string[:5]  # start from begining
substring = my_string[1:]  # stop at end of string

substring = my_string[1:5:1]  # By default
substring = my_string[::-1]  # Reverse the String


# print(substring)

'''
Concatenate two or more strings
'''

# concat strings with +
greeting = "Hello"
name = "Tom"
sentence = greeting + ' ' + name
# print(sentence)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
# the given string is the separator, e.g. ' ' between each argument
a = ' '.join(my_list)


'''
 Iterating
'''
# Iterating over a string by using a for in loop
my_string = 'Hello'
# for char in my_string:
#     print(char)

'''
Check if a character or substring exists
'''
# if "e" in "Hello":
#     print("yes")
# if "llo" in "Hello":
#     print("yes")

'''
Basic & Useful Function (Hàm Cơ Bản và Hữu Ích)
'''

# 'I am alone' --> Strips all whitespace characters from both ends.
print('  I am alone '.strip())
# 'On an islan' --> # Strips all passed characters from both ends.
'On an island'.strip('d')
'but life is good!'.split()           # ['but', 'life', 'is', 'good!']
'but, quite Boring'.split(',')        # ['but', 'quite Boring']
# 'Help you' --> Replaces first with second param
'Help me'.replace('me', 'you')


'Need to make fire'.startswith('Need')  # True
'and cook rice'.endswith('rice')      # True
# returns the starting index position of the first occurence
'bye bye'.index('e')                  # 2
'oh hi there'.find('i')               # 4

'still there?'.upper()                # STILL THERE?
'HELLO?!'.lower()                     # hello?!
'how are you?'.title()                # How Are You?
'true'.title()                        # True => convert to Boolean eval(True)
'ok, I am done.'.capitalize()         # 'Ok, I am done.'

'oh hi there'.count('e')              # 2

'''
String Formatting
'''
# %, .format(), f-Strings
# %
name = "CodeXplore"
my_string = "Variable is %s" % name

pi = 3.14159
s = "Variable pi"
my_string = "Variable is %.2f from %s" % (pi, s)
# .format()
age = 24
my_string = "Variable is {:.3f} and {}".format(pi, age)

# f-Strings
my_string = f"Variable is {pi:.2f} and {age}"

# f-Strings are evaluated at runtime, which allows expressions
my_string = f"The value is {2*60}"
print(my_string)
