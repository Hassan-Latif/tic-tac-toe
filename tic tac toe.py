#!/usr/bin/env python
# coding: utf-8

# In[1]:


board=[" " for x in range(10)]

def insertLetter(letter,pos):
    if boardFull(board) and not(isWinner(board,"X")) and not(isWinner(board,"O")):
        print("Game is tied")
    board[pos] = letter
    
def isSpace(pos):
    return board[pos]==" "

def boardFull(board):
    if board.count(" ")>1:
        return False
    else:
        return True
def selectRandom(li):
    import random
    r=len(li)
    x=random.randrange(r)
    return li[x]
    
def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ") 
    
    print("____________")
    
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ") 
    
    print("____________")
    
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")
   

def isWinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or 
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l)) 
    

def playerMove():
    run=True
    while run:
        move=input("Please enter a number between 1 and 9")
        try:
            move=int(move)

            if move>0 and move<10:
                if isSpace(move):
                    run=False
                    insertLetter("X",move)
                else:
                    print("This space is already occupied")

            else:
                print("Please eneter a number berween 1 and 9")
        except:
            print("Please enter a valid number")
            
def computerMove():
    possibleMoves=[x for x,letter in enumerate(board) if letter==" " and x!=0]
    move =0
    for let in ["0","X"]:
        for i in possibleMoves:
            boardCopy=board[:]
            boardCopy[i]=let
            if isWinner(boardCopy,let):
                move=i
                return move
    
    cornerValues=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerValues.append(i)
    if len(cornerValues)>0 :
        move=selectRandom(cornerValues)
        return move
    
    if 5 in possibleMoves:
        move=5
        return move
    
    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgeOpen.append(i)
    if len(edgesOpen)>0:
        move=selectRandom(edgesOpen)
        return move

def main():
    print("Welcome to the game")
    printBoard(board)
    while not(boardFull(board)):
       
        if not(isWinner(board,"O")):
            playerMove()
            printBoard(board)
        else:
            print("Sorry you lose")
            break
        if not(isWinner(board,"X")):
            move=computerMove()
            if move==0:
                print("")
            else:
                insertLetter("O",move)
                print("Computer placed a move on position ", move)
                printBoard(board)
        else:
            print("you win")
            break

            
    if boardFull(board):
        print("Game is tied")
        
            

            
while True:
    inp=input("Do you want to play again? y/n")
    if inp.lower()=="y":
        board=[" " for x in range(10)]
        print("___________________")
        main()
    else:
        break


# In[ ]:




