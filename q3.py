start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: ")) 
numbers = range(start, end)
for number in numbers:
    if number % 7 != 0:
        print(number)