import turtle
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

_1_color = 'MediumOrchid1'   # color of PLAYER1 marbles
_1_color_sel = 'deep pink' # color of PLAYER1  marbles when selected
_2_color = 'dodger blue' # color of PLAYER2 marbles
_2_color_sel = 'cyan' # color of player2 marbles when selected
color_unsel = [_1_color, _2_color]
color_sel = [_1_color_sel, _2_color_sel]
background = 'gray99'
frame_col = 'burlywood1'
move_color = 'medium aquamarine'
win_color = 'gold'
bg_color = 'misty rose'

with open('background\\\\settings.txt','r') as file:
    back_pic = file.readline()

button_clicked = None

valid_moves = {0:[1, 3, 4], 1:[0, 2, 4], 2:[1, 5, 4], 3:[0, 6, 4],   # valid moves from each location
               4:[0, 1, 2, 3, 5, 6, 7, 8], 5:[4, 2, 8],
               6:[3, 4, 7], 7:[4, 6, 8], 8:[4, 5, 7]}

about_app = 'This app allows you to play a Ghanaian game called Kwasiada Frankaa in the Akan dialect; a game\
 similar to TicTacToe.\nThis app was developed by Ignatius Boadi in August\
 2021 at Odumaa Lab.\nYou can reach the developer at ignatiusboadi at gmail dot com.' # INFO ABOUT APP

instructions = 'This game is played by two people. To play:\n\
1. Click START GAME. Players can then opt to enter their names in the boxes provided. If the field for either\
 Player 1 or Player 2 is empty, player is named Player 1 or Player 2 respectively.\n\n\
2. Click NEXT. You are then presented with three frames: BOARD, MARBLES and MOVES.\n\n\
3. Click on a marble under your name in the MARBLES frame. Then in the MOVES frame, select a number\
 corresponding to the position you want to move the marble to. Each player can move one marble at a time.\n\n\
4. After all players\' marbles are on the board, a player can change the position of one of his/her marbles\
 by selecting the marble from the MARBLES frame, then select the number corresponding to the desired\
  position in the MOVES frame.\n\n\
5. When a player has three marbles in line vertically, horizontally or diagonally, \
the player wins.' # INSTRUCTIONS ON HOW TO PLAY GAME.


def About():
    messagebox.showinfo(title='ABOUT APP', message=about_app) # DISPLAY INFO ABOUT APP


def Instructions():
    messagebox.showinfo(title='INSTRUCTIONS', message=instructions) # DISPLAY INSTRUCTIONS TO PLAY GAME


