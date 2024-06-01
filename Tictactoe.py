import random

print("Welcome to TTT!")
poss_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
col = 3

def printgameBoard():
    for i in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for j in range(col):
            print(f" {gameBoard[i][j]} ", end="|")
    print("\n+---+---+---+")

def modifygameBoard(num, turn):
    num -= 1
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn

def CheckforWinner(gameBoard):
    # Check rows
    for row in gameBoard:
        if row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for col in range(3):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col]:
            return gameBoard[0][col]

    # Check diagonals
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        return gameBoard[0][2]

    # Check for draw
    if all(isinstance(cell, str) for row in gameBoard for cell in row):
        return "Draw"

    return None

def main():
    leaveloop = False
    turnCounter = 0

    printgameBoard()
    while not leaveloop:
        if turnCounter % 2 == 1:
            numPicked = int(input("Enter a number [1-9]: "))
            if numPicked in poss_num:
                modifygameBoard(numPicked, "X")
                poss_num.remove(numPicked)
                turnCounter += 1
            else:
                print("Invalid number")
        else:
            while True:
                cpuChoice = random.choice(poss_num)
                print("CPU Choice:", cpuChoice)
                if cpuChoice in poss_num:
                    modifygameBoard(cpuChoice, "O")
                    poss_num.remove(cpuChoice)
                    turnCounter += 1
                    break

        printgameBoard()
        result = CheckforWinner(gameBoard)
        if result:
            if result == "X":
                print("You win")
            elif result == "O":
                print("You lose")
            elif result == "Draw":
                print("It's a draw")
            leaveloop = True
if __name__ == "__main__":
    main()