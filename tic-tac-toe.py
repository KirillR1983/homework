# def drow_area(): # def - это отдельная функция (drow_area - это переменная функции def) для чтобы отрисовывать
#                  # поле в любой момент несколько раз (например после каждого действия) после каждого хода игрока
#                  # (наше поле - это area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']] и этот код:
#                  # for i in area:
#                  #     print(*i) - добавили в функцию def
#     for i in area:  # цикл for и его переменная i (а *in - указывает последовательность (это может быть
#         # переменная, список, кортеж или последовательность чисел))  - это цикл кот-ый перебирает
#         # все элементы в основной переменной (смотря что указано после *in) (указанной после in)
#         print(*i)  # чтобы вывести каждый эл-нт из списка основной перем-ой нужно в print указать перем-ую
#         # цикла for (i) - чтобы избавиться от квадр-ых скобок, нужно пост-ть перед перем-ой 'i' '*'
#         # '*' - оператор распаковки
#     print() # добавляем пустой принт для отделения полей после каждого хода
# area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# print("Добро пожаловать в крестики-нолики!") # - добавили приветствия для красоты
# print("-----------------------------------") # - добавили пунктир для отделения приветствия от поля для красоты
# drow_area() # если мы вызываем фун-ию переменную функции (def) drow_area мы получаем игровое поле
# # print(area[0][0]) # особенность списка в том что мы можем обращаться к элементам списка, можем перебирать и
#                   # менять их, а так же менять элементы в самих элементах списка)
# # area[0][0] = "X" # первое значение "[0]" - отвечает за ряд в игре (элемент в списке), а
#                  # второе значение "[0]" - отвечает за колонку в игре (элемент в каждом элементе списка)
# # чтобы дать пользователю возможность ставить знак мы вводи две переменные "row" и "column"
# row = int(input("Введите номер строки (1,2,3)")) - 1 # добавляем "-1" так как при вводе пользователем номера
# column = int(input("Ведите номер столбца (1,2,3)")) - 1 # строки или столбца идёт обращение к индексу элемента в
#                                             # списке и элемету списка в списке и для этого добавляем в строку "-1"
#                                             # (отсчёт индекса элемента всегда и везде начинается с "0")
# area[row][column] = "X" # есть миоё игровое поле area и я достаю из такой-то строки [row] и
#                         # из такой-то столбца (колонны) [column] и меняю его на "Х"
# # есть проблема, которая заключается в том, что нам нужно менять значения на "Х" и на "0" и программа должна
# # повторяться не один раз - значит мы можем использовать цикл и условия для определения того кто сейчас ходит,
# # это мы можем реализовывать с помощью цикла While (выглядит самым очевидным)
# # и с помощью цикла for - делаем именно с ним (см. ниже!!!)
# drow_area()
# print()
# print()


# def drow_area():
#     for i in area:
#         print(*i)
# print()
# area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# print("Добро пожаловать в крестики-нолики!")
# print("-----------------------------------")
# drow_area()
# for turn in range(1, 10): # создаём цикл for на 9 повторений и здесь обозначим переменную "i" - "turn"
#     # и операясь на неё мы можем реализовать смену игрока (кто ходит), т.е. "turn" - будет определяющим фактом)
#     print(f'Ход: {turn}') # выводим информацию с помощью f строки (f строка помогает обращаться к переменным
#     # внутри строки, для этого нам нужно прописать {} скобочки и f перед началом строки (в фигурных скобках
#     # можем обращаться к любым переменным (значениям)), нужна переменная turn)
#     if turn % 2 == 0: # если наш ход чётный без остатка делится на 2,
#         turn_char = '0' # то переменная turn_charm = "0"
#         print("Ходят нолики") # выводим информацию - ходят нолики
#     else: # в другом случае, если ход не чётный (не делится на 2 без остатка),
#         turn_char = 'X' # то переменная turn_charm = "Х"
#         print("Ходят крестики")
#     row = int(input("Введите номер строки (1,2,3)")) - 1
#     column = int(input("Ведите номер столбца (1,2,3)")) - 1
# # area[row][column] = "X" - чтобы реализовать эту смену, нам нужно проверять чей сейчас ход ("Х" или "0"),
# # первыми обычно ходят "Х" !!! (нечётный ход), вторыми "0" (четный ход) - значит нужно ввести особую переменную
#     # которая будет принимать значение того, кто сейчас ходит, и в зависимости от хода (чётный или не чётный)
#     # мы будем устанавливать значение переменной с помощью if (см. выше!!!)
#     if area[row][column] == "*": # если в нашем поле в такой-то строке и в таком-то столбце находится
#         # "*" (список состоит из списков со "*"), то в таком случае ставится символ того кто сейчас ходит
#         area[row][column] = turn_char # turne - переменная хода, turn_char - переменная очереди хода игроков
#     else: # в другом случае если ячейка занята выводится "Ячейка уже занята, ... "
#         print("Ячейка уже занята, вы пропускаете ход")
#         drow_area() # прописывается для отрисовки поля после каждого хода
#         continue # команда цикла которая возвращает к началу цикла
#     drow_area()


# проверка занятость ячейки в процессе игры 'X', '0' или '*'
def chek_winner(): # возвращающая функция, если её вызывать, о она оставляет какое-либо значение if
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
        return '0'
    if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
        return 'X'
    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return 'X'
    if area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0':
        return 'X'
    if area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0':
        return '0'
    if area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0':
        return '0'
    return '*'


def drow_area():
    for i in area:
        print(*i)
print()
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print("Добро пожаловать в крестики-нолики!")
print("-----------------------------------")
drow_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print("Ходят нолики")
    else:
        turn_char = 'X'
        print("Ходят крестики")
    row = int(input("Введите номер строки (1,2,3)")) - 1
    column = int(input("Ведите номер столбца (1,2,3)")) - 1
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход")
        drow_area()
        continue
    drow_area()
    if chek_winner() == 'X':
        print("Победа крестиков")
        break # остановка цикла
    if chek_winner() == '0':
        print("Победа ноликов")
        break
    if chek_winner() == '*' and turn == 9:
        print("Ничья")
        break


