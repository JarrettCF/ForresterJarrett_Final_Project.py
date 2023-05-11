#This Code allows for the user to input and delete games. 
#These games are organized by different categories and can be deleted at any time.
import tkinter as tk
from tkinter import ttk

        #Creates the application and gives the application the title of "Game Categories".
class Application(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.parent.title("Game Categories")
        #Inputs the label of GAME CATEGORIES
        ttk.Label(text="GAME CATEGORIES").grid(row=0,column=0,columnspan=4,sticky="n")
        #Inputs the label of "Add" which allows for the user to and games of their choice
        ttk.Button(text="Add",command=self.add_game).grid(row=1,column=0,sticky="w")
        #Inputs the label of "Delete" which allows for the user to delete any games that they have added
        ttk.Button(text="Delete").grid(row=2,column=0,sticky="w")
        #Inputs the label of "Exit" which allows for the user to exit the entire program
        ttk.Button(text="Exit",command=lambda:self.parent.destroy()).grid(row=3,column=2,sticky="se")

        #Inputs the headings and set them at a height that puts them at the top of the program
        self.tree = ttk.Treeview(height=15,column=("Title","Genre","Rating"))
        #Inputs the heading of "Title" and positivly identifies its location with the anchor
        self.tree.heading("#0",text="Title",anchor="w")
        #Inputs the heading of "Title" and positivly identifies its location with the anchor
        self.tree.heading("#1",text="Genre",anchor="w")
        #Inputs the heading of "Title" and positivly identifies its location with the anchor
        self.tree.heading("#2",text="Rating",anchor="w")
        #Inputs the heading of "Title" and positivly identifies its location with the anchor
        self.tree.heading("#3",text="Status",anchor="w")
        self.tree.grid(row=1,column=1,rowspan=2,columnspan=2,sticky="nsew")

    #Inputs the input the the user puts when adding a new game into the system
    def add_game(self):
        self.addGameWindow = tk.Toplevel(self.parent)
        self.addClass = NewGame(self.parent,self.addGameWindow)

#Inputs the title of "new game" inbedded in the "Add" button
class NewGame(tk.Frame):
    def __init__(self,parent,child,*args,**kwargs):
        tk.Frame.__init__(self,child)
        self.parent = parent
        self.child = child
        #Gives the title "Add Game"
        self.child.title("Add Game")

        #Locates the title of "New Game" in the up left hand corner
        ttk.Label(self.child,text="Add Game").grid(row=0,column=0,sticky="nsew")

#Allows for the application to be looped as long as the user doesn't press the "Exit" button
if __name__ == "__main__":
    app = tk.Tk()
    Application(app)
    app.mainloop()