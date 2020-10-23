import os
import time
from platform import system as system_name


def clear():
    if system_name().lower() == 'windows':
        os.system('cls')
    else:
        os.system('clear')


gameB = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']


def displayB():
    txt = ''
    txt += ('Tic Tac Toe\n{}\n'.format('-'*11))
    for i in range(1, 10):
        txt += (gameB[i-1]+' '*3)
        if i/3 in [1, 2, 3]:
            txt += ('\n{}   {}   {}\n\n'.format(str(i-2), str(i-1), str(i)))
    return txt


def checker():
    if ['X', 'X', 'X'] in [gameB[0:3], gameB[3:6], gameB[6:9], ([gameB[0], gameB[3], gameB[6]]), ([gameB[1], gameB[4], gameB[7]]), ([gameB[2], gameB[5], gameB[8]]), ([gameB[0], gameB[4], gameB[8]]), ([gameB[2], gameB[4], gameB[6]])]:
        return 1
    if ['O', 'O', 'O'] in [gameB[0:3], gameB[3:6], gameB[6:9], ([gameB[0], gameB[3], gameB[6]]), ([gameB[1], gameB[4], gameB[7]]), ([gameB[2], gameB[5], gameB[8]]), ([gameB[0], gameB[4], gameB[8]]), ([gameB[2], gameB[4], gameB[6]])]:
        return 0


def play1():
    place = input(player1+'\nWhere would you like to enter \'X\'?\nInput: ')
    if gameB[int(place)-1] == '_':
        gameB[int(place)-1] = 'X'
    else:
        print('Cheater!\n You have lost your turn')
        time.sleep(1)


def play2():
    place = input(player2+'\nWhere would you like to enter \'O\'?\nInput: ')
    if gameB[int(place)-1] == '_':
        gameB[int(place)-1] = 'O'
    else:
        print('Cheater!\n You have lost your turn')
        time.sleep(1)


def final():
    if '_' not in gameB:
        return 1
    pass


print('\nTic Tac Toe\n{}\n'.format('-'*11))
player1 = input('Enter player one name: ').capitalize()
player2 = input('Enter player two name: ').capitalize()
order = input(
    f'\nEnter 1 if {player1} goes first \nEnter 2 if {player2} goes first\nEnter here: ')


# while True:
#     try:
#         if order == '1':
#             clear()
#             print(displayB())
#             play1()
#             if checker() in [0, 1]:
#                 break
#             clear()
#             print(displayB())
#             play2()
#             if checker() in [0, 1]:
#                 break
#         else:
#             clear()
#             print(displayB())
#             play2()
#             if checker() in [0, 1]:
#                 break
#             clear()
#             print(displayB())
#             play1()
#             if checker() in [0, 1]:
#                 break
#     except:
#         print('Error')
#         break
while True:
    if order == '1':
        clear()
        print(displayB())
        play1()
        if checker() in [0, 1] or final() == 1:
            break
        clear()
        print(displayB())
        play2()
        if checker() in [0, 1]:
            break
    else:
        clear()
        print(displayB())
        play2()
        if checker() in [0, 1] or final() == 1:
            break
        clear()
        print(displayB())
        play1()
        if checker() in [0, 1]:
            break
    if final() == 1:
        break

clear()
if checker() == 0:
    print(f'{player2} won this match!')
if checker() == 1:
    print(f'{player1} won this match!')
if checker() not in [0, 1]:
    print('It was a tie!')
print('Program Finished')
