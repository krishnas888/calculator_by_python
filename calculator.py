from tkinter import *
from tkinter import ttk
 
 #Main class of calculator
class Application(Frame):
    # note Frame is basically is used to group and organize other widgets. so it's kind of like a container object for all the widgets the application is going to use.
 
    def __init__(self, master):
        #this function is usefull to initize to that instance
        #self variable is reference to the current instance of the class
        #master variable represents the parent widget.
        #super() function is a built in function
        super(Application, self).__init__(master)
        self.task=""
        self.UserIn= StringVar()
        self.grid()
        self.creat_widgets()

    #Creating a fuction that will be responce for creating art buttons for caculator
    def creat_widgets(self):

        self.user_input = Entry(self, bg = "white",bd = 20,
        insertwidth = 2, width = 20,
        font=("Verdana", 20, "bold"),textvariable=self.UserIn,justify = RIGHT)
        #entry widget is basically used to accept single line textr stings from a user.
        self.user_input.grid(columnspan = 4)

        self.user_input.insert(0,"0")

        test_size = 16
        padx_size = 23
        padx_mid_size=25
        pady_size=18
        self.button1 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "7", padx = padx_size, pady = pady_size, font = ("Halvetica", test_size, "bold",),
        command = lambda : self.buttonClick(7))
        self.button1.grid(row = 2, column = 0, sticky = W)

        self.button2 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "8", padx = padx_mid_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(8))
        self.button2.grid(row = 2, column = 1, sticky = W)

        self.button3 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "9", padx = padx_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(9))
        self.button3.grid(row = 2, column = 2, sticky = W)

        self.button4 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "4", padx = padx_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(4))
        self.button4.grid(row = 3, column = 0, sticky = W)

        self.button5 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "5", padx =padx_mid_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(5))
        self.button5.grid(row = 3, column = 1, sticky = W)

        self.button6 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "6", padx = padx_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(6))
        self.button6.grid(row = 3, column = 2, sticky = W)

        self.button7 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "1", padx = padx_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(1))
        self.button7.grid(row = 4, column = 0, sticky = W)

        self.button8 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "2", padx =padx_mid_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(2))
        self.button8.grid(row = 4, column = 1, sticky = W)

        self.button9 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "3", padx = padx_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(3))
        self.button9.grid(row = 4, column = 2, sticky = W)

        self.button10 = Button(self, bg = "#333333",bd = 12,fg="white",
        text = "0", padx = padx_size, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick(0))
        self.button10.grid(row = 5, column = 0, sticky = W)

        self.AddButton = Button(self, bg = "#FF8F00",bd = 12,
        text = "+", padx = 26, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick("+"))
        self.AddButton.grid(row = 2, column = 3, sticky = W)

        self.SubButton = Button(self, bg = "#FF8F00",bd = 12,
        text = "-", padx = 29, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick("-"))
        self.SubButton.grid(row = 3, column = 3, sticky = W)

        self.MultButton = Button(self, bg = "#FF8F00",bd = 12,
        text = "*", padx = 28, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick("*"))
        self.MultButton.grid(row = 4, column = 3, sticky = W)

        self.DiviButton = Button(self, bg = "#FF8F00",bd = 12,
        text = "/", padx = 29, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command = lambda : self.buttonClick("/"))
        self.DiviButton.grid(row = 5, column = 3, sticky = W)

        self.EqualButton = Button(self, bg = "#FF8F00",bd = 12,
        text = "=", padx = 80, pady = pady_size, font = ("Halvetica", test_size, "bold"),
        command =self.CalculateTask)
        self.EqualButton.grid(row = 5, column = 1, sticky = W,columnspan=2)

        self.ClearButton = Button(self, bg = "#D9D9D9",bd = 12,
        text = "AC", padx = 28, pady = 7, font = ("Halvetica", test_size, "bold"),
        command = self.ClearDisplay)
        self.ClearButton.grid(row = 1, columnspan= 4, sticky = W)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid Syntax")
            self.task = ""
    
    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

calculator = Tk()

calculator.title("Calculator")

app = Application(calculator)
calculator.resizable(width = False,height = False)

calculator.mainloop()
