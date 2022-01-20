import tkinter as tk
import tkinter.messagebox as mssg
import connectionProlog as pl

LARGE_FONT = ('Arial', 16)
MEDIUM_FONT = ('Arial', 15)
SMALL_FONT = ('Arial', 12)


class TicTacToe(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.order = None

        self.frames = {}
        for F in (StartPage, BoardPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def get_page(self, page_class):
        return self.frames[page_class]

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def startGame(self, desicion):
        self.order = ['human', 'machine'] if desicion == 1 else ['machine', 'human']

        if self.order[0] == 'machine':
            page = self.get_page(BoardPage)
            page.machineTurn()

        self.show_frame(BoardPage)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        self.controller = controller

        label = tk.Label(self, text='What do you want to play with?', font=LARGE_FONT,
                         bg='black', fg='white')
        label.pack(pady=10, padx=10)

        option1 = tk.Button(self, text="X", font=MEDIUM_FONT, width=15,
                            command=lambda: self.controller.startGame(1))
        option2 = tk.Button(self, text="O", font=MEDIUM_FONT, width=15,
                            command=lambda: self.controller.startGame(2))


        option1.pack(pady=15, padx=10)
        option2.pack(pady=18, padx=10)


class BoardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        self.controller = controller
        bw = 3
        bh = 7


        self.boardObjects = []

        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.player = 1
        self.state = 'play'


        pos1 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(1))
        pos1.grid(row=2, column=1)
        self.boardObjects.append(pos1)

        pos2 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(2))
        pos2.grid(row=2, column=2)
        self.boardObjects.append(pos2)

        pos3 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(3))
        pos3.grid(row=2, column=3)
        self.boardObjects.append(pos3)

        pos4 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(4))
        pos4.grid(row=3, column=1)
        self.boardObjects.append(pos4)

        pos5 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(5))
        pos5.grid(row=3, column=2)
        self.boardObjects.append(pos5)

        pos6 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(6))
        pos6.grid(row=3, column=3)
        self.boardObjects.append(pos6)

        pos7 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(7))
        pos7.grid(row=4, column=1)
        self.boardObjects.append(pos7)

        pos8 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(8))
        pos8.grid(row=4, column=2)
        self.boardObjects.append(pos8)

        pos9 = tk.Button(self, text=' ', height=bw, width=bh,
                         font=MEDIUM_FONT, borderwidth=1,
                         command=lambda: self.humanTurn(9))
        pos9.grid(row=4, column=3)
        self.boardObjects.append(pos9)

        rs = tk.Button(self, text='Restart', bg='grey',
                       font=MEDIUM_FONT, borderwidth=2,
                       command=lambda: self.restart())
        rs.grid(row=2, column=5)

    def disAll(self):
        for obj in self.boardObjects:
            obj.config(state=tk.DISABLED)

    def setBoard(self):
        for value, obj in zip(self.board, self.boardObjects):
            if value != 0:
                obj['text'] = 'X' if value == 1 else 'O'
                obj.config(state=tk.DISABLED)
            else:
                obj['text'] = ' '
                obj.config(state=tk.ACTIVE)

    def restart(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.state = 'play'
        self.player = 1

        self.setBoard()
        self.controller.show_frame(StartPage)

    def humanTurn(self, position):

        if self.state == 'play':
            self.player, self.state, self.board = pl.moveHuman(self.player, self.state, self.board, position)
            self.setBoard()
            self.checkWinner()
            self.machineTurn()
    
    def machineTurn(self):

        if self.state == 'play':
            self.player, self.state, self.board = pl.moveMachine(self.player, self.state, self.board)
            self.setBoard()
            self.checkWinner()

    def checkWinner(self):

        if self.state == 'win':

            winner = self.controller.order[0] if self.player == 2 \
                else self.controller.order[1]

            message = f'The winner is {winner}'
            mssg.showinfo('Fin', message)


            self.disAll()

        elif self.state == 'draw':
            mssg.showinfo('End', 'Tie')
            self.disAll()