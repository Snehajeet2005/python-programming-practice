numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation count: "))

if len(numbers) == 0:
    print("List is empty.")
else:
    k = k % len(numbers)

    rotated = numbers[-k:] + numbers[:-k] if k != 0 else numbers

    print("Rotated list:", rotated)