def Play():    
    global draw, locs, players, player_1, player_2, canvas_frame, start_positions, marble_selected
    global _1_marble_1, _1_marble_2, _1_marble_3, canvas
    global _2_marble_1, _2_marble_2, _2_marble_3
    canvas_frame = tk.LabelFrame(root, bg=background, text='GAME BOARD', width=470, height=400)
    canvas_frame.grid(row=0, column=0, sticky='we')
    canvas = tk.Canvas(canvas_frame, width=470, height=400)
    canvas.pack()
    locs = [(-180.00, -180.00), (0.00, -180.00), (180.00, -180.00),
            (-180.00, 0.00), (0.00, 0.00), (180.00, 0.00),
            (-180.00, 180.00), (0.00, 180.00), (180.00, 180.00)]


    def draw_square(length):
        for i in range(4):
            draw.forward(length)
            draw.left(90)
    global turtle_screen
    turtle_screen = turtle.TurtleScreen(canvas)
    try:
        turtle_screen.bgpic(back_pic)
    except:
        turtle_screen.bgcolor('gray99')
    turtle_screen.update()
    draw = turtle.RawTurtle(turtle_screen)
    draw.width(5)
    draw.speed('fastest')
    draw.hideturtle()
    draw.penup()
    draw.goto(locs[0])
    draw.pendown()
    draw_square(360)
    draw.goto(locs[8])
    draw.goto(locs[6])
    draw.goto(locs[2])

    for pos in [0, 1, 3]:
        draw.penup()
        draw.goto(locs[pos])
        draw.pendown()
        draw_square(180)

    draw.left(90)
    draw.shape('circle')

    for pos, loc in enumerate(locs):
        draw.penup()
        draw.goto(loc)
        draw.pendown()
        draw.color('yellow')
        draw.stamp()
        draw.backward(5)
        draw.color('red')
        draw.write('{}'.format(pos + 1))

    _1_marble_1 = turtle.RawTurtle(canvas)
    _1_marble_1.shape('circle')
    _1_marble_1.color(_1_color)
    _1_marble_1.left(90)
    _1_marble_2 = turtle.RawTurtle(canvas)
    _1_marble_2.shape('turtle')
    _1_marble_2.color(_1_color)
    _1_marble_2.left(90)
    _1_marble_3 = turtle.RawTurtle(canvas)
    _1_marble_3.shape('triangle')
    _1_marble_3.color(_1_color)
    _1_marble_3.left(90)
    _2_marble_1 = turtle.RawTurtle(canvas)
    _2_marble_1.shape('circle')
    _2_marble_1.color(_2_color)
    _2_marble_1.left(90)
    _2_marble_2 = turtle.RawTurtle(canvas)
    _2_marble_2.shape('turtle')
    _2_marble_2.color(_2_color)
    _2_marble_2.left(90)
    _2_marble_3 = turtle.RawTurtle(canvas)
    _2_marble_3.shape('triangle')
    _2_marble_3.color(_2_color)
    _2_marble_3.left(90)

    marble_selected = _1_marble_1
    player_1 = [_1_marble_1, _1_marble_2, _1_marble_3]
    player_2 = [_2_marble_1, _2_marble_2, _2_marble_3]

    players = [player_1, player_2]

    start_positions = []
    for player in players:
        n = 180.00
        for pos in range(3):
            player[pos].penup()
            player[pos].goto(((-1)**players.index(player)) * -210.00, n)
            start_positions.append((((-1)**players.index(player)) * -210.00, n))
            n -= 180.00

    draw.hideturtle()


def Start():
    global user_names, _1_entry, _2_entry, num_of_plays
    num_of_plays = 0 # number of plays used to determine the player whose turn it is to play
    user_names = tk.Toplevel(root)
    user_names.attributes('-topmost', 'true')
    user_names.grab_set()
    user_names.title('USERNAMES')
    tk.Label(user_names, text='NAME OF \nPLAYER ONE', relief='groove',
             bg=_1_color).grid(row=0, column=0, sticky='we')
    tk.Label(user_names, text='NAME OF \nPLAYER TWO', relief='groove',
             bg=_2_color).grid(row=0, column=1, sticky='we')
    _1_entry = tk.Entry(user_names, bd=5)
    _1_entry.grid(row=1, column=0, sticky='we')
    _2_entry = tk.Entry(user_names, bd=5)
    _2_entry.grid(row=1, column=1, sticky='we')
    next_ = tk.Button(user_names, text='NEXT', bg='thistle2', command=Next)
    user_names.resizable(0, 0)
    next_.grid(row=2, column=0, columnspan=2, sticky='we')


