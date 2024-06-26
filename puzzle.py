import threading
from tkinter import Frame, Label, CENTER
import random
import logic
import constants as c
import ai_2048

AI_KEY_AUTOPLAY = "q"

class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        self.commands = {
            c.KEY_UP: logic.up,
            c.KEY_DOWN: logic.down,
            c.KEY_LEFT: logic.left,
            c.KEY_RIGHT: logic.right,
            c.KEY_UP_ALT1: logic.up,
            c.KEY_DOWN_ALT1: logic.down,
            c.KEY_LEFT_ALT1: logic.left,
            c.KEY_RIGHT_ALT1: logic.right,
            c.KEY_UP_ALT2: logic.up,
            c.KEY_DOWN_ALT2: logic.down,
            c.KEY_LEFT_ALT2: logic.left,
            c.KEY_RIGHT_ALT2: logic.right,
            c.KEY_AI: ai_2048.ai_move
        }

        self.grid_cells = []
        self.init_grid()
        self.matrix = logic.new_game()
        self.history_matrixs = []
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(
                    background,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=c.SIZE / c.GRID_LEN,
                    height=c.SIZE / c.GRID_LEN
                )
                cell.grid(
                    row=i,
                    column=j,
                    padx=c.GRID_PADDING,
                    pady=c.GRID_PADDING
                )
                t = Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=c.FONT,
                    width=5,
                    height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
                    )
        self.update_idletasks()

    def key_down(self, event):
        key = event.keysym
        if key == c.KEY_QUIT: 
            exit()
        if key == AI_KEY_AUTOPLAY:
            # Start AI autoplay in a separate thread
            ai_thread = threading.Thread(target=self.ai_autoplay)
            ai_thread.start()
        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_grid_cells()
            print('back on step total step:', len(self.history_matrixs))
        if key == c.KEY_AI:
            self.matrix, done = ai_2048.ai_move(20,30,self.matrix)
            if done:
                self.matrix = logic.add_two(self.matrix)
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
        elif key in self.commands:
            self.matrix, done = self.commands[key](self.matrix)
            if done:
                self.matrix = logic.add_two(self.matrix)
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                if logic.game_state(self.matrix) == 'win':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'lose':
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def ai_autoplay(self):
        move_count = 0
        while logic.game_state(self.matrix) != 'lose':
            self.matrix, valid_game = ai_2048.ai_move(40, 30, self.matrix)
            if valid_game:
                self.matrix = logic.add_two(self.matrix)
                self.update_grid_cells()
            move_count += 1

    def generate_next(self):
        index = (random.randint(0, c.GRID_LEN - 1), random.randint(0, c.GRID_LEN - 1))
        while self.matrix[index[0]][index[1]] != 0:
            index = (random.randint(0, c.GRID_LEN - 1), random.randint(0, c.GRID_LEN - 1))
        self.matrix[index[0]][index[1]] = 2

game_grid = GameGrid()
