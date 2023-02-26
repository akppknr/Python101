from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() # นีคือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # นี่คือชื่อโปรแกรม
GUI.geometry('300x400') # นี่คือขนาดของโปรแกรม

L1 = Label(GUI,text='Home Work Ep.2',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
#################################
def Button1():
     text = 'สร้างไฟล์ใหม่'
     messagebox.showinfo('New File',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B1 = ttk.Button(FB1,text='New File',command=Button1)
B1.pack(ipadx=20,ipady=20)
####################################
def Button2():
     text = 'เปิดไฟล์'
     messagebox.showinfo('Open',text)

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=150)
B2 = ttk.Button(FB2,text='Open',command=Button2)
B2.pack(ipadx=20,ipady=20)
####################################
def Button3():
     text = 'แก้ไขไฟล์'
     messagebox.showinfo('Edit',text)

FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=100,y=220)
B3 = ttk.Button(FB3,text='Edit',command=Button3)
B3.pack(ipadx=20,ipady=20)
####################################
def Button4():
     text = 'บันทึกไฟล์'
     messagebox.showinfo('Save',text)

FB4 = Frame(GUI) #คล้ายกระดาน
FB4.place(x=100,y=290)
B4 = ttk.Button(FB4,text='Save',command=Button4)
B4.pack(ipadx=20,ipady=20)
####################################

GUI.mainloop()

