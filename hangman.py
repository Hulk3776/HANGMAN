
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring

RUN = True
SCORE = 0
WRONG_COUNT = 0  #wrong number of attempts
CORRECT_COUNT = 0 # correct number of attempts
DASHES_X_COORDINATE_START = 685
DASHES_X_INTERVAL = 70
DASHES_Y_COORDINATE_START = 500
HANGMAN_X_COORDINATE = 675
HANGMAN_Y_COORDINATE = -50
BUTTON_X_COORDINATE_LINE_1 = 300
BUTTON_X_INTERVAL = 70
BUTTON_Y_COORDINATE_LINE_1 = 595
BUTTON_Y_COORDINATE_LINE_2 = 655
BG_BLACK = '#191919'


# FUNCTIONS: 
def close():
        """
        1. This function helps to close the program using a exit button

        """
        global RUN
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            RUN = False
            root.destroy()

def check(letter,button):
        """
        1. This function checks the entered character in the selected_word, whether it exists or not
        2. If character exists in selected_word it replaces all the dashes with characters
        3. Else it will show number of wrong attempts and score

        """
        global WRONG_COUNT,CORRECT_COUNT,RUN,SCORE
        exec(f'{button}.destroy()')
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    CORRECT_COUNT += 1
                    exec(f'd{i}.config(text="{letter.upper()}")')
            if CORRECT_COUNT == len(selected_word):
                SCORE += 1
                answer = messagebox.askyesno('WIN','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    RUN = True
                    root.destroy()   
                else:
                    RUN = False
                    root.destroy()
        else:
            WRONG_COUNT += 1
            attempts_left = 'NUMBER OF ATTEMPTS LEFT:'+str(6 - WRONG_COUNT)
            attempt_place = Label(root,text = attempts_left,bg = "#fff",font = ("consolas",25))
            attempt_place.place(x = 10,y = 100)
            exec(f'hangman_cutout{WRONG_COUNT}.destroy()')
            exec(f'hangman_cutout{WRONG_COUNT+1}.place(x={HANGMAN_X_COORDINATE},y={HANGMAN_Y_COORDINATE})')
            if WRONG_COUNT == 6:
                answer = messagebox.askyesno('GAME-OVER',f'YOU LOST! THE WORD WAS {selected_word.upper()} \n WANT TO PLAY AGAIN?')
                if answer == True:
                    RUN = True
                    SCORE = 0
                    root.destroy()
                else:
                    RUN = False
                    root.destroy()     



# main loop
"""
1. This is the main loop of the program it contains all the methods from tkinter and user defined methods.

"""
while RUN:
    root = Tk()
    root.attributes('-fullscreen', True)
    root.title('HANGMAN')
    root.config(bg = f'{BG_BLACK}')
    WRONG_COUNT = 0  #wrong number of attempts
    CORRECT_COUNT = 0 # correct number of attempts
    root.withdraw() # Hides Root Black Screen
    while 1:
        
        selected_word = askstring('Player 1', f'\n\n\n{" "*10}Get ready to play Hangman!{" "*10}\n\n\n{" "*10}Enter a word to guess{" "*10}\n\n',
                                    show="*")
        if selected_word.isalpha():
            root.deiconify() # bringing the main root window back
            break
        else:
            messagebox.showinfo("Invalid Character","\n\nThe Entered Word Contains Special Characters, Spaces or Numbers Please enter only Alphabets\n\n")
            continue

    
    # creation of word dashes variables
    x = DASHES_X_COORDINATE_START-(DASHES_X_INTERVAL*(len(selected_word)//2)) # places or maintains the dashes in the center
    for i in range(0,len(selected_word)):
        x += DASHES_X_INTERVAL
        exec(f'd{i}=Label(root,text="_",bg="#ffffff",font=("consolas",40), padx = 10)')
        exec(f'd{i}.place(x={x},y={DASHES_Y_COORDINATE_START})')
        
    #letters icon
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in letters:
        exec(f'{letter}=PhotoImage(file="{letter}.png")')
        
    # hangman images
    hangman_images = ['h0','h1','h2','h3','h4','h5','h6']
    for hangman in hangman_images:
        exec(f'{hangman}=PhotoImage(file="{hangman}.png")')
        
    #letters placement
    buttons = []
    for button_letter in range(1, len(letters)+1):
        button_list = []
        button_list.extend([f'b{button_letter}',letters[button_letter-1],BUTTON_X_COORDINATE_LINE_1+(BUTTON_X_INTERVAL*((button_letter-1)%13)),BUTTON_Y_COORDINATE_LINE_1 if button_letter < 14 else BUTTON_Y_COORDINATE_LINE_2])
        buttons.append(button_list)

    # For bringing buttons to main screen
    for button in buttons:
        # button press check function
        exec(f'{button[0]}=Button(root,bd=0,command=lambda:check("{button[1]}","{button[0]}"),bg="{BG_BLACK}",activebackground="{BG_BLACK}",font=10,image={button[1]})')
        
        exec(f'{button[0]}.place(x={button[2]},y={button[3]})')
        
    #hangman placement
    hangman_placement = [['hangman_cutout1','h0'],['hangman_cutout2','h1'],['hangman_cutout3','h2'],
    ['hangman_cutout4','h3'],['hangman_cutout5','h4'],['hangman_cutout6','h5'],['hangman_cutout7','h6']]
    for placement in hangman_placement:
        exec(f'{placement[0]}=Label(root,bg="{BG_BLACK}",image={placement[1]})')

    # placement of first hangman image
    hangman_cutout1.place(x = HANGMAN_X_COORDINATE,y = HANGMAN_Y_COORDINATE)
    
    
            
    exit_png = PhotoImage(file = 'exit.png')
    # exit button - execute close function in command
    exit_button = Button(root,bd = 0,command = close,bg=f"{BG_BLACK}",activebackground = f"{BG_BLACK}",font = 10,
                        image = exit_png,height = 81,width=189)
    
    exit_button.place(x=1345,y=10)

    main_score = 'SCORE:'+str(SCORE)
    score_place = Label(root,text = main_score,bg = "#fff",font = ("consolas",25))
    score_place.place(x = 10,y = 10)

    
        
    root.mainloop()

#made exe using - pyinstaller --onefile -w 'hangman.py'
