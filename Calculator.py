from tkinter import *

root = Tk()

root.title("Calculator")

e = Entry(root,width=40,borderwidth=25)#Entry is used to get INPUT
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)





def Button_click(number):#create function click
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def Button_clear():
        e.delete(0,END)


def Button_equal():
    secound=e.get()
    e.delete(0,END)

    if math == "addition":
       e.insert(0,f_num + int(secound))

    if math == "subtraction":
    	e.insert(0,f_num - int(secound))

    if math == "multiplication":
       e.insert(0,f_num * int(secound))

def Button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0,END)


def Button_multi():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0,END)

def Button_sub():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0,END)



   
#Define Buttons
mybutton_1 = Button(root,text="1",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(1))#Button is created
mybutton_2 = Button(root,text="2",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(2))
mybutton_3 = Button(root,text="3",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(3))

mybutton_4 = Button(root,text="4",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(4))
mybutton_5 = Button(root,text="5",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(5))
mybutton_6 = Button(root,text="6",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(6))

mybutton_7 = Button(root,text="7",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(7))
mybutton_8 = Button(root,text="8",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(8))
mybutton_9 = Button(root,text="9",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(9))

mybutton_0 = Button(root,text="0",padx=40,pady=20,bg="skyblue",command=lambda:Button_click(0))

Button_add = Button(root,text="+",padx=40,pady=20,bg="skyblue",command=Button_add)
Button_equal=Button(root,text="=",padx=40,pady=20,bg="skyblue",command=Button_equal)
Button_multi=Button(root,text="*",padx=40,pady=20,bg="skyblue",command=Button_multi)
Button_clear=Button(root,text="clear",padx=40,pady=20,bg="red",fg="white",command=Button_clear)
Button_sub=Button(root,text="-",padx=40,pady=20,bg="skyblue",command=Button_sub)

#Put Buttons on screen
mybutton_1.grid(row=1,column=0)
mybutton_2.grid(row=1,column=1)
mybutton_3.grid(row=1,column=2)

mybutton_4.grid(row=2,column=0)
mybutton_5.grid(row=2,column=1)
mybutton_6.grid(row=2,column=2)

mybutton_7.grid(row=3,column=0)
mybutton_8.grid(row=3,column=1)
mybutton_9.grid(row=3,column=2)

mybutton_0.grid(row=4,column=1)
Button_equal.grid(row=4,column=2)
Button_sub.grid(row=4,column=0)

Button_add.grid(row=5,column=0)
Button_clear.grid(row=5,column=1)
Button_multi.grid(row=5,column=2)
                 
root.mainloop()#mainloop for close.



##########################
#NOTE:- e.get() is used to move to e=Entry(root)
##########################