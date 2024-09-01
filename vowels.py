# Read the input string
input_string = input("Enter String: ")

# Initialize the counter for vowels
vowel_count = 0

# Initialize the index for the while loop
index = 0

# Set of vowels in lowercase latin letters
vowels = {'a', 'e', 'i', 'o', 'u'}

# Use while loop to iterate through the string
while index < len(input_string):
    if input_string[index] in vowels:  
        vowel_count += 1               
    index += 1                   

# Output the count of vowels
print(vowel_count)
