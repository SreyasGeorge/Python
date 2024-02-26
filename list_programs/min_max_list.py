numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
largest = max(numbers)
smallest = min(numbers)
print("The largest number is:", largest)
print("The smallest number is:", smallest)
