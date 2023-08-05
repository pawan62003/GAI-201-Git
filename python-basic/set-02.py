### Problem **1: Print the following pattern**
# Write a program to print the following number pattern using a loop.

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
print()


# ### Problem **2: Display numbers from a list using loop**
# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop
# **Given**:

# **Expected output:**
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)


# 3. ### Problem **3: Append new string in the middle of a given string**
# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.
# **Given**:
# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```
# **Expected Output**:

s1 = "Ault"
s2 = "Kelly"

mid_index = len(s1) // 2
s3 = s1[:mid_index] + s2 + s1[mid_index:]

print(s3)


# 4.### Problem **4: Arrange string characters such that lowercase letters should come first**
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# **Given**:
# ```
# str1 = PyNaTive
# ```
# **Expected Output**:

str1 = "PyNaTive"

lowercase_chars = ""
uppercase_chars = ""

for char in str1:
    if char.islower():
        lowercase_chars += char
    else:
        uppercase_chars += char

arranged_str = lowercase_chars + uppercase_chars

print(arranged_str)

# 5. ### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
# **Given**:
# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```
# **Expected output:**
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []

min_length = min(len(list1), len(list2))

for i in range(min_length):
    new_list.append(list1[i] + list2[i])

# Add any leftover items
new_list.extend(list1[min_length:])
new_list.extend(list2[min_length:])

print(new_list)


# 6. ### Problem **6: Concatenate two lists in the following order**
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# **Expected output:**

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = []

for item1 in list1:
    for item2 in list2:
        result.append(item1 + item2)

print(result)

# 7.### Problem **7: Iterate both lists simultaneously**
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
# **Given**
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# **Expected output:**

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for item1, item2 in zip(list1, reversed(list2)):
    print("list1:", item1, "| list2:", item2)
