from time import sleep

isValidGuess = False
tableGenerating1 = "Generating Tic-Tac-Toe table."
tableGenerating2 = "Generating Tic-Tac-Toe table.."
tableGenerating3 = "Generating Tic-Tac-Toe table..."
programQuit = False
playCount = 0
inRow = False

# set up the 2d array
table = [ 
    ["?", "?", "?"],
    ["?", "?", "?"],
    ["?", "?", "?"]
]

# prints the intro
print("WELCOME TO MY TIC TAC TOE!")
print("\nGET READY!")
sleep(1.0)

# the whole process is made into a function, to make repeating easy!
def guessSeq(): 
    global lastInput
    global lastInputPrint
    global lastCoOrd
    global lastCoOrdSplit
    global playCount

# takes user input for either X or O and checks for a valid input.
    lastInput = str(input("\nX OR O?\n"))
    if lastInput == "X":
        lastInputPrint = str((lastInput))

    elif lastInput == "O":
        lastInputPrint = str((lastInput))

    else:
        print("Please enter a valid guess!")
        lastInputPrint = "?"

# prints user letter choice and takes coordinates from the user
    print("you entered", lastInputPrint)
    lastCoOrd = str(input("which coordinates? please separate by a comma (e.g. 0,0 top left)\n"))
    
# splits the user's input for coords and reads them back.
    lastCoOrdSplit = lastCoOrd.split(",")
    print("your co-ordnates were...", lastCoOrdSplit)

# suspense!
    sleep(0.5)
    print(tableGenerating1)
    sleep(0.5)
    print(tableGenerating2)
    sleep(0.5)
    print(tableGenerating3)
    sleep(0.5)


# takes the coordinates from the user input and alters the table accordingly
    table[int(lastCoOrdSplit[1])][int(lastCoOrdSplit[0])] = lastInputPrint
# prints the table
    for row in table:
        print(row)
    
    
    # Add this after printing the table
    if check_win():
        print(f"Player {lastInputPrint} wins!")
        return True
    
    # Check for draw
    if playCount == 9:
        print("It's a draw!")
        return True
        
    return False

def check_win():
    # Check rows
    for row in table:
        if row[0] == row[1] == row[2] != "?":
            return True
    
    # Check columns
    for col in range(3):
        if table[0][col] == table[1][col] == table[2][col] != "?":
            return True
    
    # Check diagonals
    if table[0][0] == table[1][1] == table[2][2] != "?":
        return True
    if table[0][2] == table[1][1] == table[2][0] != "?":
        return True
    
    return False

# the main loop, which repeats the guessSeq function until a player wins or the game is a draw.
while programQuit == False:
    if not inRow:
        inRow = guessSeq()
       
       


