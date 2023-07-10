from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

#functions
def page_3():
    Page2.destroy()
    import page3
    
def exit_page():
    Page2.destroy()
    exit()
    
def click():
    a1=text2entry1.get()
    a2=text2entry2.get()
    a3=text2entry3.get()
    a4=text2entry4.get()
    a5=text2entry5.get()
    if a1 and a2 and a3 and a4 and a5:
        pass
    else:
        messagebox.showwarning("Invalid", "Please Enter all the fields")
    #from page1 import i,c
    #activity=(18*((a1*a2*i)**0.5))/(a3*a4)
    #counting_time=a2/(36*i)
    #no_of_detectors=c+2
    output.config(text="Calculated Activity(bq):__________\nCalculated Counting Time(sec):__________\nNumber of Detectors:___________")
    
    
 

Page2=Tk()
Page2.title("LEAK DETECTION IN HEAT EXCHANGERS")
Page2.geometry("1200x800+110+0")
Page2.resizable(0,0)

bgimage=ImageTk.PhotoImage(file="industry photo_page1.jpeg")
Label(Page2,image=bgimage,bd=0).pack()
mainframe2 = Frame(Page2,bg="white",width=900,height=800)
mainframe2.place(x=155,y=0)
Label(mainframe2,text="Experimental Details-1",fg="black",bg="white",font=("Times New Roman",25,"bold")).place(x=320,y=20)
Label(mainframe2,text="Type of Tracer used : ",fg="black",bg="white",font=("Ariel",15,"bold")).place(x=50,y=90)
clicked = StringVar()
clicked.set("Molybdenum-99")
drop = OptionMenu(mainframe2,clicked,"Molybdenum-99","Technetium-99m","Bromine-82")
drop.place(x=250,y=90)
Label(mainframe2,text="Background Radiation counts rate(cps):",fg="black",bg="white",font=("Ariel",15,"bold")).place(x=50,y=140)
Label(mainframe2,text="Shell side Volume(m3):",fg="black",bg="white",font=("Ariel",15,"bold")).place(x=50,y=200)
Label(mainframe2,text="Calibration factor(cps/Bq/m3):",fg="black",bg="white",font=("Ariel",15,"bold")).place(x=50,y=260)
Label(mainframe2,text="Estimated Leak Rate(%):",fg="black",bg="white",font=("Ariel",15,"bold")).place(x=50,y=320)
Label(mainframe2,text="Time of Injection(hh:mm:ss)",fg="black",bg="white",font=("Ariel",15,"bold")).place(x=50,y=380)
text2entry1 = Entry(mainframe2,width=22,bd=0,bg="white",font=("Ariel",14))
text2entry2 = Entry(mainframe2,width=22,bd=0,bg="white",font=("Ariel",14))
text2entry3 = Entry(mainframe2,width=22,bd=0,bg="white",font=("Ariel",14))
text2entry4 = Entry(mainframe2,width=22,bd=0,bg="white",font=("Ariel",14))
text2entry5 = Entry(mainframe2,width=22,bd=0,bg="white",font=("Ariel",14))
text2entry1.place(x=360,y=140)
text2entry2.place(x=360,y=200)
text2entry3.place(x=360,y=260)
text2entry4.place(x=360,y=320)
text2entry5.place(x=360,y=380)
frame21=Frame(mainframe2,width=200,height=2,bg='black').place(x=360,y=160)
frame22=Frame(mainframe2,width=200,height=2,bg='black').place(x=360,y=220)
frame23=Frame(mainframe2,width=200,height=2,bg='black').place(x=360,y=280)
frame24=Frame(mainframe2,width=200,height=2,bg='black').place(x=360,y=340)
frame25=Frame(mainframe2,width=200,height=2,bg='black').place(x=360,y=400)

output=Label(Page2,text="",width=50,height=7,bg="light blue",borderwidth=10,font=("Ariel",15,"bold"),highlightbackground = "black", highlightcolor= "black",highlightthickness=1)
output.config(highlightbackground = "black", highlightcolor= "black")
output.place(x=330,y=510)


Button(Page2,text="EXIT",highlightbackground="#9898F5",fg="black",font="none 25 bold",command=exit_page).place(x=0,y=730)
Button(Page2,text="NEXT",highlightbackground="#9898F5",fg="black",font="none 25 bold",command=page_3).place(x=1125,y=730)
Button(mainframe2,text="SUBMIT",highlightbackground="#9898F5",fg="black",width="10",font="Arial 25 bold",command=click).place(x=370,y=720)
Page2.mainloop()