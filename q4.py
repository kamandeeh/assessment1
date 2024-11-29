def get_input(value):
    while True:
        try:
            num = int(input(value)) 
            return num
        except ValueError:
            print("Invalid input! Enter a numeric value.")
# List to store the five numbers
numbers = []
# Collect 5 numbers from the user
for i in range(1, 6):
    num = get_input(f"Enter number {i}: ")
    numbers.append(num)
max_value = max(numbers)
print(f"The maximum number is: {max_value}")