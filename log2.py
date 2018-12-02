import mysql.connector
from tkinter import *
from tkinter import messagebox
import faceRec

def faculty(screen):
    screen.destroy()
    screen = Tk()
    screen.configure(background='floral white')
    screen.geometry("400x400")
    screen.title("FRAT User")
    year = StringVar(screen)
    year.set("First")
    course = StringVar(screen)
    course.set("B.Tech")
    branch = StringVar(screen)
    branch.set("CSE")
    section = StringVar(screen)
    section.set("A")
    Label(text = "Welcome to FRAT", bg = "peach puff", width = "300", height = "2", font = ("Times", 16), fg = "SeaGreen3").pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Course", bg = 'floral white', font = ("Times", 10), fg = 'hot pink').pack()
    m = OptionMenu(screen, course, "B.Tech", "BBA", "BCA", "MBA", "Diploma")
    m.configure(bg = 'SeaGreen1')
    m.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Branch", bg = 'floral white', font = ("Times", 10), fg = 'hot pink').pack()
    a = OptionMenu(screen, branch, "CSE", "ME", "EC", "EN","CE")
    a.configure(bg = 'SeaGreen1')
    a.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Year", bg = 'floral white', font = ("Times", 10), fg = 'hot pink').pack()
    w = OptionMenu(screen, year, "First", "Second", "Third", "Fourth")
    w.configure(bg = 'SeaGreen1')
    w.pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "Section", bg = 'floral white', font = ("Times", 10), fg = 'hot pink').pack()
    b = OptionMenu(screen, section, "A", "B", "C", "D", "E")
    b.configure(bg = 'SeaGreen1')
    b.pack()
    Label(text = "", bg = 'floral white').pack()
    Button(master=screen, text = "Start Scanning", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "30", command = lambda : faceRec.face_rec(str(year.get()),str(course.get()),str(branch.get()),str(section.get()))).pack()
    
def loginCheck(user,password,screen):
    if user!="" and password!="":
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="fras")
        mycursor= mydb.cursor()
        query="select * from access where userid like '"+user+"' and password like '"+password+"';"
        mycursor.execute(query)
        result=mycursor.fetchall()
        if result!=[]:
            faculty(screen)
        else:
            messagebox.showerror("LOGIN","User ID and Password is Incorrect...")
            login(screen)
    else:
        messagebox.showwarning("LOGIN","User ID and Password Required...")
        login(screen)


def login(screen1):

    screen1.destroy()
    screen1=Tk()
    screen1.configure(background='floral white')
    screen1.geometry("400x400")
    screen1.title("FRAT Login")
        
    Label(screen1, text = "FRAT Login Welcomes you", bg = "peach puff", width = "300", height = "2", font = ("Times", 14), fg = "SeaGreen3").pack()
    Label(screen1, text = "", bg = 'floral white').pack()
    Label(screen1, text = "Username * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
        
    user=StringVar()
    password= StringVar()
    Entry(screen1, text = " ", textvariable=user).pack()
    

    Label(screen1, text = "", bg = 'floral white').pack()
    Label(screen1, text = "Password * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
    
    Entry(screen1, text = " ", textvariable=password).pack()
    
    Button(screen1, text = "Login", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "20", command =lambda : loginCheck(str(user.get()),str(password.get()),screen1)).place(bordermode=OUTSIDE, x=125, y=220)
   

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
