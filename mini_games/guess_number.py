# Игра: Угадай число

# Используя модуль `random`, напишите программу, которая случайным образом выбирает число от 0 до 100.
# У пользователя есть 6 попыток, чтобы угадать это число. Если пользователь угадывает число,
# выводится сообщение об успехе: "Отлично! Вы угадали число … с … попытки!". Если не угадывает за 6 попыток,
# выводится сообщение о неудаче: “К сожалению, вы не угадали число. Загаданное число было: …”.

# В конце программы должны выводиться все попытки пользователя и загаданное число.

# По ходу игры после каждой попытки пользователя компьютер выводит сообщение, было ли число пользователя
# больше или меньше загаданного числа: "Загаданное число больше.", "Загаданное число меньше." соответственно.

from random import randint


def guess_num_start():
    turns = 6
    while turns != 0:
        user_choice = int(input('Ваше предположение? '))
        comp_choice = randint(0, 100)
        if user_choice == comp_choice:
            print(f'Поздравляю вы угадали {comp_choice} за {6 - turns + 1} попыток!')
            break
        else:
            turns -= 1
            if turns > 0:
                print("Упс! Попробуйте еще раз")
                print(f'У вас осталось {turns} попыток!')
                if comp_choice > user_choice:
                    print("Загаданное число больше")
                else:
                    print("Загаданное число меньше")

            else:
                print('Вы проиграли!')
                print(f"Загаданное число было {comp_choice}")


if __name__ == "__main__":
    guess_num_start()
