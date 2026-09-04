numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("Second largest element does not exist.")
else:
    unique_numbers.sort(reverse=True)
    print("Second largest element:", unique_numbers[1])
