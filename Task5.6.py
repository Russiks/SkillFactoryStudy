print("=+" * 10, " Игра Крестики-нолики для двух игроков ver.1.1 ", "+=" * 10)  # Печатаем название программы
print("Правила игры:\n 1) Игру начинает Х \n 2) В поле \"Куда поставим?\" нужно ввести число свободной клетки "
      "\n 3) Выигрывает тот, кто первым выстроит в ряд 3 свои фигуры по вертикали, горизонтали или диагонали ")
field = list(range(1, 10))  # Создаем список чисел через функцию range от 1 до 10 (включительно 9)


def draw_field(field):  # Функция для отображения поля игры, в качестве аргумента добавляем "field" - список
    print()  # Создаем отступ от названия программы
    print("-" * 13)  # Оформляем начальное поле игры
    for i in range(3):  # С помощью цикла for создаем поле 3на3
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-" * 13)  # Оформляем разделение в поле игры


def take_input(player_input):  # Создаем функцию, которая будет принимать ввод пользователя через аргумент player_input
    valid = False  # Создаем переменную valid равную False
    while not valid:
        player_answer = input("Куда поставим " + player_input + "? ")  # Создаем переменную player_answer для ввода
        # пользователем значения
        try:  # Блок try…except используется для обработки некоренного ввода данных пользователем
            player_answer = int(player_answer)  # Приравниваем "player_answer" к целому числу
        except:  # Если ввод данных был некорректный, то игрок увидит надпись:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue  # Цикл переходит на новую итерацию с возможностью нового ввода данных
        if 1 <= player_answer <= 9:  # Если число введено не из диапазона от 1 до 9
            if str(field[player_answer - 1]) not in "XO":  # И если клетка уже занята
                field[player_answer - 1] = player_input  # Приравниваем "field[player_answer - 1]" к "player_input"
                valid = True  # В цикле читается как "not True"
            else:  # Если клетка занята, то игрок увидит надпись:
                print("Эта клетка уже занята!")
        else:  # Если значение ввода не в диапазоне, то игрок увидит надпись:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(field):  # Создаем функцию проверки игрового поля (аргумент "field")- выиграл или нет текущий игрок
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # Создаем
    # кортеж с вариантами выигрыша
    for every in win_coord:  # С помощью цикла "for" проверяем кортеж на наличие выигрышных вариантов
        if field[every[0]] == field[every[1]] == field[every[2]]:  # Проверяем, чтобы символы во всех трех заданных
            # клетках были равны
            return field[every[0]]  # Если клетки равны, возвращаем любой выигрышный вариант
    return False  # Иначе возвращаем False


def main(field):  # Создаем основную функцию
    counter = 0  # Переменная для счета очков
    win = False  # Переменная для обнаружения победителя
    while not win:
        draw_field(field)  # Определяем игрока
        if counter % 2 == 0:
            take_input("X")  # Первый игрок Х
        else:
            take_input("O")  # Второй игрок О
        counter += 1  # Создаем переменную "counter" (счетчик)
        if counter > 4:  # Проверяем, чтобы переменная counter стала больше 4, чтобы избежать заведомо ненужного
            # вызова функции check_win
            tmp = check_win(field)  # Создаем переменную "tmp" и привариваем к "check_win(field)" для того, чтобы не
            # вызывать постоянно функцию "check_win"
            if tmp:  # Если игрок выполнил выигрышной вариант, то вывести надпись:
                print(tmp, "победитель!")
                win = True  # win становится True
                break  # Игра завершается
        if counter == 9:  # Если counter равняется 9, то выводим надпись:
            print("Ничья!")
            break  # Игра завершается
    draw_field(field)  # Вызываем функцию для отображения поля игры


main(field)  # Вызываем основную функцию

input("Нажмите Enter для выхода!")
