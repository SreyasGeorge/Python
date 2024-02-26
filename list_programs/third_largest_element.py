numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
numbers.sort(reverse=True)
if len(numbers) < 3:
    print("The list must contain at least 3 numbers.")
else:
    print("The 3rd largest number is:", numbers[2])
