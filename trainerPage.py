# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:18:41 2018

@author: Abhishek
"""

from tkinter import *
import trainer


def main_screen():
    global screen
    screen = Tk()
    screen.configure(background='mint cream')
    screen.geometry("400x500")
    screen.title("FRAT Training Model Creater")
    year = StringVar(screen)
    year.set("First")
    course = StringVar(screen)
    course.set("B.Tech")
    branch = StringVar(screen)
    branch.set("CSE")
    section = StringVar(screen)
    section.set("A")
    Label(text = "Welcome to FRAT Trainer", bg = "peach puff", width = "300", height = "2", font = ("Times", 16,"bold"), fg = "dodgerblue").pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Course", bg = 'floral white', font = ("Times", "12", "bold"), fg = 'black').pack()
    m = OptionMenu(screen, course, "B.Tech", "BBA", "BCA", "MBA", "Diploma")
    m.configure(bg = 'misty rose')
    m.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Branch", bg = 'floral white', font = ("Times", "12", "bold"), fg = 'black').pack()
    a = OptionMenu(screen, branch, "CSE", "ME", "EC", "EN","CE")
    a.configure(bg = 'misty rose')
    a.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Year", bg = 'floral white', font = ("Times", "12", "bold"), fg = 'black').pack()
    w = OptionMenu(screen, year, "First", "Second", "Third", "Fourth")
    w.configure(bg = 'misty rose')
    w.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Section", bg = 'floral white', font = ("Times", "12", "bold"), fg = 'black').pack()
    b = OptionMenu(screen, section, "A", "B", "C", "D", "E")
    b.configure(bg = 'misty rose')
    b.pack()
    Label(text = "", bg = 'floral white').pack()
    Button(text = "Create training model", fg = "dark violet", font=("Times","12","bold"), bg = "plum1", height = "2", width = "30", command = lambda : trainer.train(str(year.get()),str(course.get()),str(branch.get()),str(section.get()))).pack()
    
    screen.mainloop()

if __name__=="__main__":
    main_screen() 

