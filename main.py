from tkinter import *
import ctypes
import random
import tkinter

# For a sharper window
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Setup
root = Tk()
root.title('Type Speed Test')

# Setting the starting window dimensions
root.geometry('700x700')

# Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


# functions
def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # Deleting one from the right side.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            # set the next Letter Lavbel
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass


def resetWritingLabels():
    # Text List
    possibleTexts = [
        'Football, also known as soccer, is one of the most popular sports in the world. It is played by millions of people of all ages in various countries. The game is played with a round ball on a rectangular field with two teams of eleven players each. The objective of the game is to score more goals than the opposing team. Football has a long and rich history, dating back to ancient times. The modern version of the game originated in England in the 19th century and quickly spread throughout Europe and beyond. Today, there are numerous professional football leagues and international competitions that attract millions of viewers and fans. Football is more than just a game, it is a way of life for many people. It brings communities together and fosters a sense of camaraderie among players and fans alike. The sport is known for its intense rivalries and passionate supporters, who often travel long distances to support their favorite teams.',
        'California is a state located on the West Coast of the United States. It is known for its warm climate, beautiful beaches, and diverse culture. The state is home to many famous attractions, such as Hollywood, Disneyland, and the Golden Gate Bridge. California is also known for its wine country, where visitors can tour vineyards and taste locally produced wines. The state has a vibrant economy, with many technology companies and startups headquartered in cities like San Francisco and Silicon Valley. California is also home to many prestigious universities, including Stanford and the University of California, Berkeley. Despite its many attractions, California faces challenges such as wildfires, drought, and high cost of living.',
        'Barbies playing football might seem like an unusual sight, but its not as rare as you might think. These days, the famous dolls are taking on new hobbies and sports, and football is one of them. With their tiny feet and nimble bodies, Barbies make for surprisingly good football players. Of course, the Barbies dont play in a regular football league – they have their own special competitions. The Barbie Football League is a popular event among fans of the dolls, and its not hard to see why. The players are dressed in colourful kits and have all the right moves, even if they are a bit smaller than your average footballer. One of the most exciting things about Barbies playing football is the way they bring people together. Fans of the dolls and the sport come from all over to watch the matches and cheer on their favourite players.'
    ]
    # Chosing one of the texts randomly with the choice function
    text = random.choice(possibleTexts).lower()
    # defining where the text is split
    splitPoint = 0
    # This is where the text is that is already written
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # Here is the text which will be written
    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    # This label shows the user which letter he now has to press
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # this label shows the user how much time has gone by
    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    # Binding callbacks to functions after a certain amount of time.
    root.after(60000, stopTest)
    root.after(1000, addSecond)


def stopTest():
    global writeAble
    writeAble = False

    # Calculating the amount of words
    amountWords = len(labelLeft.cget('text').split(' '))

    # Destroy all unwanted widgets.
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    # Display the test results with a formatted string
    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restart the game
    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)


def restart():
    # Destry result widgets
    ResultLabel.destroy()
    ResultButton.destroy()

    # re-setup writing labels.
    resetWritingLabels()


def addSecond():
    # Add a second to the counter.

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    # call this function again after one second if the time is not over.
    if writeAble:
        root.after(1000, addSecond)


# This will start the Test
resetWritingLabels()

# Start the mainloop
root.mainloop()