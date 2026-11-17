# Program to check whether a string is palindrome

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


# Accept input from user
text = input("Enter a string: ")

if palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")