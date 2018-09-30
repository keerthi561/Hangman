import curses
import random
def RemainingLetters(Letters, guess) :
    if guess in Letters :
        return Letters.replace(guess," ") 

def WordEqualsToGuess(Word, Guesses) :
     return len(set(Guesses)) == len(set(AlphabetsInWord(Word)))

def AlphabetsInWord(Word) :
    return [ch for ch in Word if ch.isalpha()]

def GuessedLetters(Word,Guesses) :
    Space = " "
    Hifen = "-"
    Underscore ="_"
    StringGuessed = ""
    for ch in Word :
        if ch == Space or ch == Hifen :
            StringGuessed += ch
        elif ch in Guesses :
            StringGuessed += ch
        else :
            StringGuessed += Underscore
    return StringGuessed 

def AlreadyEntered(guess,AllGuesses):
    return guess in AllGuesses

Filenames = "animals.py countries.py fruits.py sports.py cars.py"
filename = random.choice(Filenames.split(" "))
file = open(filename, "r")
F1 = file.read()
Word = random.choice(F1.split("\n"))
#Word = "keer th-i"
Word = Word.upper()

Hangman = ['''
   +---+
       |
       |
       |
       |
       |
 =========''','''

   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

stdscr = curses.initscr()
stdscr.clear()
max_height, max_width = stdscr.getmaxyx()
h = max_height
w = max_width

h1 = h // 4; w1 = w // 2
h2 = h // 2; w2 = w // 2
h3 = h // 4; w3 = w // 2
h4 = h // 2; w4 = w // 2
h5 = h // 2; w5 = w // 4

y1 = 1; x1 = 1
y2 = h // 2; x2 = 1
y3 = h // 4; x3 = 0
y4 = 1; x4 = w // 2
y5 = h // 2; x5 = w // 2

win1 = curses.newwin(h1, w1, y1, x1)
win2 = curses.newwin(h2, w2, y2, x2)
win3 = curses.newwin(h3, w3, y3, x3)
win4 = curses.newwin(h4, w4, y4, x4)
win5 = curses.newwin(h5, w5, y5, x5)

stdscr.refresh()
win5_y1 = 4; win5_x1 = 4
win5.addstr(win5_y1, win5_x1, "Hint:", curses.A_REVERSE)
win5.refresh()

Slicing = -3
filename = (filename[:Slicing]).upper()
win5_y2 = 4; win5_x2 = 10
win5.addstr(win5_y2, win5_x2, filename, curses.A_BOLD)
win5.refresh()

turns = len(Hangman)
Letters ="abcdefghijklmnopqrstuvwxyz".upper()
Guesses = ""
AllGuesses = ""
FinalIndex = turns -1 
FinalPicture = Hangman[FinalIndex]
win2.addstr(FinalPicture)
win2.refresh()
win2.addstr("\nFinal Picture",curses.A_REVERSE)
win2.refresh()

curses.curs_set(False)
win3_y = 2; win3_x = 4
win3.addstr(win3_y, win3_x, GuessedLetters(Word, Guesses))
win3.refresh()

while turns > 0 :
    win1_y = 2; win1_x = 4
    win1.addstr(win1_y, win1_x,"\nGuess a letter from\n ", curses.A_BOLD)
    win1.refresh()

    for ch in Letters:
        win1.addstr(ch.upper()+" ")
        win1.refresh()

    win3_y1 = 4; win3_x1 = 4
    Guess = int(win3.getch(win3_y1, win3_x1))
    win3.refresh()
    guess = (chr(Guess)).upper()
    win3.delch(win3_y1, win3_x1)
    win3.refresh()

    if AlreadyEntered(guess,AllGuesses) :
        continue
    AllGuesses += guess
    Letters = RemainingLetters(Letters, guess)
    
    if guess in Word :
        Guesses += guess
    else :
        turns -= 1
        win4.addstr(Hangman[FinalIndex-turns],curses.A_BOLD)
        win4.refresh()

    win3.addstr(win3_y, win3_x, GuessedLetters(Word, Guesses))
    win3.refresh()

    if WordEqualsToGuess(Word, Guesses):
        win3.addstr("\nCongratultions,you won the game\n", curses.A_STANDOUT)
        win3.refresh()
        win3.addstr("\nEnter any key to ")
        win3.addstr("EXIT",curses.A_STANDOUT)
        win3.refresh()
        break
    
    if turns == 0 :
        win3.addstr("\nSorry, you lost the game\n",curses.A_STANDOUT)
        win3.refresh()
        win3.addstr("\nEnter any key to ")
        win3.addstr("EXIT",curses.A_STANDOUT)
        win3.refresh()
        win3.addstr(win3_y, win3_x, Word)
        win3.refresh()
        break
    
    win4.clear()
stdscr.getkey()
curses.endwin()

