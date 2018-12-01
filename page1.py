from tkinter import *
import faceRec


def main_screen():
    global screen
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
    
    screen.mainloop()

if __name__=="__main__":
    main_screen() 

