game_zone = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]


def show_zone():  #функция отображения поля на текущий момент
    print(f'  │ 0 │ 1 │ 2 │')
    print('--│------------')
    print(f'0 │ {game_zone[0][0]} │ {game_zone[0][1]} │ {game_zone[0][2]} │')
    print('  -------------')
    print(f'1 │ {game_zone[1][0]} │ {game_zone[1][1]} │ {game_zone[1][2]} │')
    print('  -------------')
    print(f'2 │ {game_zone[2][0]} │ {game_zone[2][1]} │ {game_zone[2][2]} │')
    print('  -------------')


def step_player1(): #ход первого игрока с проверкой занятности и диапазона
    while True:
        step = input('Введите две координаты через пробел: ').split()
        if not len([i for i in step if i in '012']) == 2:
            print('Введите только два числа от 0 до 2: ')
            continue
        x, y = list(map(int, step))
        if 0 <= x <= 2 and 0 <= y <= 2:
            if game_zone[x][y] == ' ' and game_zone[x][y] != '0':
                return x, y
            else:
                print('Клетка занята! ')


def step_player2(): #ход второго игрока с проверкой занятности и диапазона
    while True:
        step = input('Введите две координаты через пробел: ').split()
        if not len([i for i in step if i in '012']) == 2:
            print('Введите только два числа от 0 до 2: ')
            continue
        x1, y1 = list(map(int, step))
        if 0 <= x1 <= 2 and 0 <= y1 <= 2:
            if game_zone[x1][y1] == ' ' and game_zone[x1][y1] != 'x':
                return x1, y1
            else:
                print('Клетка занята! ')


def printing_stepPlayer1(): # функция печати хода первого игрока
    x, y = step_player1()
    game_zone[x][y] = 'x'


def printing_stepPlayer2():
    x1, y1 = step_player2()
    game_zone[x1][y1] = '0'



def chek_winning():
    if game_zone[0] == ['x', 'x', 'x']:
        print('Игра окончена! Выйграл крестик! ')
        return True
    elif game_zone[0] == ['0', '0', '0']:
        print('Игра окончена! Выйграл нолик! ')
        return True
    elif game_zone[1] == ['x', 'x', 'x']:
        print('Игра окончена! Выйграл крестик!')
        return True
    elif game_zone[1] == ['0', '0', '0']:
        print('Игра окончена! Выйграл нолик!')
        return True
    elif game_zone[2] == ['x', 'x', 'x']:
        print('Игра окончена! Выйграл крестик!')
        return True
    elif game_zone[2] == ['0', '0', '0']:
        print('Игра окончена! Выйграл нолик!')
        return True
    elif game_zone[0][0] == 'x' and game_zone[1][0] == 'x' and game_zone[2][0] == 'x':
        print('Игра окончена! Выйграл крестик!')
        return True
    elif game_zone[0][0] == '0' and game_zone[1][0] == '0' and game_zone[2][0] == '0':
        print('Игра окончена! Выйграл нолик!')
        return True
    elif game_zone[0][0] == game_zone[1][1] == game_zone[2][2] == 'x' or game_zone[0][2] == game_zone[1][1] == \
            game_zone[2][0] == 'x':
        print('Игра окончена! победил крестик!')
        return True
    elif game_zone[0][0] == game_zone[1][1] == game_zone[2][2] == '0' or game_zone[0][2] == game_zone[1][1] == \
            game_zone[2][0] == '0':
        print('Игра окончена! Победил нолик!')
        return True
    elif game_zone[0][0] !=' ' and game_zone[0][1] !=' ' and game_zone[0][2] !=' ' and game_zone[1][0] !=' ' and game_zone[1][1] !=' ' and game_zone[1][2] !=' ' and game_zone[2][0] !=' ' and game_zone[2][1] !=' ' and game_zone[2][2] != ' ':
        print('Игра окончена! Ничья!')
        return True
    elif game_zone[0][1] == 'x' and game_zone[1][1] == 'x' and game_zone[2][1] == 'x':
        print('Игра окончена! Выйграл крестик!')
        return True
    elif game_zone[0][1] == '0' and game_zone[1][1] == '0' and game_zone[2][1] == '0':
        print('Игра окончена! Выйграл нолик!')
        return True
    elif game_zone[0][2] == 'x' and game_zone[1][2] == 'x' and game_zone[2][2] == 'x':
        print('Игра окончена! Выйграл крестик!')
        return True
    elif game_zone[0][2] == '0' and game_zone[1][2] == '0' and game_zone[2][2] == '0':
        print('Игра окончена! Выйграл нолик!')
        return True

show_zone()
count = 0
while True:
    if count % 2 == 0:
        printing_stepPlayer1()
        count += 1
        show_zone()
        if chek_winning():
            break

    else:
        printing_stepPlayer2()
        count += 1
        show_zone()
        if chek_winning():
            break


