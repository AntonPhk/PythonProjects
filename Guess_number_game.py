# This is mini project, witch realise a game.
# In these game you need find what number was guessed.

from random import randrange
def number_god_game():
  print('Добро пожаловать в числовую угадайку')
  a_border = int(input("Введите границу числового диапазона: "))
  print(f"Введите число в диапазоне от 1 до {a_border}, которое, вероятно, загадали")
  a = randrange(a_border)
  compare_num(input(), a, a_border)

def is_valid(num, a_border):
  while 0 > int(num) or int(num) > a_border:
    print(f'А может все-таки введем целое число от 1 до {a_border}?')
    num = input()
  return (int(num))

def compare_num(field, a, a_border):
  num = is_valid(field, a_border)
  count = 1
  while num != a:
    if num < a:
      print('Ваше число меньше загаданного, попробуйте еще разок')
    elif num > a:
      print('Ваше число больше загаданного, попробуйте еще разок')
    num = is_valid(input(), a_border)
    count += 1
  print(f'Вы угадали c {count} раза, поздравляем! \nСпасибо, что играли в числовую угадайку. Еще увидимся...')


number_god_game()