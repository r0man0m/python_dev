# Завдання 2
#
# Створіть програму, яка перевіряє, чи є паліндромом введена фраза.

def is_palindrome(input_text):
    reversed_text = input_text[::-1]
    if reversed_text == input_text:
        return True
    else:
        return False


def main():
   print('Palindrome') if is_palindrome(input('Input text: ')) else print('Not Palindrome')

main()