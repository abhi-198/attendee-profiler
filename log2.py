from tkinter import *

def login():
    screen1 = Tk()
    screen1.configure(background='floral white')
    screen1.geometry("400x400")
    screen1.title("FRAT Login")
    Label(screen1, text = "FRAT Login Welcomes you", bg = "peach puff", width = "300", height = "2", font = ("Algerian", 13), fg = "SeaGreen3").pack()
    Label(screen1, text = "", bg = 'floral white').pack()
    Label(screen1, text = "Username * ", bg = 'floral white', fg = 'hot pink', font = ('calibri',10)).pack()
    Entry(screen1, text = "").pack()
    Label(screen1, text = "", bg = 'floral white').pack()
    Label(screen1, text = "Password * ", bg = 'floral white', fg = 'hot pink', font = ('calibri',10)).pack()
    Entry(screen1, text = "").pack()
    Button(screen1, text = "Login", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "30", command = login).place(bordermode=OUTSIDE, x=70, y=250)
   

def main_screen():
    global screen
    screen = Tk()
    screen.configure(background='floral white')
    screen.geometry("400x400")
    screen.title("FRAT Login/Registration")
    Label(text = "FRAT Login/Registration", bg = "peach puff", width = "300", height = "2", font = ("Algerian", 13), fg = "SeaGreen3").pack()
    Label(text = "", bg = 'floral white').pack()
    Button(text = "Login", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "30", command = login).place(bordermode=OUTSIDE, x=70, y=100)
   
    

    screen.mainloop()
main_screen()    
