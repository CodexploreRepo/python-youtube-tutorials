'''
Topic 8 - Dictionary:  một tập hợp các cặp key-value không có thứ tự, có thể thay đổi và lập chỉ mục (truy cập phần tử theo chỉ mục). 
Dictionary được khởi tạo với các dấu ngoặc nhọn {} và chúng có các khóa và giá trị (key-value). 
Mỗi cặp key-value được xem như là một item. Key mà đã truyền cho item đó phải là duy nhất, 
trong khi đó value có thể là bất kỳ kiểu giá trị nào. 

Key phải là một kiểu dữ liệu không thay đổi (immutable) như chuỗi, số hoặc tuple.
'''

# Create a new Dictionary: A dictionary is a collection which is unordered, changeable and indexed.
# A dictionary consists of a collection of key-value pairs.

my_dict = {"name": "Max", "age": 28, "city": "New York"}
print(my_dict)

# or use the dict constructor, note: no quotes necessary for keys
my_dict_2 = dict(name="Lisa", age=27, city="Boston")
print(my_dict_2)

# Access items
name_in_dict = my_dict["name"]
print(name_in_dict)

# KeyError if no key is found
# print(my_dict["lastname"])


# Add and change items
# add a new key
my_dict["email"] = "max@xyz.com"
print(my_dict)

# or overwrite the now existing key
my_dict["email"] = "coolmax@xyz.com"
print(my_dict)

# Delete items
# delete a key-value pair
del my_dict["email"]

# this returns the value and removes the key-value pair
print("popped value:", my_dict.pop("age"))

# return and removes the last inserted key-value pair
# (in versions before Python 3.7 it removes an arbitrary pair)
print("popped item:", my_dict.popitem())

print(my_dict)

# clear() : remove all pairs
# my_dict.clear()

# Check for keys
my_dict = {"name": "Max", "age": 28, "city": "New York"}
# use if .. in ..
if "name" in my_dict:
    print(my_dict["name"])

# use try except
try:
    print(my_dict["firstname"])
except KeyError:
    print("No key found")

# Looping through Dictionary
# loop over keys
for key in my_dict:
    print(key, my_dict[key])

# loop over keys
for key in my_dict.keys():
    print(key)

# loop over values
for value in my_dict.values():
    print(value)

# loop over keys and values
for key, value in my_dict.items():
    print(key, value)
