from tkinter import *

def login(screen1):
    screen1.destroy()
    screen1=Tk()
    screen1.configure(background='floral white')
    screen1.geometry("400x400")
    screen1.title("FRAT Login")
    Label(screen1, text = "FRAT Login Welcomes you", bg = "peach puff", width = "300", height = "2", font = ("Times", 14), fg = "SeaGreen3").pack()
    Label(screen1, text = "", bg = 'floral white').pack()
    Label(screen1, text = "Username * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
    Entry(screen1, text = "").pack()
    Label(screen1, text = "", bg = 'floral white').pack()
    Label(screen1, text = "Password * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
    Entry(screen1, text = "").pack()
    Button(screen1, text = "Login", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "20", command = login).place(bordermode=OUTSIDE, x=125, y=220)
   

def main_screen():
    global screen
    screen = Tk()
    screen.configure(background='floral white')
    screen.geometry("400x400")
    screen.title("FRAT Login")
    Label(text = "FRAT Login", bg = "peach puff", width = "300", height = "2", font = ("Times","14","bold"), fg = "SeaGreen3").pack()
    Label(text = "", bg = 'floral white').pack()
    Button(text = "Login", fg = "black", bg = "SeaGreen1",font=("Times","10") ,height = "2", width = "30", command = lambda: login(screen)).place(bordermode=OUTSIDE, x=90, y=100)
   
    

    screen.mainloop()
    
if __name__=="__main__":
    main_screen()    
