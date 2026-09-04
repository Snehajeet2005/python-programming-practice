text = input("Enter a string: ")

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print("Character frequencies:")

for character, count in frequency.items():
    print(character, ":", count)
