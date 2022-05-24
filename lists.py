numbers = [3, 5, 7, 9, 10.5]
numbers.append("Python")
print("numbers:", numbers)
print(len(numbers))
print(numbers[0])
print(numbers[5])
print(numbers[-1])
print(numbers[1:5])
del numbers[5]
print("numbers:", numbers)
numbers.append("Python")
print("numbers:", numbers)
numbers.remove("Python")
print("numbers:", numbers)