def Next():
    global player1_name, player2_name, player_names, moves, marbles, canvas_frame, player1, player2, quit_game
    global player1_wins, player2_wins, restart_diff, players_buttons, marbles_moves_frame
    global _1circle, _1turtle, _1triangle, _2circle, _2turtle, _2triangle, space

    player1_wins, player2_wins = 0, 0
    
    canvas_frame.destroy()
    start.destroy()
    
    player1_name = _1_entry.get().upper()
    player2_name = _2_entry.get().upper()
    user_names.destroy()
    
    if player1_name.isspace() or player1_name == '':
        player1_name = 'PLAYER 1'
    if player2_name.isspace() or player2_name == '':
        player2_name = 'PLAYER 2'
    
    player_names = [player1_name, player2_name]
    
    marbles_moves_frame = tk.LabelFrame(root, background=frame_col)
    marbles_moves_frame.grid(row=1, column=0, sticky='we')
    marbles = tk.LabelFrame(marbles_moves_frame, text='MARBLES', bg=frame_col)
    marbles.grid(row=2, column=0, sticky='we')
    tk.Label(marbles, text='{} WINS: {}'.format(player1_name, player1_wins), 
             bg=_1_color, relief='groove').grid(row=4,column=0, sticky='we')
    tk.Label(marbles, text='{} WINS: {}'.format(player2_name, player2_wins), 
             bg=_2_color, relief='groove').grid(row=4,column=2, sticky='we')
    moves = tk.LabelFrame(marbles_moves_frame, text='MOVES', bg=frame_col)
    moves.grid(row=2, column=1, columnspan=2, sticky='we')
    
    width = 9
    _1 = tk.Button(moves, text='1', command=lambda:Move(0), bg=move_color, state='disabled')
    _1.config(width=width)
    _1.grid(row=3, column=0, sticky='we')
    _2 = tk.Button(moves, text='2', command=lambda:Move(1), bg=move_color, state='disabled')
    _2.config(width=width)
    _2.grid(row=3, column=1, sticky='we')
    _3 = tk.Button(moves, text ='3', command=lambda:Move(2), bg=move_color, state='disabled')
    _3.config(width=width)
    _3.grid(row=3, column=2, sticky='we')
    _4 = tk.Button(moves, text ='4', command=lambda:Move(3), bg=move_color, state='disabled')
    _4.config(width=width)
    _4.grid(row=2, column=0, sticky='we')
    _5 = tk.Button(moves, text ='5', command=lambda:Move(4), bg=move_color, state='disabled')
    _5.config(width=width)
    _5.grid(row=2, column=1, sticky='we')
    _6 = tk.Button(moves, text ='6', command=lambda:Move(5), bg=move_color, state='disabled')
    _6.config(width=width)
    _6.grid(row=2, column=2, sticky='we')
    _7 = tk.Button(moves, text ='7', command=lambda:Move(6), bg=move_color, state='disabled')
    _7.config(width=width)
    _7.grid(row=1, column=0, sticky='we')
    _8 = tk.Button(moves, text ='8', command=lambda:Move(7), bg=move_color, state='disabled')
    _8.config(width=width)
    _8.grid(row=1, column=1, sticky='we')
    _9 = tk.Button(moves, text ='9', command=lambda:Move(8), bg=move_color, state='disabled')
    _9.config(width=width)
    _9.grid(row=1, column=2, sticky='we')
    
    tk.Label(marbles, text='MARBLES OF {}'.format(player1_name), relief='groove', 
             bg=_1_color).grid(row=0, column=0, sticky='we')
    
    _1circle = tk.Button(marbles, text='CIRCLE', bg=_1_color, activebackground=_1_color_sel,
                        command=lambda: Marble_clicked('00'), state='disabled')
    _1circle.grid(row=1, column=0, sticky='we')
    _1turtle = tk.Button(marbles, text='TURTLE', bg=_1_color, activebackground=_1_color_sel,
                        command=lambda: Marble_clicked('01'), state='disabled')
    _1turtle.grid(row=2, column=0, sticky='we')
    _1triangle = tk.Button(marbles, text='TRIANGLE', bg=_1_color, activebackground=_1_color_sel,
                        command=lambda: Marble_clicked('02'), state='disabled')
    _1triangle.grid(row=3, column=0, sticky='we')
    
    space = tk.Label(marbles, text = '    ', bg = frame_col)
    space.grid(row=0, column=1, rowspan=4, sticky='ns')
    
    tk.Label(marbles, text='MARBLES OF {}'.format(player2_name), relief='groove',
            bg=_2_color).grid(row=0, column=2, sticky='we')
    
    _2circle = tk.Button(marbles, text='CIRCLE', bg=_2_color, activebackground=_2_color_sel,
                        command=lambda: Marble_clicked('10'), state='disabled')
    _2circle.grid(row=1, column=2, sticky='we')
    _2turtle = tk.Button(marbles, text='TURTLE', bg=_2_color, activebackground=_2_color_sel,
                        command=lambda: Marble_clicked('11'), state='disabled')
    _2turtle.grid(row=2, column=2, sticky='we')
    _2triangle = tk.Button(marbles, text='TRIANGLE', bg=_2_color, activebackground=_2_color_sel,
                        command=lambda: Marble_clicked('12'), state='disabled')
    _2triangle.grid(row=3, column=2, sticky='we')
    
    restart = tk.Button(moves, text='RESTART CURRENT GAME', command=Restart, bg='salmon', state='disabled')
    restart.grid(row=4, column=0, columnspan=3, sticky='we')
    
    restart_diff = tk.Button(moves, text='CHANGE PLAYERS', state='disabled',
                             command=Change_Players, bg='maroon')
    restart_diff.grid(row=5, column=0, columnspan=3, sticky='we')
    
    space = tk.Label(root, text='{} VS {}'.format(player1_name, player2_name), bg=frame_col,
                     font=('Lucida Calligraphy','12','bold'))
    space.grid(row=3, column=0, sticky='we')
    
    moves = [_1, _2, _3, _4, _5, _6, _7, _8, _9]
    player1_buttons = [_1circle, _1turtle, _1triangle]
    player2_buttons = [_2circle, _2turtle, _2triangle]
    players_buttons = [player1_buttons, player2_buttons]

    Play()
    
    settings_menu.entryconfig(0, state='normal')
    more_menu.entryconfig(2, state='normal')
    for button in player1_buttons + player2_buttons:
        button.config(state='normal')
    for button in moves:
        button.config(state='normal')
    restart_diff.config(state='normal')
    restart.config(state='normal')
    

