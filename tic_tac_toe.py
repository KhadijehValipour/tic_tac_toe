import random

from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from functools import partial

def check():
    # check row
    for i in range(3):
        if Buttons[i][0].text() == 'X' and Buttons[i][1].text() == 'X' and Buttons[i][2].text() == 'X':
            show_message(Buttons[i][0].text())
        elif Buttons[i][0].text() == 'O' and Buttons[i][1].text() == 'O' and Buttons[i][2].text() == 'O':
            show_message(Buttons[i][0].text())

    # check columns
    for j in range(3):
        if Buttons[0][j].text() == 'X' and Buttons[1][j].text() == 'X' and Buttons[2][j].text() == 'X':
            show_message(Buttons[0][j].text())
        elif Buttons[0][j].text() == 'O' and Buttons[1][j].text() == 'O' and Buttons[2][j].text() == 'O':
            show_message(Buttons[0][j].text())

    # Check diagonals
    if Buttons[0][0].text() == 'X' and Buttons[1][1].text() == 'X' and Buttons[2][2].text() == 'X':
        show_message(Buttons[0][0].text())
    elif Buttons[0][0].text() == 'O' and Buttons[1][1].text() == 'O' and Buttons[2][2].text() == 'O':
        show_message(Buttons[0][0].text())
    if Buttons[0][2].text() == 'X' and Buttons[1][1].text() == 'X' and Buttons[2][0].text() == 'X':
        show_message(Buttons[0][2].text())
    if Buttons[0][2].text() == 'O' and Buttons[1][1].text() == 'O' and Buttons[2][0].text() == 'O':
        show_message(Buttons[0][2].text())

def show_message(winner):
    global points_o, points_x
    if winner == 'O':
        points_o += 1
        main_window.player_o_label.setText(f"Player O : {points_o}")
    elif winner == 'X':
        points_x += 1
        main_window.player_x_label.setText(f"Player X : {points_x}")
    msg_box = QMessageBox(text=f"⭐️⭐️⭐️ player {winner} wins ⭐️⭐️⭐️")
    msg_box.setWindowTitle("✨Congratulations✨")
    msg_box.exec()
    restart_game()

def play(row, col):
    global player
    if player == 1:
        Buttons[row][col].setText("X")
        Buttons[row][col].setStyleSheet("color: blue; background-color: lightblue")
        player = 2
    elif player == 2:
        Buttons[row][col].setText("O")
        Buttons[row][col].setStyleSheet("color: red; background-color: lightpink")
        player = 1
    check()





def restart_game():
     for i in range(3):
         for j in range(3):
             Buttons[i][j].setText('')
             Buttons[i][j].setStyleSheet("background-color: white")

app = QApplication([])

player = 1
points_o = 0
points_x = 0

loader = QUiLoader()
main_window = loader.load("tic_tac_toe.ui")
main_window.show()

Buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

for i in range(3):
    for j in range(3):
        Buttons[i][j].clicked.connect(partial(play, i, j))


main_window.btn_restart.clicked.connect(restart_game)



app.exec()
