numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

seen = {}

for index, number in enumerate(numbers):

    complement = target - number

    if complement in seen:
        print("Pair found at indices:", seen[complement], index)
        break

    seen[number] = index

else:
    print("No pair found.")
