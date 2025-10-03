def count_letters(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("No. of uppercase characters:", upper)
    print("No. of lower case characters:", lower)

# Example usage:
text = "AbcdefgHijklmnopqrstuvwxyzab"
count_letters(text)
