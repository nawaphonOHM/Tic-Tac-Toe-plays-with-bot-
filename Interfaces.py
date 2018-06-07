import os
import random

def OX():
    O = set()
    X = set()
    
    while True:
        while True:
            printedTable(O, X)
            move = input("Choose position [1-9]\n")
            move = int(move)
            if move not in O and move not in X and move > 0:
                break
            else:
                print("idiot move!", end = "")
        O |= {move}
        if isWin(O):
            printedTable(O, X)
            print("\nYou win! senpai")
            break
        elif isDraw(O, X):
            printedTable(O, X)
            print("We draw!")
            break
        X |= AImoves(X, O)
        if isWin(X):
            printedTable(O, X)
            print("\nI win! Baka..")
            break
        elif isDraw(O, X):
            printedTable(O, X)
            print("We draw!")
            break

def isDraw(O, X):
    return O.union(X) == {x for x in range(1, 10)}

def isWin(input):
    windicts = {
        "1": {1, 2, 3}, 
        "2": {4, 5, 6}, 
        "3": {7, 8, 9}, 
        "4": {1, 4, 7}, 
        "5": {2, 5, 8}, 
        "6": {3, 6, 9}, 
        "7": {1, 5, 9}, 
        "8": {3, 5, 7}
    }

    for value in windicts.values():
        if value - input == set():
            return True
    return False

def AImoves(X, O):
    score = -100
    move = 0
    if X > set():
        allmove = {x for x in range(1, 10)}.difference(X | O)
        for i in allmove:
            newscore = evaluateScore(i, O, X)
            if newscore > score:
                score = newscore
                move = i
    else:
        x = [x for x in range(1, 10)]
        x.remove(*O)
        x = random.sample(x, 1)
        for i in x:
            move = i
    return {move}

def evaluateScore(element, O, X):
    probalitywalkpaths = {
        "1": {1, 2, 3}, 
        "2": {4, 5, 6}, 
        "3": {7, 8, 9}, 
        "4": {1, 4, 7}, 
        "5": {2, 5, 8}, 
        "6": {3, 6, 9}, 
        "7": {1, 5, 9}, 
        "8": {3, 5, 7}
    }
    newscore = 1
    for value in probalitywalkpaths.values():
        if element in value and value - O == value:
            newscore = newscore + 1
    for i in O:
        for value in probalitywalkpaths.values():
            if i in value and (value - X) - {element} == value:
                newscore = newscore - 1
    return newscore

def printedTable(O, X):
    os.system("cls")
    for i in range(9):
        if i % 3 == 0:
            print("\n")
        i = i + 1
        if i in O:
            print("O", end = "\t")
        elif i in X:
            print("X", end = "\t")
        else:
            print(i, end = "\t")
    print("\n")


OX()