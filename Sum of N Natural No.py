# Function to calculate the sum of first N natural numbers
def sum_of_n(n):
    total = 0                 # Variable to store the sum

    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        total += i            # Add current number to total

    return total              # Return the final sum


# Taking input from the user
n = int(input("Enter a natural number: "))

# Checking whether the input is valid
if n < 0:
    # Natural numbers are positive
    print("Please enter a positive number.")
else:
    # Calling the function and storing the result
    result = sum_of_n(n)

    # Displaying the result
    print("Sum of first", n, "natural numbers is:", result)
