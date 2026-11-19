import sys

# Function to check palindrome
def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


# Accept input from command line or keyboard
if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("Enter a string: ")

# Display result
if palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")