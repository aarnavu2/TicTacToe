"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
APB = False

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    numX = 0  #how many Xs
    numO = 0  #how many Os
    playerTurn = None

    for row in board: #iterate through entire board
        for square in row:
            if square == "X": numX +=1
            elif square == "O": numO +=1

    if numX>numO: playerTurn = O     #if more Xs than Os its Os turn 
    elif numX <= numO: playerTurn = X #if more same Os than Xs, its Xs turn
    return playerTurn

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []
    currentAction = []
    rowNum = 0
    squareNum = 0

    for row in board:      #iterate through entire board
        squareNum = 0
        for square in row: 
            if not square:
                currentAction = [rowNum, squareNum]
                possibleActions.append(currentAction)
            squareNum+=1
        rowNum +=1

   
    return possibleActions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """


    turn = player(board) 
    
    board[action[0]][action[1]] = turn    
    return board


    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None

    for row in board:   #checks rows for winner
        if row == [X, X, X]:
            winner = X
            return winner
        elif row == [O,O,O]:
            winner = O
            return winner
         
    for column in range(3):  #checks columns for winnner
        if board[0][column] == board[1][column] and board[1][column] == board[2][column]:
            winner = board[0][column]
            return winner

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: #checks top down diagonal
        winner = board[0][0]
        return winner

    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        winner = board[2][0]
        return winner

    return winner

            

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    
    
    else:
        
        for row in board:
            for square in row:
               
                if square == None:
                   # print("not terminal")
                    return False
   # print("terminal")
    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


    raise NotImplementedError




class actionValue():
    def __init__(self, action, val, parentAction):
        self.action = action
        self.val = val
        self.parentAction = parentAction

class finalActionValue():
    def __init__(self, action, val, parentAction, numMoves):
        self.action = action
        self.val = val
        self.parentAction = parentAction
        self.numMoves = numMoves


actionList = []
allActions = []
def minimax(board, parentAction, bestVal):
    """
    Returns the optimal action for the current player on the board.

    """

    grid = copy.deepcopy(board)
    play = player(board)
   
    

    bestAction =  finalActionValue(None, None, parentAction, None)

    thisAction = finalActionValue(None, None, parentAction, None)
    
    if terminal(board):
        numMoves = 0
      
        thisAction.val = utility(board)
        action = thisAction
        while (action.parentAction != None):
            numMoves  +=1
            
            action = action.parentAction

        thisAction.numMoves = numMoves
       
        return thisAction

    
    
    
    if play == X:
        val = -10
        funcVal = 0
        bestAction.val = val

        
        
        for act in actions(grid):
            try: 
                if (bestAction.val != -10):
                    bestActionValue = bestAction.val
                else: 
                    bestActionValue = -10
            except: 
                bestActionValue = -10

            thisAction.action = act

            funcReturn = minimax(result(board, act), thisAction, bestActionValue)
            board = copy.deepcopy(grid)
            
           
            if (val<funcReturn.val):
          
                bestAction.action = act
                
                val = funcReturn.val
                bestAction.val = funcReturn.val
                bestAction.numMoves= funcReturn.numMoves

            elif (val == funcReturn.val):
              
                if (val >= 0):
                    if funcReturn.numMoves<bestAction.numMoves:
                        bestAction.action = act
                        bestAction.numMoves = funcReturn.numMoves

                else:
                    if funcReturn.numMoves>bestAction.numMoves:
                        bestAction.action = act
                        bestAction.numMoves = funcReturn.numMoves
             
            if thisAction.parentAction == None:
                allActions.append(act)
                allActions.append(val)
            
            try: 
                if (bestAction.val > bestVal):
                    break

            except:
                pass
            
        return bestAction
   
    elif play == O:
        val = 10
        funcVal = 0
        bestAction.val = val
        for act in actions(grid):

            try: 
                if (bestAction.val != 10):
                    bestActionValue = bestAction.val

                else:
                    bestActionValue = 10

            except:
                bestActionValue = 10

           # print("O doing move: "+ str(act))
           # print("grid is " + str(grid))
          #  print("board is "+ str(board))
            thisAction.action = act
         
            
            funcReturn = minimax(result(board, act), thisAction, bestActionValue)
            board = copy.deepcopy(grid)
          #  print(" O If I do: " + str(thisAction.action) + "opponent will do this: " + str(funcReturn.action))
            if (val>funcReturn.val):
                bestAction.action = act
                val = funcReturn.val
                bestAction.val = funcReturn.val
                bestAction.numMoves = funcReturn.numMoves

            elif (val == funcReturn.val):
                if (val<=0):
                    if funcReturn.numMoves<bestAction.numMoves:
                        bestAction.action = act
                        bestAction.numMoves = funcReturn.numMoves

                else:
                    if funcReturn.numMoves>bestAction.numMoves:
                        bestAction.action = act
                        bestAction.numMoves = funcReturn.numMoves
            
            if thisAction.parentAction == None:
                allActions.append(act)
                allActions.append(val)

            try: 
                if (bestAction.val < bestVal):
                    break

            except: 
                pass
        #print("when parent action is " + str(bestAction.parentAction.action)+ ", the best move is: " + str(bestAction.action))

        return bestAction

    else: 
        print("no ones turn")
    






def bestMove(board):

    if (terminal(board)):
        return None

    func = minimax(board, parentAction = None, bestVal = None)
    
    return func.action
        

   

initState = [[EMPTY, O, X],
             [EMPTY, X , EMPTY],
             [O, EMPTY, EMPTY ]]


#x = bestMove(initial_state())
#print("best Move is " + str(x))

#print(player(initState))




"""
for y in allActions:
    print(y)
"""



   