def initializeCharacters():

    global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36
    c1 = '1'
    c2 = '2'
    c3 = '3'
    c4 = '4'
    c5 = '5'
    c6 = '6'
    c7 = '7'
    c8 = '8'
    c9 = '9'
    c10 = '10'
    c11 = '11'
    c12 = '12'
    c13 = '13'
    c14 = '14'
    c15 = '15'
    c16 = '16'
    c17 = '17'
    c18 = '18'
    c19 = '19'
    c20 = '20'
    c21 = '21'
    c22 = '22'
    c23 = '23'
    c24 = '24'
    c25 = '25'
    c26 = '26'
    c27 = '27'
    c28 = '28'
    c29 = '29'
    c30 = '30'
    c31 = '31'
    c32 = '32'
    c33 = '33'
    c34 = '34'
    c35 = '35'
    c36 = '36'

def draw():
    print(" " + c31 + " |" + " " + c32 + " |" + " " + c33 + " |" + " " + c34 + " |" + " " + c35 + " |" + " " + c36 + " |")
    print("------------------------------")
    print(" " + c25 + " |" + " " + c26 + " |" + " " + c27 + " |" + " " + c28 + " |" + " " + c29 + " |" + " " + c30 + " |")
    print("------------------------------")
    print(" " + c19 + " |" + " " + c20 + " |" + " " + c21 + " |" + " " + c22 + " |" + " " + c23 + " |" + " " + c24 + " |")
    print("------------------------------")
    print(" " + c13 + " |" + " " + c14 + " |" + " " + c15 + " |" + " " + c16 + " |" + " " + c17 + " |" + " " + c18 + " |")
    print("------------------------------")
    print(" " + c7 + "  |" + " " + c8 + "  |" + "  " + c9 + " |" + " " + c10 + " |" + " " + c11 + " |" + " " + c12 + " |")
    print("------------------------------")
    print(" " + c1 + "  |" + "  " + c2 + " |" + " " + c3 + "  |" + " " + c4 + "  |" + " " + c5 + "  |" + " " + c6 + "  |")
    print("------------------------------")

def replace(i, c):
    global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36
    if i == 1:
        c1 = c
    elif i == 2:
        c2 = c
    elif i == 3:
        c3 = c
    elif i == 4:
        c4 = c
    elif i == 5:
        c5 = c
    elif i == 6:
        c6 = c
    elif i == 7:
        c7 = c
    elif i == 8:
        c8 = c
    elif i == 9:
        c9 = c
    elif i == 10:
        c10 = c
    elif i == 11:
        c11 = c
    elif i == 12:
        c12 = c
    elif i == 13:
        c13 = c
    elif i == 14:
        c14 = c
    elif i == 15:
        c15 = c
    elif i == 16:
        c16 = c
    elif i == 17:
        c17 = c
    elif i == 18:
        c18 = c
    elif i == 19:
        c19 = c
    elif i == 20:
        c20 = c
    elif i == 21:
        c21 = c
    elif i == 22:
        c22 = c
    elif i == 23:
        c23 = c
    elif i == 24:
        c24 = c
    elif i == 25:
        c25 = c
    elif i == 26:
        c26 = c
    elif i == 27:
        c27 = c
    elif i == 28:
        c28 = c
    elif i == 29:
        c29 = c
    elif i == 30:
        c30 = c
    elif i == 31:
        c31 = c
    elif i == 32:
        c32 = c
    elif i == 33:
        c33 = c
    elif i == 34:
        c34 = c
    elif i == 35:
        c35 = c
    elif i == 36:
        c36 = c


