import numpy as np
import pygame
import sys
BLUE = (0,0,255)
BLAC = (0,0,0)
rowCount = 6
columnCount = 7

def createBoard():
    board = np.zeros((rowCount, columnCount))
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def isValidLocation(board, col):
    return board[rowCount-1][col] == 0

def getNextOpenRow(board, col):
    for r in range(rowCount):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(np.flip(board, 0))

def winningMove(board, piece):
    for c in range(columnCount-3):
        for r in range(rowCount):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for c in range(columnCount):
        for r in range(rowCount-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    for c in range(columnCount-3):
        for r in range(rowCount-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(columnCount):
        for r in range(3, rowCount):
            if board[r][c] == piece and board[r-1][c-1] == piece and board[r-2][c-2] == piece and board[r-3][c-3] == piece:
                return True

def drawBoard(board): 
    for c in range(columnCount):
        for r in range(rowCount):
            pygame.draw.rect(screen, BLUE, (c * squareSize, r * squareSize + squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, BLACK, (int(c * squareSize + squareSize/2, r * squareSize + squareSize + 
            squareSize/2, RADIUS)))

print(createBoard())
printBoard(board)
gameOver = False
turn = 0
pygame.init()
squareSize = 100
width = columnCount * squareSize
height = (rowCount+1) * squareSize

size = (width, height)
RADIUS = int(squareSize/2 - 5)  
screen = pygame.display_set_mode(size)
drawBoard(board)
pygame.display.update()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            continue

    if turn == 0:
        col = int(input("Player 1 Make your selection (0-6):"))
        
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
            
            if winningMove(board, 1):
                print("Player 1 wins!")
                gameOver = True

    else:
        col = int(input("Player 2 Make your selection (0-6):"))
        
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)
          
            if winningMove(board, 2):
                print("Player 2 wins!")
                gameOver = True
                
    printBoard(board)   

    turn += 1
    turn %= 2
