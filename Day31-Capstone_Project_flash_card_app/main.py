#import libraries
from tkinter import *
from matplotlib import image
from numpy import flip
import pandas as pd
import random

# Const definition
BACKGROUND_COLOR = "#B1DDC6"

#Global definition
current_card = {}
to_learn = {}

#Load the french words data
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
try:
    data = pd.read_csv(r'data\words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv(r"data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


#function definition
#function to select the next card
def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    
#function flip cards
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

#function to save     
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv(r"data\words_to_learn.csv", index=0)
    
    next_card()

window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Canvas setting for the flash card
canvas = Canvas(width=800, height=526)
#review the file relative path if you're on linux/macos
card_front_img = PhotoImage(file=r"images\card_front.png")
card_back_img = PhotoImage(file=r"images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons for the guessing 
#review the file relative path if you're on linux/macos
cross_image = PhotoImage(file=r"images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

#review the file relative path if you're on linux/macos
check_image = PhotoImage(file=r"images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

#init a random word to generate
next_card()

window.mainloop()