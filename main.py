import tkinter as tk
from tkinter import messagebox
import functions

root = tk.Tk()
root.geometry("200x300")

def dinnerMenu():
    temp_dinner = functions.getDinner()
    messagebox.showinfo(title = "Dinner Resturant", message = temp_dinner)
    
dinnerButton = tk.Button(root, text = "Random Dinner Resturant", command = lambda:[functions.setDinner(), dinnerMenu()])
dinnerButton.pack()

def breakfastMenu():
    temp_breakfast = functions.getBreakfast()
    messagebox.showinfo(title = "Breakfast Resturant", message = temp_breakfast)
    
breakfastButton = tk.Button(root, text = "Random Breakfast Resturant", command = lambda:[functions.setBreakfast(), breakfastMenu()])
breakfastButton.pack()

def desertMenu():
    temp_desert = functions.getDesert()
    messagebox.showinfo(title = "Desert Resturant", message = temp_desert)
    
dinnerButton = tk.Button(root, text = "Random Desert Resturant", command = lambda:[functions.setDesert(), desertMenu()])
dinnerButton.pack()

root.mainloop()
