import os

if not os.path.exists('res/learn.keras'):
    print('Run res/train.py file!')
    exit()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import random
import time
from tensorflow import keras
import pandas as pd

model = keras.models.load_model('res/learn.keras')


def guess(lst_):
    new_data = pd.DataFrame([lst_], columns=['a', 'b', 'c'])
    return model.predict(new_data)


def print_tik():
    os.system('clear')  # cls for windows
    print('AI [O] - User [X]')
    print(f"\n\n  {board[1]}  |  {board[2]}  |  {board[3]} ")
    print(f"_____|_____|______")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print(f"_____|_____|______")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]} ")
    print(f"     |     |      \n")


def checkWin():
    for loopCheckWin in [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [7, 8, 9], [4, 5, 6], [3, 5, 7]]:
        if board[loopCheckWin[0]] == board[loopCheckWin[1]] == board[loopCheckWin[2]]:
            return True

    return None if len([x for x in board if type(x) is int and x != 0]) != 0 else False


def tryWinAI(m):
    global board
    max_prediction = 0
    index = 0
    for ijm in [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [7, 8, 9], [4, 5, 6], [3, 5, 7]]:
        gb = []
        for imn in ijm:
            jn = 1
            if board[imn] == 'O':
                jn = 0.5
            elif board[imn] == imn:
                jn = 0
            gb.append(jn)
        temp = guess(gb)
        if temp > max_prediction:
            max_prediction = temp
            index = ijm
    print('Selected index => ', index)
    ij = [x for x in index if type(board[x]) is int]
    if not len(ij):
        return True
    board[ij[0]] = m


def AIPlayNow(m):
    global board
    if tryWinAI(m):
        # if you want to win by any chance, below code is yrs.
        ij = [x for x in board if type(x) is int and x != 0]
        if not len(ij):
            return
        _p = random.choice(ij)
        board[_p] = m


board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def writeRow():
    hgb = []
    for ijm in [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [7, 8, 9], [4, 5, 6], [3, 5, 7]]:
        gb = []
        for imn in ijm:
            jn = 1
            if board[imn] == 'O':
                jn = 0.5
            elif board[imn] == imn:
                jn = 0
            gb.append(jn)
        hgb.append(gb)
    print(hgb)


def play():
    for k in range(10):
        for im in trn:
            if im % 2 == 0:
                def inp():
                    try:
                        user_inp_value = int(input(f"Your Choice [X]: "))
                        if user_inp_value > 9 or user_inp_value < 1:
                            raise ValueError
                        if board[user_inp_value] != user_inp_value:
                            raise ValueError
                    except ValueError:
                        print("You Stupid.. Try again...")
                        return inp()
                    return user_inp_value

                inp_ = inp()
                board[inp_] = 'X'
            else:
                AIPlayNow('O')
            print_tik()
            jm = checkWin()
            if jm:
                print('Won:', 'AI' if im % 2 != 0 else 'USER')
                return
            elif jm is not None:
                print('Tie: AI vs USER')
                return


# trn = [2, 1]
trn = [1, 2]  # Didn't want to win? Use this line

for i in range(10):
    print_tik()
    play()

    # Resetting variable data
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # To check log
    time.sleep(2)
