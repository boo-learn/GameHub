# Задание:
# Разработать консольную игру «Крестики-нолики», в которой игрок играет против компьютера.
from dataclasses import field
import random

# Требования:

# 1. Игровое поле:
#   Создать игровое поле 3x3, которое будет отображаться в консоли.
#   Игровое поле должно быть представлено в виде списка списков или двумерного массива.
# 2. Отображение поля:
#   Реализовать функцию, которая будет выводить текущее состояние игрового поля в консоль..
# 3. Ввод хода игрока:
#   Реализовать функцию, которая будет запрашивать у игрока координаты клетки для хода.
#   Координаты должны быть представлены в виде двух чисел (номер строки и номер столбца).
# 4. Необходимо реализовать проверку корректности ввода:
#   Координаты должны быть в диапазоне от 1 до 3.
#   Клетка должна быть свободной.
# 5. Ход компьютера:
#   Реализовать функцию, которая будет определять ход компьютера.
#   Компьютер должен делать ход на свободную клетку.
#   Реализовать простой ИИ (например, случайный ход или попытка заблокировать победу игрока).
# Игроки должны ходить по очереди.
# 6. Проверка победы:
#   Реализовать функцию, которая будет проверять, есть ли победитель на текущем поле.
#   Проверка должна осуществляться по горизонталям, вертикалям и диагоналям.
# 7. Проверка ничьей:
#   Реализовать функцию, которая будет проверять, есть ли ничья (все клетки заполнены, но победителя нет).

# Основная игровая логика:
# Реализовать главную функцию, которая управляет ходом игры:
# Отображает игровое поле.
# Запрашивает ходы у игроков.
# Выполняет ходы.
# Проверяет победу или ничью.
# Выводит результаты игры.

# Примеры, которыми можно воспользоваться:
# game_field = [
#     ["X", "X", "O"],
#     [" ", "O", "X"],
#     ["O", " ", "X"],
# ]
#
# for line in game_field:
#     print(" ".join(line))
#
# print("------")
# step:
# game_field[1][0] = "X"
# for line in game_field:
#     print(" ".join(line))

moves_number = 0
field = []
for _ in range(3):
    row = []
    for _ in range(3):
        row.append(" ")
    field.append(row)


def print_field():
    for line in field:
        print(" ".join(line))
        print("------")


def move_checking(x, y):
    global moves_number
    if x in range(1, 4) and y in range(1, 4) and field[x - 1][y - 1] == " ":
        moves_number += 1
        return True
    return False


def player_move():
    while True:
        x = int(input("Введите номер строки (от 1 до 3) "))
        y = int(input("Введите номер колонки (от 1 до 3) "))
        if move_checking(x, y):
            field[x - 1][y - 1] = "X"
            break
        else:
            print("Неправильный ввод (значения должны быть от 1 до 3 и не повторяться) !")


def computer_move():
    while True:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if move_checking(x, y):
            field[x - 1][y - 1] = "0"
            break


def check_winner_combination(symbol):
    if field[0][0] == field[1][1] == field[2][2] == symbol or \
            field[0][2] == field[1][1] == field[2][0] == symbol or \
            field[0][0] == field[0][1] == field[0][2] == symbol or \
            field[1][0] == field[1][1] == field[1][2] == symbol or \
            field[2][0] == field[2][1] == field[2][2] == symbol or \
            field[0][0] == field[1][0] == field[2][0] == symbol or \
            field[1][0] == field[1][1] == field[1][2] == symbol or \
            field[2][0] == field[2][1] == field[2][2] == symbol:
        return True
    return False


def check_winner():
    if check_winner_combination("X"):
        return "Победил игрок"
    elif check_winner_combination("0"):
        return "Победил компьютер"
    return False


while True:
    player_move()
    print_field()
    if moves_number == 9:
        print("Ничья")
        break
    computer_move()
    print_field()
    result = check_winner()
    if result:
        print(result)
        break
    else:
        print("Для выхода нажмите Ctrl + D")
