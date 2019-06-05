import re
is_palindrome = input("Please enter text to be checked for palindrome status: ")
lower_palindrome = is_palindrome.lower()
clean_palindrome = re.sub(r'[^A-Za-z]', '', lower_palindrome)
i = len(clean_palindrome)
reverse_word = []

while i > 0:
    reverse_word.append(clean_palindrome[i - 1])
    i -= 1

nolist = ' '.join(reverse_word)
clean_reverse = re.sub(r'[^A-Za-z]', '', nolist)

if clean_palindrome == clean_reverse:
    print(is_palindrome + " is a palindrome")
else:
    print (is_palindrome + " is not a palindrome")