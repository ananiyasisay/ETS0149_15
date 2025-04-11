#1. count()

fruits = ['apple', 'banana', 'orange', 'apple', 'kiwi']
apple_count = fruits.count('apple')
print(f"'apple' appears {apple_count} times in the list.")  # Output: 'apple' appears 2 times in the list.

#2. extend()

numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
numbers.extend(more_numbers)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

#3. index()

colors = ['red', 'green', 'blue', 'yellow']
index_of_green = colors.index('green')
print(f"'green' is found at index {index_of_green}.")  # Output: 'green' is found at index 1.