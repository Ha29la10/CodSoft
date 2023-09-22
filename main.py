board={1:' ',2:' ',3:' ',
        4:' ',5:' ',6:' ',
        7:' ',8:' ',9:' '}

def print_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")
def space_isFree(position):
    if (board[position]==' '):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if board[key]==' ':
            return False

    return True

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def insert_letter(letter,position):
    if(space_isFree(position)):
        board[position]=letter
        print_board(board)
        if(checkDraw()):
            print("Draw!")
            exit()
        if checkWin():
            if letter=='X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!") #never going to happen
                exit()
        return

    else:
        print("Can't insert there!")
        position=int(input("Enter new position"))
        insert_letter(letter,position)
        return


player='O'
bot='X'
def PlayerMove():
    position=int(input("Enter position for 'O': "))
    insert_letter(player,position)
    return
def checkwhichWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def minimax(board,depth,isMaximize):
    #base case
  if(checkwhichWon(bot)):
      return 1
  elif (checkwhichWon(player)):
      return -1

  elif checkDraw():
      return 0

#bot:
  if isMaximize:
      bestscore = -1000
      for key in board.keys():
          if (board[key] == ' '):
              board[key] = bot
              score = minimax(board, depth+1, False)
              board[key] = ' '
              if (score > bestscore):
                  bestscore = score
      return bestscore
  #enemy:
  else:
      bestscore = 1000

      for key in board.keys():
          if (board[key] == ' '):
              board[key] = player
              score = minimax(board, depth+1, True)
              board[key] = ' '
              if (score < bestscore):
                  bestscore = score
      return bestscore




def botmove():
    bestscore=-1000
    bestmove=0
    for key in board.keys():
        if(board[key]==' '):
            board[key]=bot
            score=minimax(board,0,False)
            board[key]=' '
            if(score>bestscore):
                bestscore=score
                bestmove=key
    insert_letter(bot,bestmove)
    return



while not checkWin():
    botmove()
    PlayerMove()