def Marble_clicked(n):
    global marble_selected, player_selected, button_clicked
    player_selected = int(n[0])
    button_clicked = players_buttons[int(n[0])][int(n[1])]
    marble_selected = players[int(n[0])][int(n[1])]
    marble_selected.color(color_sel[player_selected])
    button_clicked.config(background=color_sel[player_selected])
    for value in range(2):
        for marble in players[value]:
            if marble != marble_selected:
                marble.color(color_unsel[value])

    for value in range(2):
        for button in players_buttons[value]:
            if button != button_clicked:
                button.config(background=color_unsel[value])


def Move(loc):
    global num_of_plays, canvas_frame, img, start, marble_selected, quit_game, start_positions
    global player1_name, player1_wins, player2_name, player2_wins, button_clicked
    if button_clicked == None:
        button_clicked = players_buttons[0][0]
    if num_of_plays % 2 == 0 and player_selected == 1:
        messagebox.showwarning(title='NOT YOUR TURN', 
                    message='{} has to play. Kindly wait for your turn.'.format(player_names[num_of_plays % 2]))
        marble_selected.color(color_unsel[player_selected])
        button_clicked.config(background=color_unsel[player_selected])
    elif num_of_plays % 2 == 1 and player_selected == 0:
        messagebox.showwarning(title='NOT YOUR TURN', 
                    message='{} has to play. Kindly wait for your turn.'.format(player_names[num_of_plays % 2]))
        marble_selected.color(color_unsel[player_selected])
        button_clicked.config(background=color_unsel[player_selected])
    else:
        if len(start_positions) != 0 and marble_selected.position() not in start_positions:
            messagebox.showwarning(title='INVALID SELECTION', 
                            message='You have at least one marble not on\n the board. Move such a marble rather.')
            marble_selected.color(color_unsel[player_selected])
            button_clicked.config(background=color_unsel[player_selected])
        elif marble_selected.position() in start_positions or len(start_positions) == 0:
            cur_pos = marble_selected.position()
            marble_locs = [_1_marble_1.position(), _1_marble_2.position(), _1_marble_3.position(),
                           _2_marble_1.position(), _2_marble_2.position(), _2_marble_3.position()]
            if cur_pos in locs and loc not in valid_moves[locs.index(cur_pos)]:
                valid = valid_moves[locs.index(cur_pos)]
                _message1 = 'With this marble, you can only move to {}, {} or {}.'.format(
                    valid[0] + 1, valid[1] + 1, valid[2] + 1)
                messagebox.showwarning(title='INVALID MOVE', message=_message1)
            elif locs[loc] in marble_locs:
                _message2 = 'You cannot move to this position because\n another marble is already in that position.'
                messagebox.showwarning(title='INVALID MOVE', message=_message2)
            else:
                try:
                    start_positions.remove(marble_selected.position())
                except ValueError:
                    pass
                try:
                    marble_selected.goto(locs[loc])
                except:
                    pass
                
                marble_selected.color(color_unsel[player_selected])
                button_clicked.config(background=color_unsel[player_selected])
                
                loc_11 = _1_marble_1.position()
                loc_12 = _1_marble_2.position()
                loc_13 = _1_marble_3.position()
                loc_21 = _2_marble_1.position()
                loc_22 = _2_marble_2.position()
                loc_23 = _2_marble_3.position()

                win_1 = [(-180.00, 180.00), (0.00, 0.00), (180.00, -180.00)]
                win_2 = [(180.00, 180.00), (0.00,0), (-180,-180)]
                win_3 = [(-180.00, 180.00), (-180.00, 0.00), (-180.00, -180.00)]
                win_4 = [(180.00, 180.00), (180.00, 0.00), (180.00, -180.00)]
                win_5 = [(0.00, 180.00), (0.00, 0.00), (0.00, -180.00)]
                win_6 = [(-180.00, 0.00), (0.00, 0.00), (180.00, 0.00)]
                win_7 = [(-180.00, 180.00), (0.00, 180.00), (180.00, 180.00)]
                win_8 = [(-180.00, -180.00), (0.00, -180.00), (180.00, -180.00)]
                wins = {1:win_1, 2:win_2, 3:win_3, 4:win_4, 5:win_5,6:win_6,7:win_7,8:win_8}

                for i in range(1,9):
                    if loc_11 in wins[i] and loc_12 in wins[i] and loc_13 in wins[i]:
                        player1_wins += 1
                        tk.Label(marbles, text='{} WINS: {}'.format(player1_name, player1_wins), 
                                     bg=_1_color, relief='groove').grid(row=4,column=0, sticky='we')
                        win_message = messagebox.askyesno(title='CONGRATULATIONS', 
                        message = '{} WINS!!! BETTER LUCK NEXT TIME {}.\nDO YOU WANT TO PLAY ANOTHER GAME?'.format(
                                    player1_name, player2_name))
                        if win_message == 1:
                            start_positions = []
                            for player in players:
                                n = 180.00
                                for pos in range(3):
                                    player[pos].penup()
                                    player[pos].goto(((-1)**players.index(player)) * -210.00, n)
                                    start_positions.append((((-1)**players.index(player)) * -210.00, n))
                                    n -= 180.00
                        else:
                            start = tk.Button(root, text='START GAME', command=Start, bg='cyan2')
                            start.config(width=30)
                            start.grid(row=1, column=0, sticky='we')
                            space.destroy()
                            canvas_frame.destroy()
                            canvas_frame = tk.LabelFrame(root, text='GAME BOARD', width=470, height=400)
                            img = tk.PhotoImage(file='canvas_img.png')
                            tk.Label(canvas_frame, image=img).grid(row=0,column=0)
                            canvas_frame.grid(row=0, column=0, sticky='we')
                            try:
                                marbles_moves_frame.destroy()
                            except:
                                pass
                    elif loc_21 in wins[i] and loc_22 in wins[i] and loc_23 in wins[i]:
                        player2_wins += 1
                        tk.Label(marbles, text='{} WINS: {}'.format(player2_name, player2_wins), 
                                     bg=_2_color, relief='groove').grid(row=4,column=2, sticky='we')
                        win_message = messagebox.askyesno(title='CONGRATULATIONS', 
                        message = '{} WINS!!! BETTER LUCK NEXT TIME {}.\nDO YOU WANT TO PLAY ANOTHER GAME?'.format(
                                    player2_name, player1_name))
                        if win_message == 1:
                            start_positions = []
                            for player in players:
                                n = 180.00
                                for pos in range(3):
                                    player[pos].penup()
                                    player[pos].goto(((-1)**players.index(player)) * -210.00, n)
                                    start_positions.append((((-1)**players.index(player)) * -210.00, n))
                                    n -= 180.00
                        else:
                            start = tk.Button(root, text='START GAME', command=Start, bg='cyan2')
                            start.config(width=30)
                            start.grid(row=1, column=0, sticky='we')
                            space.destroy()
                            canvas_frame.destroy()
                            canvas_frame = tk.LabelFrame(root, text='GAME BOARD', width=470, height=400)
                            img = tk.PhotoImage(file='canvas_img.png')
                            tk.Label(canvas_frame, image=img).grid(row=0,column=0)
                            canvas_frame.grid(row=0, column=0, sticky='we')
                            try:
                                marbles_moves_frame.destroy()
                            except:
                                pass
                num_of_plays += 1


