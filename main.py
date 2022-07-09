import random
from playsound import playsound
from graphics import *

words = ["ACADEMY", "HANGMAN", "ANCIENT", "COMPANY", "COUNTRY", "ALCOHOL", "SUCCESS", "MANAGER",
         "ABILITY", "COLLEGE", "ECONOMY", "CENTURY", "PROJECT", "MORNING", "PROCESS", "VILLAGE",
         'BECAUSE', 'ANXIETY', 'BROTHER', 'BILLION', 'CIRCUIT', 'COMPANY', 'CONSENT', 'DRAWING',
         'FASHION', 'FOREVER', 'FORMULA', 'FREEDOM', 'HIGHWAY', 'HISTORY', 'HOLIDAY', 'JUSTICE',
         'JOURNAL', 'LIBERTY', 'LOYALTY', 'MAXIMUM', 'MYSTERY', 'OUTCOME', 'OPINION', 'OFFENSE',
         'POPULAR', 'POVERTY', 'PRECISE', 'PROBLEM', 'PURPOSE', 'SERVICE', 'STRANGE', 'SUPPORT',
         'SERIOUS', 'SILENCE', 'SOCIETY', 'SIXTEEN', 'SOMEHOW', 'SMOKING', 'THEATRE', 'TOWARDS',
         'TRAFFIC', 'TROUBLE', 'UNKNOWN', 'VARIETY', 'VIOLENT', 'WARRANT', 'WELCOME', 'WHEREAS',
         'UNIFORM', 'UPGRADE', 'SUPREME', 'ADDRESS', 'AGAINST', 'ANYBODY', 'WORKING', 'UNUSUAL',
         'complex', 'concept', 'council', 'default', 'dynamic', 'edition', 'exactly', 'example',
         'faculty', 'formula', 'gallery', 'fortune', 'highway', 'healthy', 'million', 'network',
         'package', 'premium', 'privacy', 'telecom', 'program', 'suspect', 'tension', 'welfare']

WIDTH = 1000
HEIGHT = 700

def main():

    # pre-drawings and initial conditions

    word = random.choice(words).upper()
    hangman_status = 7
    guessed_letters = []

    win = GraphWin("Scaffold", WIDTH, HEIGHT)
    win.setBackground(color_rgb(209, 237, 242))

    images = []
    for i in range(1, 9):
        image = Image(Point(250, 300), str(i) + ".png")
        images.append(image)

    img = images[hangman_status]
    img.draw(win)

    blank = ' __ __ __ __ __ __ __ '
    blank_space = Text(Point(680, 300), blank)
    blank_space.setSize(20)
    blank_space.setStyle('bold')
    blank_space.draw(win)

    status = Text(Point(680, 50), "Tries left: " + str(hangman_status))
    status.setStyle('bold')
    status.setSize(20)
    status.draw(win)

    main_note = Text(Point(WIDTH/2, 500), "Guess a letter")
    main_note.setStyle('bold')
    main_note.setFace('courier')
    main_note.setSize(25)
    main_note.draw(win)

    sec_note = Text(Point(WIDTH/2-25, 550), "Type here:")
    sec_note.setFace('courier')
    sec_note.setSize(20)
    sec_note.setStyle('bold')
    sec_note.draw(win)

    type_space = Entry(Point(WIDTH/2+70, 550), 2)
    type_space.draw(win)
    type_space.setFill(color_rgb(255, 255, 255))
    type_space.setSize(20)

    CB = Rectangle(Point(WIDTH/2 - 50, 600), Point(WIDTH / 2 + 50, 640))
    CB.setWidth(2)
    CB.setFill('white')
    CB.draw(win)
    CBT = Text(Point(WIDTH / 2, 620), 'CONFIRM')
    CBT.setSize(15)
    CBT.setStyle('bold')
    CBT.draw(win)

    game_again = Rectangle(Point(50, HEIGHT - 130), Point(130, HEIGHT - 80))
    game_again.setWidth(3)
    game_again.setFill(color_rgb(255, 255, 255))
    game_again.draw(win)
    game_again_text = Text(Point(90, HEIGHT - 105), 'AGAIN')
    game_again_text.setStyle('bold')
    game_again_text.draw(win)

    exit_game = Rectangle(Point(50, HEIGHT - 70), Point(130, HEIGHT - 20))
    exit_game.setWidth(3)
    exit_game.setFill(color_rgb(255, 255, 255))
    exit_game.draw(win)
    exit_game_text = Text(Point(90, HEIGHT - 45), 'EXIT')
    exit_game_text.setStyle('bold')
    exit_game_text.draw(win)

    def again_or_exit():
        if p.getX() > 50 and p.getX() < 130 and p.getY() > HEIGHT - 130 and p.getY() < HEIGHT - 80:
            playsound('Button_push.mp3')
            win.close()
            main()
        elif p.getX() > 50 and p.getX() < 130 and p.getY() > HEIGHT - 70 and p.getY() < HEIGHT - 20:
            playsound('Button_push.mp3')
            win.close()

    # the main game body

    you_won = False

    while hangman_status > 0 and you_won == False:

        guess = ''

        p = win.getMouse()

        again_or_exit()

        if p.getX() < WIDTH/2 - 50 or p.getX() > WIDTH / 2 + 50 or p.getY() < 600 or p.getY() > 640:
            continue
        else:
            guess = type_space.getText().upper()
            type_space.setText('')
            playsound('Button_push.mp3')

        if not guess.isalpha() or len(guess) != 1 or guess == ' ' or guess == '':
            main_note.setText("Only single letters")
            continue

        if guess in word and not (guess in guessed_letters):
            main_note.setText(guess.upper() + " is in the word")
            guessed_letters.append(guess)
            blank = word
            for letter in word:
                if not letter.upper() in guessed_letters:
                    blank = blank.replace(letter, ' __ ')
                blank_space.setText(blank)

        elif guess in guessed_letters:
            main_note.setText(guess.upper() + " is already chosen")

        else:
            guessed_letters.append(guess)
            main_note.setText(guess.upper() + ' is not in the word.')
            hangman_status -= 1
            img = images[hangman_status]
            img.draw(win)
            status.setText("Tries left: " + str(hangman_status))

        if blank == word:
            you_won = True

    # after-game part

    type_space.undraw()
    CB.undraw()
    CBT.undraw()
    sec_note.undraw()

    if you_won:
        blank_space.setText(word)
        win.setBackground(color_rgb(152, 251, 152))
        main_note.setText("YOU WON!")
        img2 = Image(Point(WIDTH/2+330, HEIGHT/2+220), "pic0.png")
        img2.draw(win)
        playsound('Ding.mp3')

    else:
        blank_space.setText("The right answer: " + word)
        win.setBackground(color_rgb(216, 36, 41))
        main_note.setText("YOU LOST...")
        img3 = Image(Point(WIDTH-200, HEIGHT - 70), 'pic1.png')
        img3.draw(win)
        playsound('Error.wav')

    while True:
        p = win.getMouse()
        again_or_exit()
        continue

main()
