from tkinter import *

def login():
    print("Login session started")

def main_screen():
    global screen
    screen = Tk()
    screen.configure(background='floral white')
    screen.geometry("400x400")
    screen.title("FRAT User")
    variable = StringVar(screen)
    variable.set("First")
    variable1 = StringVar(screen)
    variable1.set("B.Tech")
    variable2 = StringVar(screen)
    variable2.set("CSE")
    variable3 = StringVar(screen)
    variable3.set("A")
    Label(text = "Welcome to FRAT", bg = "peach puff", width = "300", height = "2", font = ("Calibri", 11), fg = "SeaGreen3").pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Course", bg = 'floral white', font = ("Calibri", 10), fg = 'hot pink').pack()
    m = OptionMenu(screen, variable1, "B.Tech", "BBA", "BCA", "MBA", "Diploma")
    m.configure(bg = 'SeaGreen1')
    m.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Branch", bg = 'floral white', font = ("Calibri", 10), fg = 'hot pink').pack()
    a = OptionMenu(screen, variable2, "CSE", "Mechanical", "EC", "EEE", "EN")
    a.configure(bg = 'SeaGreen1')
    a.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Year", bg = 'floral white', font = ("Calibri", 10), fg = 'hot pink').pack()
    w = OptionMenu(screen, variable, "First", "Second", "Third", "Fourth")
    w.configure(bg = 'SeaGreen1')
    w.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Section", bg = 'floral white', font = ("Calibri", 10), fg = 'hot pink').pack()
    b = OptionMenu(screen, variable3, "A", "B", "C", "D", "E")
    b.configure(bg = 'SeaGreen1')
    b.pack()
    Label(text = "", bg = 'floral white').pack()
    Button(text = "Start Scanning", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "30", command = login).pack() 
   
    

    screen.mainloop()
main_screen()    
