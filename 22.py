import sys
from tkinter import *
import tkinter as tk
import pickle
import os

window=Tk()
window.wm_iconbitmap('pill.ico')
window.title("Medical Store")
window.geometry("420x400")
photo=PhotoImage(file="store.gif")
w=Label(window, image=photo).pack()

Label(window, text="Medical Store", bg="crimson",fg="white", font="meiro 22", width="420").pack()



class medicine(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Add Medicine")
        self.wm_iconbitmap('pill.ico')
        
        Label(self,text="Medicine Id.").grid(row=0)
        Label(self,text="Medicine Name").grid(row=1)
        Label(self,text="Cost").grid(row=2)
        Label(self, text="Expiry Date").grid(row=3)
        Label(self, text="Manufactured Date").grid(row=4)
        Label(self, text="Supplier Name" ).grid(row=5)
        Label(self, text="Rack No." ).grid(row=6)
        Label(self, text="Cabinet No." ).grid(row=7)

        self.e1= tk.Entry(self)
        self.e2= tk.Entry(self)
        self.e3= tk.Entry(self)
        self.e4= tk.Entry(self)
        self.e5= tk.Entry(self)
        self.e6= tk.Entry(self)
        self.e7= tk.Entry(self)
        self.e8= tk.Entry(self)



        self.e1.grid(row=0 , column=1)
        self.e2.grid(row=1 , column=1) 
        self.e3.grid(row=2 , column=1)
        self.e4.grid(row=3 , column=1)
        self.e5.grid(row=4 , column=1)
        self.e6.grid(row=5 , column=1)
        self.e7.grid(row=6 , column=1)
        self.e8.grid(row=7 , column=1)
        
        
        
        self.button = tk.Button(self, text='Quit', command=self.destroy).grid(row=8, column=1, pady=4)
        self.button2 = tk.Button(self, text='Done', command=self.on_button).grid(row=8, column=2, pady=4)

        

    def on_button(self):

        
        self.x1=self.e1.get()
        self.x2=self.e2.get()
        self.x3=self.e3.get()
        self.x4=self.e4.get()
        self.x5=self.e5.get()
        self.x6=self.e6.get()
        self.x7=self.e7.get()
        self.x8=self.e8.get()
        
    
  
        self.f1=open('medicine.log','ab+')
        self.l1=[self.x1,self.x2,self.x3,self.x4,self.x5,self.x6,self.x7,self.x8 ]
        if len(self.l1[0])>=1:
            pickle.dump(self.l1,self.f1)
            self.textin="Successfully Saved!"
        else:
            self.textin=" Not Saved"
        self.f1.close()
        self.window=tk.Toplevel()
        label=tk.Label(self.window, text=self.textin)
        label.pack(side="top", fill="both", padx=24, pady=18)
        self.button3 = tk.Button(self.window, text='Okay', command=self.destroyall).pack()
        mainloop()
    def destroyall(self):
        self.window.destroy()
        self.destroy()





class library3(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        Label(self,text="Enter Password").grid(row=0)
        self.e1= tk.Entry(self,show='•')
        self.e1.grid(row=0 , column=1)
        
        self.button = tk.Button(self, text='Cancel', command=self.destroy).grid(row=6, column=1, pady=4)
        self.button2 = tk.Button(self, text='Okay', command=self.on_button3).grid(row=6, column=2, pady=4)
    def on_button3(self):
        if self.e1.get() == "password":
            self.window1=tk.Toplevel()
            self.button = tk.Button(self.window1, text='See whole record', command=self.on_button4).grid(row=6, column=1, pady=4)
            self.button2 = tk.Button(self.window1, text="See one record", command=self.on_button5).grid(row=6, column=2, pady=4)
            self.destroy()
        else:
            self.window1 = tk.Toplevel()
            label = tk.Label(self.window1, text="Wrong password")
            label.pack(side="top", fill="both", padx=24, pady=10)
            self.button = tk.Button(self.window1, text='Quit', command=self.window1.destroy).pack()
    def on_button4(self):
        self.f2=open("medicine.log",'rb')
        self.objs = []
        while True:
            try:
                self.objs.append(pickle.load(self.f2))
            except EOFError:
                break
        self.window2=tk.Toplevel()


        Label(self.window2,text="MEDICINE ID.").grid(row=0,column=0 )
        Label(self.window2,text="MEDICINE NAME").grid(row=0,column=1)
        Label(self.window2,text="COST").grid(row=0 , column=2)
        Label(self.window2,text="EXPIRY DATE").grid(row=0,column=3)
        Label(self.window2,text="MANUFACTURE DATE").grid(row=0,column=4)

        Label(self.window2,text="SUPPLIER NAME").grid(row=0 ,column=5)
        Label(self.window2,text="RACK NO.").grid(row=0,column=6)
        Label(self.window2,text="CABINET NO.").grid(row=0,column=7)
        for i in range (len(self.objs)) :
            for j in range (8) :
                label = tk.Label(self.window2, text=self.objs[i][j])
                label.grid(row=i+1,column=j)
        self.f2.close()
        b1=tk.Button(self.window2,text="Exit",command=self.window2.destroy).grid(column=8)
    def on_button5(self):
        self.window3=tk.Toplevel()
        Label(self.window3,text="Medicine Id.").grid(row=0)
        self.e1= tk.Entry(self.window3)
        self.e1.grid(row=0 , column=1)
        
        self.button = tk.Button(self.window3, text='Quit', command=self.window3.destroy).grid(row=6, column=1, pady=4)
        self.button = tk.Button(self.window3, text='Okay', command=self.on_button6).grid(row=6, column=2, pady=4)
        mainloop()
    def on_button6(self):
        self.f2=open("medicine.log","rb")
        self.objs=[]
        while True:
            try:
                self.objs.append(pickle.load(self.f2))
            except EOFError:
                break
        self.stu=[]
            
        self.f2.close()
        for self.i in self.objs:
            if self.i[0]==self.e1.get():
                self.stu=self.i
        self.window4=tk.Toplevel()

        Label(self.window4,text="MEDICINE ID.").grid(row=0,column=0 )
        Label(self.window4,text="MEDICINE NAME").grid(row=0,column=1)
        Label(self.window4,text="COST").grid(row=0 , column=2)
        Label(self.window4,text="EXPIRY DATE").grid(row=0,column=3)
        Label(self.window4,text="MANUFACTURE DATE").grid(row=0,column=4)

        Label(self.window4,text="SUPPLIER NAME").grid(row=0 ,column=5)
        Label(self.window4,text="RACK NO.").grid(row=0,column=6)
        Label(self.window4,text="CABINET NO.").grid(row=0,column=7)
        
        for i in range (8) :
            label = tk.Label(self.window4, text=self.stu[i])
            label.grid(row=1,column=i)
        self.button = tk.Button(self.window4, text='Okay', command=self.destroyall2).grid(row=2, column=8)

    def destroyall2(self):
        self.window4.destroy()
        self.window3.destroy()
        self.window1.destroy()








class purchase(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        Label(self,text="Medicine Id.").grid(row=0, sticky=W)
        Label(self,text="Medicine Name").grid(row=1, sticky=W)
        Label(self,text="Units To Be Purchased").grid(row=2, sticky=W )


        self.e1= tk.Entry(self)
        self.e2= tk.Entry(self)
        self.e3= tk.Entry(self)




        self.e1.grid(row=0 , column=1)
        self.e2.grid(row=1 , column=1) 
        self.e3.grid(row=2 , column=1)


        
    

        
        self.button = tk.Button(self, text='Quit', command=self.destroy).grid(row=6, column=1, pady=4)
        self.button = tk.Button(self, text='Okay', command=self.on_button6).grid(row=6, column=2, pady=4)
        mainloop()
    def on_button6(self):
        self.f2=open("medicine.log","rb")
        self.objs=[]
        while True:
            try:
                self.objs.append(pickle.load(self.f2))
            except EOFError:
                break
        self.stu=[]
            
        self.f2.close()
        for self.i in self.objs:
            if self.i[0]==self.e1.get():
                self.stu=self.i
        self.window4=tk.Toplevel()

        Label(self.window4,text="Medicine Id.").grid(row=0,column=0,sticky=W )
        Label(self.window4,text="Medicine Name").grid(row=1,column=0,sticky=W )
        Label(self.window4,text="Cost").grid(row=2 , column=0,sticky=W )
        Label(self.window4,text="Expiry Date").grid(row=3,column=0,sticky=W )



        for i in range (4) :
            label = tk.Label(self.window4, text=self.stu[i])
            label.grid(row=i,column=1,sticky=W)

        Label(self.window4,text="Units To Be Purchased").grid(row=4,column=0,sticky=W)
        Label(self.window4,text=str(self.e3.get())).grid(row=4,column=1,sticky=W)
        Label(self.window4,text="Total Amount To Be Paid (Rs.)").grid(row=5,column=0,sticky=W)
        Label(self.window4,text=str(int(self.stu[2])*int(self.e3.get()))).grid(row=5,column=1,sticky=W)
        self.button = tk.Button(self.window4, text='Okay', command=self.destroyall2).grid(row=6, column=2,sticky=W)

    def destroyall2(self):

        
    
  
        self.f1=open('bill.log','ab+')
        self.l1=[self.stu[1],self.stu[2],self.stu[3],self.e3.get(),int(self.stu[2])*int(self.e3.get()) ]
        if len(self.l1[0])>=1:
            pickle.dump(self.l1,self.f1)
        else:
            pass
        self.f1.close()
        self.window4.destroy()
        self.destroy()
        







        


def start_admin():
    c=library3()
    return (c)



        

def add():
    a= medicine()
    return (a)

def pur():
    b=purchase()
    return(b)

        


tk.Button(window, text=" Admin Menu", command=start_admin, width="14",bg="light pink").pack(side=LEFT)
tk.Button(window, text=" Purchase ",command=pur, width="13",bg="light pink").pack(side=LEFT)
tk.Button(window, text=" Add Medicine ",command=add, width="15",bg="light pink").pack(side=LEFT)


b1=Button(window, text=" Exit ",command=window.destroy, width="13",bg="light pink").pack(side=LEFT)
window.mainloop()

