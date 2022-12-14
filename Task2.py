# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
#  Играют два игрока делая ход друг после друга. 
#  Первый ход определяется жеребьёвкой. 
#  За один ход можно забрать не более чем 28 конфет. 
#  Все конфеты оппонента достаются сделавшему последний ход. 
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint, shuffle

print('Выберите режим: ')
print('1. 2 игрока')
print('2. С ботом (глупый)')
print('3. С ботом (умный)')
game_mode = int(input(': '))

player_count = [int(x+1) for x in range(2)]
shuffle(player_count)
candy_count = 2021
log_test = []

def mode_algorithm_1(player_count): 
    s_value = input(f'Введите число от 1 до 28: ')
    if (s_value == ''):
        print ('Не верный ход!')
        return 0

    turn_value = int(s_value)
    if 0 < turn_value < 29:
        player_count.insert(0, player_count.pop())
        return turn_value

    print ('Не верный ход!')
    return 0


def mode_algorithm_2(player_count): 
    turn_value = randint(1,28)
    print ('Игрок № ', player_count[0], ' выбрал: ', turn_value)
    player_count.insert(0, player_count.pop())
    return turn_value


def mode_algorithm_3(player_count, candy): 
    turn_value = candy - (candy//29*29)
    if turn_value == 0: turn_value = randint(1,28)
    print ('Игрок № ', player_count[0], ' выбрал: ', turn_value)
    player_count.insert(0, player_count.pop())
    return turn_value


while candy_count > 28:
    print('\nНа столе ', candy_count, 'конфет')
    print ('Ходит игрок №: ', player_count[0])
    
    if game_mode == 1:
        candy_count -= mode_algorithm_1 (player_count)

    elif game_mode == 2:
        if player_count[0] == 1:
            candy_count -= mode_algorithm_1 (player_count)
        else: candy_count -= mode_algorithm_2 (player_count)

    elif game_mode == 3:
        if player_count[0] == 1:
            candy_count -= mode_algorithm_1 (player_count)
        else: candy_count -= mode_algorithm_3 (player_count, candy_count)

    elif game_mode == 4:
        log_test.append('p = ' +str(player_count[0]) +'; c = ' +str(candy_count))
        if player_count[0] == 1:
            candy_count -= mode_algorithm_2 (player_count)
        else: candy_count -= mode_algorithm_3 (player_count, candy_count)
        
    else: 
        print ('Ошибка! Не верный режим')
        break

print(f'\nПобеда! Игрок № {player_count[0]}')

