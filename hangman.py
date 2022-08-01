
from tkinter import *
from tkinter import messagebox
import getpass

score = 0
run = True
# main loop
while run:
    root = Tk()
    root.geometry('905x700')
    root.title('HANG MAN')
    root.config(bg = '#191919')
    count = 0
    win_count = 0

    # choosing word
    print("Get ready to play Hangman!")
    while 1:

        
        selected_word = getpass.getpass("Player 1, input your word: ").lower()
        if selected_word.isalpha():
            break
        else:
            print("\n\nThe Entered Word Contains Special Characters, Spaces or Numbers Please enter only Alphabets\n\n")
            continue

    
    # creation of word dashes variables
    x = 550
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#ffffff",font=("arial",40), padx = 10)'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,500))
        
    #letters icon
    al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))
        
    # hangman images
    h123 = ['h0','h1','h2','h3','h4','h5','h6']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
    #letters placement
    button = [['b1','a',300,595],['b2','b',370,595],['b3','c',440,595],['b4','d',510,595],['b5','e',580,595],['b6','f',650,595],['b7','g',720,595],['b8','h',790,595],['b9','i',860,595],['b10','j',930,595],['b11','k',1000,595],['b12','l',1070,595],['b13','m',1140,595],['b14','n',300,655],['b15','o',370,655],['b16','p',440,655],['b17','q',510,655],['b18','r',580,655],['b19','s',650,655],['b20','t',720,655],['b21','u',790,655],['b22','v',860,655],['b23','w',930,655],['b24','x',1000,655],['b25','y',1070,655],['b26','z',1140,655]]

    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#191919",activebackground="#191919",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
    #hangman placement
    han = [['c1','h0'],['c2','h1'],['c3','h2'],['c4','h3'],['c5','h4'],['c6','h5'],['c7','h6']]
    for p1 in han:
        exec('{}=Label(root,bg="#191919",image={})'.format(p1[0],p1[1]))

    # placement of first hangman image
    c1.place(x = 650,y =- 50)
    
    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(root,bd = 0,command = close,bg="#191919",activebackground = "#191919",font = 10,image = e1,height = 81,width=189)
    ex.place(x=1350,y=10)
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
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,700,-50))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST! THE WORD WAS '+selected_word+'\n WANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()

