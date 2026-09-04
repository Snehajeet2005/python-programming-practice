numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for number in numbers:
    if number not in result:
        result.append(number)

print("List after removing duplicates:", result)
