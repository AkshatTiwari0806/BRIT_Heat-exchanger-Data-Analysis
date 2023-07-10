from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfilename
import numpy as np
import matplotlib.pyplot as plt
import csv
#functions
def exit_page():
    Page4.destroy()
    exit()
def open_file():
    Page4.filename = askopenfilename(initialdir="../",title="Select a File",filetypes=[("CSV File", "*.csv"),("All Files", "*.*")])
    
def plot():
    plot=Label(image=myimag)
    plot.pack()
    output2.config(text="Graph plotted successfully\nCH1 and CH7 detected as Inlet and Outlet detector\n")
    
def analyze():
    
    output2.config(text="")
    plot.config(image=None)
    output2.config(text="Graph plotted succesguvhvhvhvsfully\nCH1 and CH7 detected as Inlet and Outlet detector\n")
        


Page4=Tk()
Page4.title("LEAK DETECTION IN HEAT EXCHANGERS")
Page4.geometry("1200x800+110+0")
Page4.resizable(0,0)
myimag=ImageTk.PhotoImage(file="plot.png")
myimag2=ImageTk.PhotoImage(file="analyze.png")

Button(Page4,text="PLOT",highlightbackground="#9898F5",fg="black",font="none 22 bold",command=plot).place(x=400,y=585)
Button(Page4,text="Analyze",highlightbackground="#9898F5",fg="black",font="none 22 bold",command=analyze).place(x=700,y=585)
Button(Page4,text="OPEN FILE",highlightbackground="#9898F5",fg="black",font="none 22 bold",command=open_file).place(x=0,y=20)
Button(Page4,text="EXIT",highlightbackground="#9898F5",fg="black",font="none 25 bold",command=exit_page).place(x=0,y=730)
Button(Page4,text="NEXT",highlightbackground="#9898F5",fg="black",font="none 25 bold",command=None).place(x=1125,y=730)
output2=Label(Page4,text="",width=80,height=6,bg="light blue",borderwidth=10,font=("Ariel",15,"bold"),highlightbackground = "black", highlightcolor= "black",highlightthickness=1)
output2.config(highlightbackground = "black", highlightcolor= "black")
output2.place(x=180,y=630)
Page4.mainloop()

'''with open('20220620-data.csv', mode ='r') as file:   
        
       # reading the CSV file
       csvFile = csv.reader(file)
       plt.rcParams["figure.figsize"] = [7.00, 3.50]
       plt.rcParams["figure.autolayout"] = True
       csvFile.plot()
       csvFile.show()'''