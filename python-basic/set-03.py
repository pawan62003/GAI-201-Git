# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."

tuple_list = [("John", 25), ("Jane", 30)]

result = ""
for name, age in tuple_list:
    # result.append("")
     result += f"{name} and {age} year old. "

# print(result)

# # 2. 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

my_dictionary = {
     "pawan":21
}

# addition of new name-age value pair;
my_dictionary["aman"] = 22

# updation of new name-age pair;
my_dictionary["pawan"] = 20

# deletion of new name-age pair;
del my_dictionary["aman"]

print(my_dictionary)

# 3.1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
    # - *Input*: [2, 7, 11, 15], target = 9
    # - *Output*: "[0, 1]"


def check_target(num,target):
     num_with_index = {}
     
     for index, item in enumerate(num):
          compleated = target-item
          if compleated in num_with_index:
               # print(num_with_index[compleated])
               return [num_with_index[compleated],index]
          num_with_index[item] = index
     return 'none'

numd = [4,5,6,7,0]
targetd = 9

ans = check_target(numd,targetd)
print(ans)

# 4. 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def check_palidrome(string):
     reverse = ""

     for char in string[::-1]:
          reverse += char

     if string == reverse:
          return True
     
     return False


# print(check_palidrome("madam"))


# 5. 1. **Selection Sort**: Implement the selection sort algorithm in Python.
    - *Input*: [64, 25, 12, 22, 11]
    - *Output*: "[11, 12, 22, 25, 64]"