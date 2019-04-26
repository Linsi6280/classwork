# 1
word = str(input("Enter a word: "))
for char in word:
    if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
        print(char)

# 2
numbers = [1, 22, 15, 991]
for num in numbers:
    if num > 10:
        print(num)

# 3
numbers = [1, 22, 15, 91, 467]
maximum = 0
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)

# 4
name = "Frank"
for i in range(len(name)):    # length of name is 5
    print(f"index: {i}, char: {name[i]}")
