from string import digits, ascii_lowercase, ascii_uppercase
from random import choice


def safe_password_generator():
    result = []
    chars = digits + ascii_uppercase + ascii_lowercase
    passwords_count = int(input("Вы запустили генератор безопасных паролей. Какое колличество паролей вам нужно?\n"))
    password_length = int(input('Длина одного пароля:\n'))
    chars_in_passwords = input('Использовать неоднозначные символы "il1Lo0O"?(y/n)\n')
    if chars_in_passwords.lower() == 'y':
        chars += "il1Lo0O"
    for _ in range(passwords_count):
        password = ''
        for i in range(password_length):
            password += choice(chars)
        result.append(password)
    return print(*result)


safe_password_generator()
