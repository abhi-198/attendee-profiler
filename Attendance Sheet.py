from tkinter import *

def main_screen():
    global screen
    screen = Tk()
    screen.configure(background = 'floral white')
    screen.geometry("1000x800")
    screen.title("List Of Students")
    Label(text = "FRAS Attendance Sheet", bg = "azure", width = "300", height = "2", font = ("Ariel", 13), fg = "maroon1").pack()
    Label(text = "", bg = 'floral white').pack()
    Label(text = "List Of Students", bg = "floral white", font = ("Ariel", 13), fg = "maroon1").pack()
    Label(text = "", bg = 'floral white').pack()
    Label(screen, text = "Present Students", fg = 'blue', bg = 'floral white', font = ('Ariel',11)).place(x = 30, y = 170)
    Entry(screen, text = "").place(x = 30, y = 200)
    Label(screen, text = "Attendance", fg = 'blue', bg = 'floral white', font = ('Ariel',11)).place(x = 250, y = 170)
    Label(screen, text = "Absent Students", fg = 'blue', bg = 'floral white', font = ('Ariel',11)).place(x = 600, y = 170)
    Entry(screen, text = "").place(x = 600, y = 200)
    Label(screen, text = "Attendance", fg = 'blue', bg = 'floral white', font = ('Ariel',11)).place(x = 850, y = 170)
    var1 = IntVar()
    Checkbutton(screen, text="", variable=var1, bg = 'floral white').place(x = 280, y = 200)
    var2 = IntVar()
    Checkbutton(screen, text="", variable=var2, bg = 'floral white').place(x = 880, y = 200)
    screen.mainloop()
main_screen()    
