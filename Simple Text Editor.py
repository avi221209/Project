while True:
    choice = input("Do you want to OPEN or CREATE a file? ").lower()

    if choice == "open":
        filename = input("Enter filename to open: ")

        try:
            with open(filename, "r") as f:
                print("\n--- File Content ---")
                print(f.read())
        except FileNotFoundError:
            print("File not found.")
            continue

    elif choice == "create":
        filename = input("Enter new filename: ")
        print("New file created.")

    else:
        print("Invalid choice")
        continue

    print("\nStart editing the file.")
    print("Type SAVE to save and exit.\n")

    content = ""

    while True:
        line = input()
        if line == "SAVE":
            break
        content += line + "\n"

    with open(filename, "w") as f:
        f.write(content)

    print("File saved successfully.")
    break