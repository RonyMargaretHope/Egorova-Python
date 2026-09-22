# SubTask 1. Check the entered number
number = int(input("Enter a number: "))

if number > 7:
    print("Hello")


# SubTask 2. Check the entered name
name = input("Enter a name: ")

if name == "John":
    print("Hello, John")
else:
    print("There is no such name")


# SubTask 3. Numbers that are multiples of 3
numbers = input("Enter numbers separated by spaces: ")

numbers = [int(number) for number in numbers.split()]

print("Numbers that are multiples of 3:")

for number in numbers:
    if number % 3 == 0:
        print(number)


