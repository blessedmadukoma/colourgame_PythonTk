from tkinter import *
import random

#List of possible colours
colours = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'White', 'Purple', 'Brown']

score = 0

#Time limit: 30 seconds
time = 30

#Function that starts the game
def startGame(event):

    if time==30:

        #Start the countdown
        countdown()

    #Run function to choose the next colour
    nextColour()

#Next colour function
def nextColour():
    global time
    global score

    # Condition if game is in play
    if time > 0:
        # Activate Entry box
        colour_entry.focus_set()

        # Check if value input is in lowercase
        if colour_entry.get().lower() == colours[1].lower():
           #increment
            score += 1

        # Clear the entry box for the next colour
        colour_entry.delete(0, END)

        # Shuffle the colours for the next colour
        random.shuffle(colours)

        # Change the colour to type by changing the text
        # and colour to a random colour value
        colour.config(fg= str(colours[1]), text=str(colours[0]))

        #Update the score
        scoreLabel.config(text="Score: " + str(score))


#Countdown Function
def countdown():

    global time

    #Condition if a game is in play
    if time > 0:

        # decrement the time value
        time -=1

        #update the time left label
        timeLabel.config(text="Time left: " + str(time))

        #run the function again after one second
        timeLabel.after(1000, countdown)


#The Driver Code
if __name__=='__main__':

    tk = Tk()

    #Setting the title
    tk.title("Colour Game")

    #Setting the geometry of the window
    tk.geometry("350x350")

    #Introduction Label
    welcome = Label(tk, text="WELCOME TO MY COLOUR GAME!")
    welcome.pack()

    #Setting an instruction
    instructions = Label(tk,  text = "Type in the colour of the words and not the word itself!!")
    instructions.pack()

    #Create a score label
    scoreLabel = Label(tk, text="Score: "+str(score), font=('Helvetica',12))
    scoreLabel.pack()

    #Create a time label
    timeLabel = Label(tk, text="Time Left: "+str(time), font=('Helvetica',12))
    timeLabel.pack()

    #create a colour label
    colour = Label(tk, font=('Helvetica',12))
    colour.pack()

    #Entry box for input from user
    colour_entry = Entry(tk)

    colour_entry.focus_set()
    tk.bind('<Return>', startGame)

    colour_entry.pack()


    tk.mainloop()