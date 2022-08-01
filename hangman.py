
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.simpledialog import askstring

run = True
score = 0
# main loop
while run:
    root = Tk()
    
    # root.geometry('905x700')
    root.attributes('-fullscreen', True)
    root.title('HANGMAN')
    root.config(bg = '#191919')
    count = 0  #number of attempts
    win_count = 0 # choosing word
    print("Get ready to play Hangman!")
    root.withdraw() # Hides Root Black Screen
    while 1:
        
        
        selected_word = askstring('Player 1', f'\n\n\n{" "*10}Get ready to play Hangman!{" "*10}\n\n\n{" "*10}Enter a word to guess{" "*10}\n\n', show="*")
        if selected_word.isalpha():
            root.deiconify() # bringing the main root window back
            break
        else:
            print("\n\nThe Entered Word Contains Special Characters, Spaces or Numbers Please enter only Alphabets\n\n")
            continue

    
    # creation of word dashes variables
    x = 685-(70*(len(selected_word)//2)) # places or maintains the dashes in the center
    for i in range(0,len(selected_word)):
        x += 70
        exec('d{}=Label(root,text="_",bg="#ffffff",font=("arial",40), padx = 10)'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,500))
        
    #letters icon
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in letters:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))
        
    # hangman images
    hangman_images = ['h0','h1','h2','h3','h4','h5','h6']
    for hangman in hangman_images:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
    #letters placement
    buttons = [['b1','a',300,595],['b2','b',370,595],['b3','c',440,595],['b4','d',510,595],['b5','e',580,595],['b6','f',650,595],['b7','g',720,595],['b8','h',790,595],['b9','i',860,595],['b10','j',930,595],['b11','k',1000,595],['b12','l',1070,595],['b13','m',1140,595],['b14','n',300,655],['b15','o',370,655],['b16','p',440,655],['b17','q',510,655],['b18','r',580,655],['b19','s',650,655],['b20','t',720,655],['b21','u',790,655],['b22','v',860,655],['b23','w',930,655],['b24','x',1000,655],['b25','y',1070,655],['b26','z',1140,655]]

    for button in buttons:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#191919",activebackground="#191919",font=10,image={})'.format(button[0],button[1],button[0],button[1]))
        exec('{}.place(x={},y={})'.format(button[0],button[2],button[3]))
        
    #hangman placement
    hangman_placement = [['c1','h0'],['c2','h1'],['c3','h2'],['c4','h3'],['c5','h4'],['c6','h5'],['c7','h6']]
    for placement in hangman_placement:
        exec('{}=Label(root,bg="#191919",image={})'.format(placement[0],placement[1]))

    # placement of first hangman image
    c1.place(x = 650,y =- 50)
    
    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    exit_png = PhotoImage(file = 'exit.png')
    exit_button = Button(root,bd = 0,command = close,bg="#191919",activebackground = "#191919",font = 10,image = exit_png,height = 81,width=189)
    exit_button.place(x=1350,y=10)
    s2 = 'SCORE:'+str(score)
    s1 = Label(root,text = s2,bg = "#fff",font = ("arial",25))
    s1.place(x = 10,y = 10)

    # button press check function
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            s2 = 'NUMBER OF ATTEMPTS LEFT:'+str(6 - count)
            s1 = Label(root,text = s2,bg = "#fff",font = ("arial",25))
            s1.place(x = 10,y = 100)
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,700,-50))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER',f'YOU LOST! THE WORD WAS {selected_word} \n WANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()

