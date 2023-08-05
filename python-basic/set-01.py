# 1. Hello, World!: Write a Python program that prints "Hello, World!" to the console.
print("Hello, World!")

#2. Data Type Play: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.

number=6;  #integer
num=34.2   # float
stri = "pawan" # string
is_number = False #boolean
data_list = ["pawan","aman","chhunu"];

my_tuple = (10, 20, 30)
print("Tuple:", my_tuple, "Type:", type(my_tuple))

my_dictionary = {
    "name":"pawan",
    "age":20
}

my_set = {3,8,12,48}

# 3. Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
# Create a list of numbers from 1 to 10
numbers_list = list(range(1, 11))
print(numbers_list)

# Add a number to the list
numbers_list.append(11)
print(numbers_list)

# Remove a number from the list
if 5 in numbers_list:
    numbers_list.remove(5)
    print("List after removing 5:", numbers_list)
else:
    print("5 not found in the list")

# Sort the list
numbers_list.sort()
print(numbers_list)

# 4 .Write a Python program that calculates and prints the sum and average of a list of numbers.

numbers_list = [3,5,6,7,8,9,5]

total_sum = sum(numbers_list)

# Calculate the average of the numbers
average = total_sum / len(numbers_list)

print(average)

# 5.String Reversal: Write a Python function that takes a string and returns the string in reverse order.

def reverse_str(string):
    return string[::-1]

my_str = "pawan kumar"

print(reverse_str(my_str))

# 6 .Count Vowels: Write a Python program that counts the number of vowels in a given string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

# Test the function
input_string = "pawan kumar"
vowel_count = count_vowels(input_string)
print(vowel_count)

# 7.Prime Number: Write a Python function that checks whether a given number is a prime number.
