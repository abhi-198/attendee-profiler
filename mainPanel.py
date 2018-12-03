# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:44:17 2018

@author: Abhishek
"""

import tkinter as tk
import mysql.connector
import trainer

def createID(name,user,password,new_password,screen):
    if user!="" and password!="" and name!="":
        try:
            if password == new_password:
                db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="fras")
                mycursor= db.cursor()
                query="insert into access values(%s,%s,%s)"
                val=(name,user,password)
                mycursor.execute(query,val)
                db.commit()
                
                if mycursor.rowcount==1:
                    tk.messagebox.showinfo("Insert","Faculty added successfully...")
                    add_faculty(screen)
                else:
                    tk.messagebox.showerror("LOGIN","User ID and Password is Incorrect...")
                    add_faculty(screen)
            else:
                 tk.messagebox("warning","Password mismatch...")
                 return
        except mysql.connector.Error as error:
            tk.messagebox.showerror("Insert Error",error)
            add_faculty(screen)
            
    else: 
        tk.messagebox.showwarning("LOGIN","User ID and Password Required...")
        add_faculty(screen) 
    

def deleteID(name,user,password,new_password,screen):
    if user!="" and password!="" and name!="":
        try:
            if password == new_password:
                db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="fras")
                mycursor= db.cursor()
                query="delete from access where userid like '"+user+"' and password like '"+password+"';"
                mycursor.execute(query)
                db.commit()
                
                if mycursor.rowcount==1:
                    tk.messagebox.showinfo("Insert","Faculty deleted successfully...")
                    add_faculty(screen)
                else:
                    tk.messagebox.showerror("LOGIN","User ID and Password is Incorrect...")
                    add_faculty(screen)
            else:
                 tk.messagebox("warning","Password mismatch...")
                 return
        except mysql.connector.Error as error:
            tk.messagebox.showerror("Delete Error",error)
            add_faculty(screen)
            
    else: 
        tk.messagebox.showwarning("LOGIN","User ID and Password Required...")
        add_faculty(screen) 
    
    
def add_faculty(screen):
    screen.destroy()
    screen = tk.Tk()
    screen.configure(background="mint cream")
    screen.geometry("400x500")
    screen.title("FRAS Faculty Access")
    tk.Label(screen, text = "FRAT Login Welcomes you", bg = "peach puff", width = "300", height = "2", font = ("Times", 14), fg = "SeaGreen3").pack()
    
    name= tk.StringVar()
    tk.Label(screen, text = "", bg = 'floral white').pack()
    tk.Label(screen, text = "Name * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
    
    tk.Entry(screen, text = " ", textvariable=name).pack()
    
    tk.Label(screen, text = "", bg = 'floral white').pack()
    tk.Label(screen, text = "Username * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
        
    user= tk.StringVar()
    password= tk.StringVar()
    new_password= tk.StringVar()
    tk.Entry(screen, text = " ", textvariable=user).pack()
    
    tk.Label(screen, text = " ", bg = 'floral white').pack()
    tk.Label(screen, text = "Password * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
    
    tk.Entry(screen, text = " ", textvariable=password,show="*").pack()
    
    tk.Label(screen, text = " ", bg = 'floral white').pack()
    tk.Label(screen, text = "Confirm Password * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
    
    tk.Entry(screen, text = " ", textvariable=new_password,show="*").pack()
    
    tk.Button(screen, text = "Create ID", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "20", command =lambda : createID(str(name.get()),str(user.get()),str(password.get()),str(new_password.get()),screen)).place(bordermode=tk.OUTSIDE, x=40, y=350)
    tk.Button(screen, text = "Delete ID", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "20", command =lambda : deleteID(str(name.get()),str(user.get()),str(password.get()),str(new_password.get()),screen)).place(bordermode=tk.OUTSIDE, x=220, y=350)
    tk.Button(screen, text = "Home Panel", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "20", command = lambda: panel(screen.destroy())).place(bordermode=tk.OUTSIDE, x=125, y=400)
        
    
def trainerPage(screen):
    screen.destroy()
    screen = tk.Tk()
    screen.configure(background='mint cream')
    screen.geometry("400x500")
    screen.title("FRAT Training Model Creater")
    year = tk.StringVar(screen)
    year.set("First")
    course = tk.StringVar(screen)
    course.set("B.Tech")
    branch = tk.StringVar(screen)
    branch.set("CSE")
    section = tk.StringVar(screen)
    section.set("A")
    tk.Label(text = "Welcome to FRAT Trainer", bg = "peach puff", width = "300", height = "2", font = ("Times", 16,"bold"), fg = "dodgerblue").pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Label(text = "Course", bg = 'floral white', font = ("Times", "12", "bold"), fg = 'black').pack()
    m = tk.OptionMenu(screen, course, "B.Tech", "BBA", "BCA", "MBA", "Diploma")
    m.configure(bg = 'misty rose')
    m.pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Label(text = "Branch", bg = 'floral white', font = ("Times", "12", "bold"), fg = 'black').pack()
    a = tk.OptionMenu(screen, branch, "CSE", "ME", "EC", "EN","CE")
    a.configure(bg = 'misty rose')
    a.pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Label(text = "Year", bg = 'floral white', font = ("Times", "12", "bold"), fg = 'black').pack()
    w = tk.OptionMenu(screen, year, "First", "Second", "Third", "Fourth")
    w.configure(bg = 'misty rose')
    w.pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Label(text = "Section", bg = 'floral white', font = ("Times", "12", "bold"), fg = 'black').pack()
    b = tk.OptionMenu(screen, section, "A", "B", "C", "D", "E")
    b.configure(bg = 'misty rose')
    b.pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Button(text = "Create training model", fg = "dark violet", font=("Times","12","bold"), bg = "plum1", height = "2", width = "30", command = lambda : trainer.train(str(year.get()),str(course.get()),str(branch.get()),str(section.get()))).pack()
    
    
def panel(screen=None):
    screen = tk.Tk()
    screen.configure(background='mint cream')
    screen.geometry("400x500")
    screen.title("FRAS Menu")
    tk.Label(text = "Welcome to FRAS Admin Menu", bg = "peach puff", width = "300", height = "2", font = ("Times", 16,"bold"), fg = "dodgerblue").pack()
    tk.Label(text = "", bg = 'floral white').pack()
    
    tk.Button(text = "Create training model", fg = "dark violet", font=("Times","12","bold"), bg = "plum1", height = "2", width = "30", command = lambda : trainerPage(screen)).pack()
    tk.Label(width="20",height="2").pack()
    tk.Button(text = "Add faculty", fg = "dark violet", font=("Times","12","bold"), bg = "plum1", height = "2", width = "30", command = lambda : add_faculty(screen)).pack()
    
    screen.mainloop()
    

if __name__=="__main__":
    panel()