def checkAvailability(input):
    global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36
    if input < 1 or input > 36:
        return False
    if input == 1:
        return c1 == '1'
    elif input == 2:
        return c2 == '2'
    elif input == 3:
        return c3 == '3'
    elif input == 4:
        return c4 == '4'
    elif input == 5:
        return c5 == '5'
    elif input == 6:
        return c6 == '6'
    elif input == 7:
        return c7 == '7'
    elif input == 8:
        return c8 == '8'
    elif input == 9:
        return c9 == '9'
    elif input == 10:
        return c10 == '10'
    elif input == 11:
        return c11 == '11'
    elif input == 12:
        return c12 == '12'
    elif input == 13:
        return c13 == '13'
    elif input == 14:
        return c14 == '14'
    elif input == 15:
        return c15 == '15'
    elif input == 16:
        return c16 == '16'
    elif input == 17:
        return c17 == '17'
    elif input == 18:
        return c18 == '18'
    elif input == 19:
        return c19 == '19'
    elif input == 20:
        return c20 == '20'
    elif input == 21:
        return c21 == '21'
    elif input == 22:
        return c22 == '22'
    elif input == 23:
        return c23 == '23'
    elif input == 24:
        return c24 == '24'
    elif input == 25:
        return c25 == '25'
    elif input == 26:
        return c26 == '26'
    elif input == 27:
        return c27 == '27'
    elif input == 28:
        return c28 == '28'
    elif input == 29:
        return c29 == '29'
    elif input == 30:
        return c30 == '30'
    elif input == 31:
        return c31 == '31'
    elif input == 32:
        return c32 == '32'
    elif input == 33:
        return c33 == '33'
    elif input == 34:
        return c34 == '34'
    elif input == 35:
        return c35 == '35'
    elif input == 36:
        return c36 == '36'
    return False

