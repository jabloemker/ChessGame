import pygame
from .constants import BLACK, RED, WHITE, ROWS, COLS, SQUARE_SIZE
from .piece import Piece


class Board:
    START_ROWS = 3

    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.reset_pieces()

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == 0 or row == ROWS:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def draw_board_pattern(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE,
                                 col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def reset_pieces(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row+1) % 2):
                    if row < self.START_ROWS:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > (ROWS - (self.START_ROWS+1)):
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_board_pattern(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
