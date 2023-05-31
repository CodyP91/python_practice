def square_number(num):
    return num ** 2


def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)


def is_even(num):
    return num % 2 == 0


def print_numbers(numbers):
    for num in numbers:
        print(num)


def sum_numbers(numbers):
    return sum(numbers)


def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)


def factorial_smaller_number(num1, num2):
    smaller = min(num1, num2)
    factorial = 1
    for i in range(1, smaller + 1):
        factorial *= i
    return factorial


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = sum(1 for char in string if char.lower() in vowels)
    return count


def get_last_half_array(array):
    half_length = len(array) // 2
    last_half = array[half_length:]
    return last_half


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_largest_number_no_builtin(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers


def convert_temperature(number, unit):
    if unit == 'F':
        return (number - 32) * 5 / 9
    elif unit == 'C':
        return (number * 9 / 5) + 32
    else:
        print("Error: Invalid unit")


def is_power_of_two(num):
    if num <= 0:
        return False
    while num > 1:
        if num % 2 != 0:
            return False
        num = num // 2
    return True


def common_strings(array1, array2):
    common = []
    for string in array1:
        if string in array2:
            common.append(string)
    return common

# Testing the functions
# You can call each function here and verify its output
