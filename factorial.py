# Read the input integer N
n = int(input("Enter any Number: "))

# Initialize the factorial variable
factorial = 1

# Initialize the loop counter
i = n

# Use while loop to calculate the factorial
while i > 0:
    factorial *= i  # Multiply factorial by the current value of i
    i -= 1          # Decrement i by 1

# Output the factorial
print("\nFactorial of",n ,"is",factorial)
