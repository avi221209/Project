numbers = list(map(int, input("Enter list elements: ").split()))
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("List without duplicates:", unique_list)