'''
Topic #7: List trong Python - một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau trong nó, 
và chũng ta có thể truy xuất đến các phần tử bên trong nó thông qua vị trí của phần tử đó trong list

Ngôn Ngữ Khác: C/C++, Java, List trong Python = Mảng (Array)

'''

'''
1. Creating a list
'''

list_1 = ["banana", "cherry", "apple"]

# Or create an empty list with the list function
list_2 = list()

# Lists allow different data types
list_3 = [5, True, "apple"]

# Lists allow duplicates
list_4 = [0, 0, 1, 1]

'''
2. Access elements: Truy cập đến các giá trị trong list
'''
my_list = [1, 2, '3',
           True]  # we assume this list won't mutate for each example below
len(my_list)               # 4

my_list.index('3')         # 2
my_list.count(2)           # 1 --> count how many times 2 appears

for item in my_list:
    print(item)

# Python’s built-in enumerate function
# allows us to loop over a list and retrieve
# both the index and the value of each item in the list
presidents = ["Washington", "Adams", "Jefferson",
              "Madison", "Monroe", "Adams", "Jackson"]

# Note: the start=1 option to enum erate here is optional.
# If we didn’t specify this, we’d start counting at 0 by default.
for index, name in enumerate(presidents, start=1):
    print(f"President {index}: {name}")

# Slicing
# : is called slicing and
# has the format [ start : end : step ]
my_list[3]                 # True
my_list[1:]                # [2, '3', True]
my_list[:1]                # [1]
my_list[-1]                # True
my_list[::1]               # [1, 2, '3', True]
# Reverse List by Slicing
my_list[::-1]              # [True, '3', 2, 1]
my_list[0:3:2]             # [1, '3']

'''
3. List Operations & Useful Methods
    3.1. Add to List
'''

# Add to List
my_list * 2                # [1, 2, '3', True, 1, 2, '3', True]
# [1, 2, '3', True, 100] --> doesn't mutate origina list, creates new one
my_list + [100]
# None --> Mutates original list to [1, 2, '3', True, 100]          # Or: <list> += [<el>]
my_list.append(100)
# None --> Mutates original list to [1, 2, '3', True, 100, 200]
my_list.extend([100, 200])
# None -->  [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.
my_list.insert(2, '!!!')
# 'Hello There' --> Joins elements using string as separator.
' '.join(['Hello', 'There'])


'''
    3.2. Remove from List
'''

# 3 --> mutates original list, default index in the pop method is -1 (the last item)
[1, 2, 3].pop()
[1, 2, 3].pop(1)   # 2 --> mutates original list
# None --> [1,3] Removes first occurrence of item or raises ValueError.
[1, 2, 3].remove(2)
[1, 2, 3].clear()  # None --> mutates original list and removes all items: []
del [1, 2, 3][0]


'''
    3.3. Sorting
'''

[1, 2, 5, 3].sort()         # None --> Mutates list to [1, 2, 3, 5]
[1, 2, 5, 3].sort(reverse=True)  # None --> Mutates list to [5, 3, 2, 1]
[1, 2, 5, 3].reverse()      # None --> Mutates list to [3, 5, 2, 1]

sorted([1, 2, 5, 3])        # [1, 2, 3, 5] --> new list created
list(reversed([1, 2, 5, 3]))  # [3, 5, 2, 1] --> reversed() returns an iterator

'''
    3.4. Useful operations
'''

1 in [1, 2, 5, 3]  # True
min([1, 2, 3, 4, 5])  # 1
max([1, 2, 3, 4, 5])  # 5
sum([1, 2, 3, 4, 5])  # 15


'''
4. List Comprehensions
'''
'''
List Comprehension giúp bạn viết code ngắn gọn (đặc biệt khi đang ở trong một vòng lặp đã có) 
và dễ đọc, nhìn code hơn.
'''

# new_list[<action> for <item> in <iterator> if <some condition>]
a = [i for i in 'hello']                  # ['h', 'e', 'l', 'l', '0']

word = "A man, a plan, a canal: Panama"

[i for i in word.lower() if i.isalnum()]

b = [i*2 for i in [1, 2, 3]]                # [2, 4, 6]
c = [i for i in range(0, 10) if i % 2 == 0]  # [0, 2, 4, 6, 8]


# Advanced Functions
# ['H', 'e', 'l', 'l', 'o', 'o', 'o', 'o']
list_of_chars = list('Helloooo')
sum_of_elements = sum([1, 2, 3, 4, 5])                                 # 15
element_sum = [sum(pair)
               for pair in zip([1, 2, 3], [4, 5, 6])]         # [5, 7, 9]
sorted_by_second = sorted(['hi', 'you', 'man'],
                          key=lambda el: el[1])  # ['man', 'hi', 'you']
sorted_by_key = sorted([
                       {'name': 'Bina', 'age': 30},
                       {'name': 'Andy', 'age': 18},
                       {'name': 'zoey', 'age': 55}],
                       key=lambda el: (el['name']))  # [{'name': 'Andy', 'age': 18}, {'name': 'Bina', 'age': 30}, {'name': 'zoey', 'age': 55}]


'''
5. 2D Array/List = Matrix: Mảng 2 Chiều
'''

# Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[2][0]  # 7 --> Grab first first of the third item in the matrix object

# Looping through a matrix by rows:
mx = [[1, 2], [3, 4]]
for row in range(len(mx)):
    for col in range(len(mx)):
        print(mx[row][col])  # 1 2 3 4

# Transform into a list:
[mx[row][col] for row in range(len(mx)) for col in range(len(mx))]  # [1,2,3,4]

# Combine columns with zip and *:
[x for x in zip(*mx)]  # [(1, 3), (2, 4)]


# Exercise:
# Solution: https://leetcode.com/submissions/detail/292886668/
