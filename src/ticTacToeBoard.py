theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'down-L': ' ', 'down-M': ' ', 'down-R': ' '}

def printBoard(brd):
    print(brd['top-L'] + '|' + brd['top-M'] + '|' + brd['top-R'])
    print('___________')

    print(brd['mid-L'] + '|' + brd['mid-M'] + '|' + brd['mid-R'])
    print('___________')

    print(brd['down-L'] + '|' + brd['down-M'] + '|' + brd['down-R'])

turn = 'X'

for i in range(9):
    printBoard(theBoard)

    print('Turn for ' + turn + '. Move to which space?')

    move = input()

    theBoard[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
    
