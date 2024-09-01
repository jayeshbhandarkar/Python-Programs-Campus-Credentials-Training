def Carry(n1, n2):
    # Ensure n1 is the longer string
    if len(n1) < len(n2):
        n1, n2 = n2, n1  # Swap so that n1 is always longer

    # Reverse both strings to make addition easier from the least significant digit
    n1 = n1[::-1]
    n2 = n2[::-1]

    count = 0
    carry = 0

    # Iterate over the length of the longer number
    for i in range(len(n1)):
        # Get the current digit from n1 and n2, or 0 if out of range for n2
        digit1 = int(n1[i])
        digit2 = int(n2[i]) if i < len(n2) else 0

        # Calculate the sum of current digits and the carry
        temp = digit1 + digit2 + carry

        # If sum is 10 or greater, increment carry count and set carry to 1
        if temp >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

    return count

# Input two numbers as strings
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")

# Print the number of carry operations
print("Number of carry operations:", Carry(n1, n2))
