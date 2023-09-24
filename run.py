# Tic Tac Toe

xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
yState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1

def sum(a, b, c):
    return a + b + c


def printBoard(xState, yState):

    zero = 'X' if xState[0] else ('O' if yState[0] else " ")
    one = 'X' if xState[1] else ('O' if yState[1] else " ")
    two = 'X' if xState[2] else ('O' if yState[2] else " ")
    three = 'X' if xState[3] else ('O' if yState[3] else " ")
    four = 'X' if xState[4] else ('O' if yState[4] else " ")
    five = 'X' if xState[5] else ('O' if yState[5] else " ")
    six = 'X' if xState[6] else ('O' if yState[6] else " ")
    seven = 'X' if xState[7] else ('O' if yState[7] else " ")
    eight = 'X' if xState[8] else ('O' if yState[8] else " ")
    

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(xState, yState):
      
      wins = [0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [8, 4, 0], [6, 4, 2]

      for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        
        if(sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3):
            print("O Won the match")
            return 0

      return -1


def main():
   print('hello')
   turn = 1

   while(True):
        printBoard(xState, yState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Please enter a value: "))
            yState[value] = 1

        theWinner = checkWin(xState, yState)
        if(theWinner != -1):
            print('Match over')
            break
            
            

        turn = 1 - turn


main()