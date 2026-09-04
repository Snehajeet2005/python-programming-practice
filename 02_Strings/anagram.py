first = input("Enter first string: ")
second = input("Enter second string: ")

first = first.replace(" ", "").lower()
second = second.replace(" ", "").lower()

if len(first) != len(second):
    print("Not Anagram")
elif sorted(first) == sorted(second):
    print("Anagram")
else:
    print("Not Anagram")