def Quit_Game():
    global canvas_frame, start, img, space
    quit = messagebox.askyesno(title='End Game', 
                          message='Do you want to quit the game?')
    if quit == 1:
        settings_menu.entryconfig(0, state='disabled')
        more_menu.entryconfig(2, state='disabled')
        start = tk.Button(root, text='START GAME', command=Start, bg='cyan2')
        start.config(width=30)
        start.grid(row=1, column=0, columnspan=2, sticky='we')
        canvas_frame.destroy()
        canvas_frame = tk.LabelFrame(root, text='GAME BOARD', width=470, height=400)
        img = tk.PhotoImage(file='canvas_img.png')
        tk.Label(canvas_frame, image=img).grid(row=0,column=0)
        canvas_frame.grid(row=0, column=0, sticky='we')
        try:
            marbles_moves_frame.destroy()
            space.destroy()
        except:
            pass


def Exit_App():
    quit = messagebox.askyesno(title='Exit App',
                              message='Do you want to close this App?')
    if quit == 1:
        with open('background\\\\settings.txt', 'w') as file:
            file.write(back_pic)
        root.destroy()


def Restart():
    global start_positions, num_of_plays
    num_of_plays = 0 # number of plays used to determine the player whose turn it is to play
    restart_game = messagebox.askyesno(title='RESTART GAME!',
                                       message = 'Do you want to restart the current game?')
    if restart_game == 1:
        start_positions = []
        for player in players:
            coord = 180.00
            for pos in range(3):
                player[pos].penup()
                player[pos].goto(((-1)**players.index(player)) * -210.00, coord)
                start_positions.append((((-1)**players.index(player)) * -210.00, coord))
                coord -= 180.00