def checkWinner(player):
    global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36
    #36 ohne diagonale
    row1_1 = c31 == player and c32 == player and c33 == player and c34 == player
    row1_2 = c32 == player and c33 == player and c34 == player and c35 == player
    row1_3 = c32 == player and c33 == player and c34 == player and c36 == player

    row2_1 = c25 == player and c26 == player and c27 == player and c28 == player
    row2_2 = c26 == player and c27 == player and c28 == player and c29 == player
    row2_3 = c27 == player and c28 == player and c29 == player and c30 == player
    
    row3_1 = c19 == player and c20 == player and c21 == player and c22 == player
    row3_2 = c20 == player and c21 == player and c22 == player and c23 == player
    row3_3 = c21 == player and c22 == player and c23 == player and c24 == player
    
    row4_1 = c13 == player and c14 == player and c15 == player and c16 == player
    row4_2 = c14 == player and c15 == player and c16 == player and c17 == player
    row4_3 = c15 == player and c16 == player and c17 == player and c18 == player
    
    row5_1 = c7 == player and c8 == player and c9 == player and c10 == player
    row5_2 = c8 == player and c9 == player and c10 == player and c11 == player
    row5_3 = c9 == player and c10 == player and c11 == player and c12 == player
    
    row6_1 = c1 == player and c2 == player and c3 == player and c4 == player
    row6_2 = c2 == player and c3 == player and c4 == player and c5 == player
    row6_3 = c3 == player and c4 == player and c5 == player and c6 == player


    column1_1 = c31 == player and c25 == player and c19 == player and c13 == player
    column1_2 = c25 == player and c19 == player and c13 == player and c7 == player
    column1_3 = c19 == player and c13 == player and c7 == player and c1 == player


    column2_1 = c32 == player and c26 == player and c20 == player and c14 == player
    column2_2 = c26 == player and c20 == player and c14 == player and c8 == player
    column2_3 = c20 == player and c14 == player and c8 == player and c2 == player

    column3_1 = c33 == player and c27 == player and c21 == player and c15 == player
    column3_2 = c27 == player and c21 == player and c15 == player and c9 == player
    column3_3 = c21 == player and c15 == player and c9 == player and c3 == player

    column4_1 = c34 == player and c28 == player and c22 == player and c16 == player
    column4_2 = c28 == player and c22 == player and c16 == player and c10 == player
    column4_3 = c22 == player and c16 == player and c10 == player and c4 == player

    column5_1 = c35 == player and c29 == player and c23 == player and c17 == player
    column5_2 = c29 == player and c23 == player and c17 == player and c11 == player
    column5_3 = c23 == player and c17 == player and c11 == player and c5 == player

    column6_1 = c36 == player and c30 == player and c24 == player and c18 == player
    column6_2 = c30 == player and c24 == player and c18 == player and c12 == player
    column6_3 = c24 == player and c18 == player and c12 == player and c6 == player
    



    diagonal1 = c19 == player and c14 == player and c9 == player and c4 == player
    diagonal2_1 = c25 == player and c20 == player and c15 == player and c10 == player
    diagonal2_2 = c20 == player and c15 == player and c10 == player and c5 == player
    
    diagonal3_1 = c31 == player and c26 == player and c21 == player and c16 == player
    diagonal3_2 = c26 == player and c21 == player and c16 == player and c11 == player
    diagonal3_3 = c21 == player and c16 == player and c11 == player and c6 == player
    
    diagonal4_1 = c32 == player and c27 == player and c22 == player and c17 == player
    diagonal4_2 = c27 == player and c22 == player and c17 == player and c12 == player

    diagonal5 = c33 == player and c28 == player and c23 == player and c18 == player



    diagonal6 = c24 == player and c17 == player and c10 == player and c3 == player

    diagonal7_1 = c30 == player and c23 == player and c16 == player and c9 == player
    diagonal7_2 = c23 == player and c16 == player and c9 == player and c2 == player
    
    diagonal8_1 = c36 == player and c29 == player and c22 == player and c15 == player
    diagonal8_2 = c29 == player and c22 == player and c15 == player and c8 == player
    diagonal8_3 = c22 == player and c15 == player and c8 == player and c1 == player
    
    diagonal9_1 = c35 == player and c28 == player and c21 == player and c14 == player
    diagonal9_2 = c28 == player and c21 == player and c14 == player and c7 == player

    diagonal10 = c34 == player and c27 == player and c20 == player and c13 == player


    if row1_1 or row1_2 or row1_3 or row2_1 or row2_2 or row2_3 or row3_1 or row3_2 or row3_3 or row4_1 or row4_2 or row4_3 or row5_1 or row5_2 or row5_3 or row6_1 or row6_2 or row6_3 or column1_1 or column1_2 or column1_3 or column1_1 or column1_2 or column1_3 or column2_1 or column2_2 or column2_3 or column3_1 or column3_2 or column3_3 or column4_1 or column4_2 or column4_3 or column5_1 or column5_2 or column5_3 or column6_1 or column6_2 or column6_3 or diagonal1 or diagonal2_1 or diagonal2_2 or diagonal3_1 or diagonal3_2 or diagonal3_3 or diagonal4_1 or diagonal4_2 or diagonal5 or diagonal6 or diagonal7_1 or diagonal7_2 or diagonal8_1 or diagonal8_2 or diagonal8_3 or diagonal9_1 or diagonal9_2 or diagonal10:
        print(player + " is the winner!")
        return True
    return False

c1, c2, c3, c4, c5, c6, c7, c8, c9 = '', '', '', '', '', '', '', '', ''
currentPlayer = 'X'

while True:
    initializeCharacters()

    print("Welcome to X-O game\n")
    draw()

    counter = 0
    while True:
        print("Turn of", currentPlayer)
        input_val = int(input())

        while not checkAvailability(input_val):
            print("The number is wrong or it's already used")
            print("Enter another number")
            input_val = int(input())

        if counter % 2 == 0:
            replace(input_val, currentPlayer)
            currentPlayer = 'O'
        else:
            replace(input_val, currentPlayer)
            currentPlayer = 'X'

        counter += 1
        draw()

        if checkWinner('X') or checkWinner('O'):
            print()
            break
        elif counter == 9:
            print("Draw! No Winner!")
            break

    print("Do you want to play again?")
    print("1- continue")
    print("2- exit")
    input_val = int(input())
    if input_val != 1:
        break
