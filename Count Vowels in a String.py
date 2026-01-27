word = input("Enter a Word")
vowels = 0

for ch in word:
    if ch in "aeiou":
        count +=1

print("Number of Vowels:",count)