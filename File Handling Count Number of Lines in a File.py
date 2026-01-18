filename = input("Enter file name: ")

file = open(filename, "r")
lines = file.readlines()
file.close()

print("Number of lines:", len(lines))
