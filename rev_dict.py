# Reverse a Dictionary
# Question: Write a function to reverse the dictionary

# -----------------------------------------------------------
# Reversing of complete dictionary along with keys and values 

def reverse_dictionary_order(original_dict):
    reversed_items = list(original_dict.items())[::-1]
    reversed_dict = dict(reversed_items)
    return reversed_dict

def display_dict(d, title):
    print(title)
    for key, value in d.items():
        print(f"{key}: {value}")
    print()

def main():
    original_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }

    display_dict(original_dict, "Original Dictionary:")
    reversed_dict = reverse_dictionary_order(original_dict)
    display_dict(reversed_dict, "Reversed Dictionary:")

if __name__ == "__main__":
    main()


# Reversing of the keys and values pairs 

"""
def reverse_dictionary(original_dict):
    reversed_dict = {value: key for key, value in original_dict.items()}
    return reversed_dict

def display_dict(d, title):
    print(title)
    for key, value in d.items():
        print(f"{key}: {value}")
    print()

def main():
    original_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }

    display_dict(original_dict, "Original Dictionary:")
    reversed_dict = reverse_dictionary(original_dict)
    display_dict(reversed_dict, "Reversed Dictionary:")

if __name__ == "__main__":
    main()
"""