def Change_Players():
    change = messagebox.askyesno(title='CHANGE PLAYERS',
    message = 'Changing players will restart the game.\nDo you want to continue?')
    if change == 1:
        space.destroy()
        marbles_moves_frame.destroy()
        Start()

def change_bg():
    global num, viewer, pics
    warn_message = 'Changing background will restart the game.\nDo you want to continue?'
    response = messagebox.askyesno(title='WARNING', message=warn_message)
    if response == 1:
        viewer = tk.Toplevel(root)
        viewer.title('CHANGE BACKGROUND')
#         viewer.attributes('-topmost', 'true')
        viewer.grab_set()
        viewer.resizable(0, 0)
        valid_pics = ['background\\\\' + file for file in listdir('background') if file[-4:] == '.png']
        pics = [tk.PhotoImage(file=file).subsample(2, 2) for file in valid_pics]

        num = 0

        mylabel = tk.Label(viewer, image=pics[num])
        mylabel.grid(row=0, column=0, columnspan=3)

        def Next_pic():
            global num
            if num < len(pics) - 1:
                num += 1
                mylabel = tk.Label(viewer, image=pics[num])
                mylabel.grid(row=0, column=0, columnspan=3)
                status = tk.Label(viewer, text=f'{num + 1} of {len(pics)}', bd = 5, 
                                  relief = 'groove', anchor = 'e', bg='peach puff')
                status.grid(row=2, column=2, sticky='we')
            else:
                pass

        def Back():
            global num
            if num > 0:
                num -= 1
                mylabel = tk.Label(viewer, image=pics[num])
                mylabel.grid(row=0, column=0, columnspan=3)
                status = tk.Label(viewer, text=f'{num + 1} of {len(pics)}', bd = 5, 
                                  relief = 'groove', anchor = 'e', bg='peach puff')
                status.grid(row=2, column=2, sticky='we')
            else:
                pass

        def Select():
            global back_pic, turtle_screen
            back_pic = valid_pics[num]
            select.config(state='disabled')
            exit_viewer.config(state='disabled')
            browse.config(state='disabled')
            turtle_screen = turtle.TurtleScreen(canvas)
            turtle_screen.bgpic(back_pic)
            turtle_screen.update()
            Play()
            select.config(state='normal')
            exit_viewer.config(state='normal')
            browse.config(state='normal')
            
        def Browse():
            global new_pic_name, pics, num
            select_pic = filedialog.askopenfilename(title='Choose A File', 
                filetypes=(('jpg pictures', '*.jpg'), 
                           ('jpeg pictures', '*.jpeg'), ('png pictures','*.png')))
            file = imread(select_pic)
            file = resize(file, (470, 400), interpolation=INTER_AREA)
            new_pic_name = 'background\\\\' + ''.join(select_pic.split('/')[-1].split('.')[:-1]) + '.png'
            imwrite(new_pic_name, file)
            img = tk.PhotoImage(file=new_pic_name).subsample(2, 2)
            valid_pics.extend([new_pic_name])
            num = valid_pics.index(new_pic_name)
            pics.extend([img])
            mylabel = tk.Label(viewer, image=img)
            mylabel.grid(row=0, column=0, columnspan=3)
            status = tk.Label(viewer, text=f'{num + 1} of {len(pics)}', bd = 5, 
                                  relief = 'groove', anchor = 'e', bg='peach puff')
            status.grid(row=2, column=2, sticky='we')
            
        button_col = 'bisque'
        next_ = tk.Button(viewer, text='Next' , command=Next_pic, bg=button_col)
        back = tk.Button(viewer, text='Back', command=Back, bg=button_col)
        select = tk.Button(viewer, text='Select', command=Select, bg=button_col)
        back.grid(row=1, column=0, sticky='we')
        select.grid(row=1, column=1, sticky='we')
        next_.grid(row=1, column=2, sticky='we')
        status = tk.Label(viewer, text=f'Image {num + 1} of {len(pics)}', bd = 5, 
                          relief = 'sunken', anchor = 'e', bg='peach puff')
        status.grid(row=2, column=2, sticky='we')
        exit_viewer = tk.Button(viewer, text='Exit', command=viewer.destroy, bg='red2')
        exit_viewer.grid(row=2, column=1, sticky='we')
        browse = tk.Button(viewer, text='Browse PC...', command=Browse, bg=button_col)
        browse.grid(row=2, column=0, sticky='we')
        viewer.mainloop()

