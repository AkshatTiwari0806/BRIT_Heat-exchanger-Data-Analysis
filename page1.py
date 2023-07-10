from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
#functions

def click():
    a=textentry1.get()
    b=textentry2.get()
    c=textentry3.get()
    d=textentry4.get()
    e=tableentry1.get()
    f=tableentry2.get()
    g=tableentry3.get()
    h=tableentry4.get()
    i=tableentry5.get()
    j=tableentry6.get()
    k=tableentry7.get()
    l=tableentry8.get()
    m=tableentry9.get()
    n=tableentry10.get()
    if a and b and c and d and e and f and g and h and i and j and k and l and m and n:
        pass
    else:
        messagebox.showwarning("Invalid", "Please Enter all the fields")
    
   
        
def exit_page():
    Page1.destroy()
    exit()
  

def page_2():
    Page1.destroy()
    import page2  



Page1=Tk()
Page1.title("LEAK DETECTION IN HEAT EXCHANGERS")
#window.geometry("1125x750")
Page1.geometry("1200x800+110+0")
Page1.resizable(0,0)

bgimage=ImageTk.PhotoImage(file="industry photo_page1.jpeg")
'''window.configure(background="#CACAFF")'''
Label(Page1,image=bgimage,bd=0).pack()
mainframe1 = Frame(Page1,bg="white",width=900,height=800)
mainframe1.place(x=155,y=0)
#Label(Page1,bg="white",width=100,height=70).place(x=330,y=0)
#photo1=PhotoImage(file="big.gif")
#Label(mainframe,image=photo1,bg="white").place(x=470,y=15)
Label(mainframe1,text="Details of the System",fg="black",bg="white",font=("Times New Roman",22,"bold")).place(x=330,y=120)
Label(mainframe1,text="Enter Project Name:",fg="black",bg="white",font=("Ariel",14,"bold")).place(x=150,y=30)
Label(mainframe1,text="Enter Project Date:",fg="black",bg="white",font=("Ariel",14,"bold")).place(x=150,y=65)
Label(mainframe1,text="No: of Heat Exchangers:",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=130,y=180)
Label(mainframe1,text="Injection Header Pressure(Pascal):",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=130,y=630)
textentry1 = Entry(mainframe1,width=33,bd=0,bg="white",font=("Ariel",14))
textentry2 = Entry(mainframe1,width=33,bd=0,bg="white",font=("Ariel",14))
textentry3 = Entry(mainframe1,width=21,bd=0,bg="white",font=("Ariel",13))
textentry4 = Entry(mainframe1,width=21,bd=0,bg="white",font=("Ariel",13))
textentry1.place(x=300,y=30)
textentry2.place(x=300,y=65)
textentry3.place(x=300,y=180)
textentry4.place(x=375,y=630)
frame1=Frame(mainframe1,width=300,height=2,bg='black').place(x=300,y=50)
frame2=Frame(mainframe1,width=300,height=2,bg='black').place(x=300,y=85)
frame3=Frame(mainframe1,width=200,height=2,bg='black').place(x=300,y=200)
frame4=Frame(mainframe1,width=190,height=2,bg='black').place(x=375,y=650)
Label(mainframe1,text="Shell Side Details",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=375,y=280)
Label(mainframe1,text="Tube Side Details",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=610,y=280)
Label(mainframe1,text="Fluid:",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=130,y=330)
Label(mainframe1,text="Pressure(Pa):",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=130,y=380)
Label(mainframe1,text="Flow Rate(m3/sec):",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=130,y=430)
Label(mainframe1,text="Inlet Temprature(°C):",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=130,y=480)
Label(mainframe1,text="Outlet Temprature(°C):",fg="black",bg="white",font=("Ariel",13,"bold")).place(x=130,y=530)

''' TABLE '''
tableentry1 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry2 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry3 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry4 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry5 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry6 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry7 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry8 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry9 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry10 = Entry(mainframe1,width=20,bg="white",font=("Ariel",13))
tableentry1.place(x=340,y=325)
tableentry2.place(x=580,y=325)
tableentry3.place(x=340,y=375)
tableentry4.place(x=580,y=375)
tableentry5.place(x=340,y=425)
tableentry6.place(x=580,y=425)
tableentry7.place(x=340,y=475)
tableentry8.place(x=580,y=475)
tableentry9.place(x=340,y=525)
tableentry10.place(x=580,y=525)

"""
Button(window,text="OPEN FILE",bg="#7C7CFC",fg="white",font="none 10 bold").grid(row=0,column=0,sticky=W)
textentry=Entry(window,width=10,bg="white")
textentry.grid(row=3,column=3,sticky=W)
output=Text(window,width=20,height=20,wrap=WORD,bg="white")
output.grid(row=4,column=4,sticky=W)

dictionary={'WAO':'KANTARA'}
"""
Button(Page1,text="EXIT",highlightbackground="#9898F5",fg="black",font="none 25 bold",command=exit_page).place(x=0,y=730)
Button(Page1,text="NEXT",highlightbackground="#9898F5",fg="black",font="none 25 bold",command=page_2).place(x=1125,y=730)
Button(mainframe1,text="SUBMIT",highlightbackground="#9898F5",fg="black",width="10",font="Arial 25 bold",command=click).place(x=370,y=720)
#Page1.attributes('-fullscreen', True)
#Page1.attributes('-topmost', True)
#Page1.overrideredirect(True)

Page1.mainloop()
#coding lifestyle 4u
