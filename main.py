import tkinter as tk
from tkinter import messagebox
import functions

root = tk.Tk()
root.geometry("200x300")

def dinnerMenu():
    temp_dinner = functions.getDinner()
    messagebox.showinfo(title = "Dinner Restaurant", message = temp_dinner)
    
dinnerButton = tk.Button(root, text = "Random Dinner Restaurant", command = lambda:[functions.setDinner(), dinnerMenu()])
dinnerButton.pack()

def breakfastMenu():
    temp_breakfast = functions.getBreakfast()
    messagebox.showinfo(title = "Breakfast Restaurant", message = temp_breakfast)
    
breakfastButton = tk.Button(root, text = "Random Breakfast Restaurant", command = lambda:[functions.setBreakfast(), breakfastMenu()])
breakfastButton.pack()

def desertMenu():
    temp_desert = functions.getDesert()
    messagebox.showinfo(title = "Desert Restaurant", message = temp_desert)
    
dinnerButton = tk.Button(root, text = "Random Desert Restaurant", command = lambda:[functions.setDesert(), desertMenu()])
dinnerButton.pack()

root.mainloop()