root = tk.Tk(className=' KWASIADA FRANKAA')
root['bg'] = frame_col
root.resizable(0, 0)
root.iconbitmap('logo_new.ico')

canvas_frame = tk.LabelFrame(root, bg='aliceblue', text='GAME BOARD', width=470, height=400)
img = tk.PhotoImage(file='canvas_img.png')
tk.Label(canvas_frame, image=img).grid(row=0,column=0)
canvas_frame.grid(row=0, column=0, sticky='we')

start = tk.Button(root, text='START GAME', command=Start, bg='cyan2')
start.config(width=30)
start.grid(row=1, column=0, sticky='we')

my_menu = tk.Menu(root, background='blue')
root.config(menu=my_menu)

settings_menu = tk.Menu(my_menu, tearoff=0, background=bg_color)
my_menu.add_cascade(label='Settings', menu=settings_menu)
settings_menu.add_command(label='Change Background', command=change_bg)
settings_menu.entryconfig(0, state='disabled')

more_menu = tk.Menu(my_menu, tearoff=0, background=bg_color)
my_menu.add_cascade(label='More...', menu=more_menu)
more_menu.add_command(label='Instructions', command=Instructions)
more_menu.add_command(label='About', command=About)
more_menu.add_command(label='Quit Current Game', command=Quit_Game)
more_menu.entryconfig(2, state='disabled')
more_menu.add_command(label='Exit App', command=Exit_App)

root.mainloop()
