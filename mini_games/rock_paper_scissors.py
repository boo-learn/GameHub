# Игра: Камень, ножницы, бумага

# Создайте игру "Камень, ножницы, бумага", где пользователь играет против компьютера.
# Компьютер случайным образом выбирает одно из трех значений: камень, ножницы или бумагу.
# Пользователь вводит свой выбор, и программа определяет победителя. Если выборы одинаковы, игра объявляет ничью.
# Игра продолжается до тех пор, пока один из игроков (пользователь или компьютер)
# не одержит на три победы больше, чем соперник. В конце показывается итоговый счет и объявляется победитель.

import random


def computer_choice():
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)


def player_choice():
  user_choice = input("Выбор : камень, ножницы, бумага")
  return user_choice




def games():
    if player_choice == computer_choice():
        print(f"player_choice: {player_choice}, computer_choice: {computer_choice()} НИЧЬЯ!!!")

    elif (player_choice == ('камень') and computer_choice == ('ножницы') or player_choice == ('ножницы') and
          computer_choice == ('бумага') or player_choice('бумага') and computer_choice('камень')):
        return "Вы Выйграли!!"

    else:
     return "Компьютер выйграл!!! "

def play():
    print("Игра КНБ ")

