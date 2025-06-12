''' 
An app that converts temperature from F to C 
V1: basic functions that convert temperatures; no validation
'''

from tkinter import *

class Converter:
    '''setting up the GUI'''
    def __init__ (self):
        
        # main window
        self.root = Tk()
        self.root.title("Temperature Converter")
        
        # container for frames 
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # dictionary to hold frames
        self.frames = {}
        
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()
        
        # show the intial frame 
        self.show_frame("MainFrame")
        
    def show_frame(self, name):
        '''display the required name from the dictionary'''
        frame = self.frames[name]
        frame.tkraise() # move frame to the top
        
    def run(self):
        self.root.mainloop()
    
    def calc_c (self, num, converted):
        if num != "":
            num = int(num)
            f = (num - 32) * (5/9)
            converted.config(text = f)        
    
    def calc_f (self, num, converted):
        if num != "":
            num = int(num)
            c = (num*(9/5)) + 32
            converted.config(text = c)
            
    def reset (self, name, converted):
        name.delete(0, END)    
        converted.config(text="Converted temperature goes here")
    
        
    def create_main_frame(self):
        '''create home screen of app'''
        frame = Frame(self.container)
        
        # main heading 
        self.label_title = Label(frame, text = "Temperature Converter", 
                            font="Verdana 16 bold")
        self.label_title.grid(row=0, columnspan=2, padx=10, pady=10)
        
        # buttons: to Centrigradde and to Fahrenhiet
        self.to_c_button = Button(frame, text="to Centrigrade", bg = "yellow",
                                  font="Verdana 12 bold",
                                  command=lambda: self.show_frame("to_cFrame"))
        self.to_c_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.to_f_button = Button(frame, text="to Fahrenheit", bg = "pink",
                                  font="Verdana 12 bold",
                                  command=lambda: self.show_frame("to_fFrame"))
        self.to_f_button.grid(row=1, column=1, padx=10, pady=10)
        
        frame.grid(row=0, column=0, sticky="nsew")
        
        return frame 
    
    def create_to_f_frame(self):
        '''create to fahrenheit screen of app'''
        frame = Frame(self.container)
        
        # main heading 
        self.label_title = Label(frame, text = "Enter the temperature in Centigrade", 
                            font="Verdana 12 bold")
        self.label_title.grid(row=0, columnspan=3, padx=10, pady=10) 
        
        # entry box
        self.box = Entry(frame, justify = CENTER)
        self.box.grid(row=1, columnspan=3, sticky = "ew")
        
        # buttons
        self.calc_f_button = Button(frame, text = "Calculate", 
                                    command=lambda: self.calc_f(self.box.get(), self.converted_label))
        self.calc_f_button.grid(row=2, column=0, ipady=10, ipadx=10,  sticky = "ew")
        
        self.home_button = Button(frame, text = "Back", 
                                  command=lambda: self.show_frame("MainFrame"))
        self.home_button.grid(row=2, column=1,ipady=10, ipadx=10,  sticky = "ew")
        
        self.reset_button = Button(frame, text = "Reset", command=lambda: self.reset(self.box, self.converted_label))
        self.reset_button.grid(row=2, column=2,ipady=10, ipadx=10, sticky = "ew")
        
        # label box at end :)
        self.converted_label = Label(frame, text = "Converted temperature goes here")
        self.converted_label.grid(row=3, columnspan=3, padx=10, pady=10) 
        
        frame.grid(row=0, column=0, sticky="nsew")
        
        return frame
    
    def create_to_c_frame(self):
        '''create to centrigrade screen of app'''
        frame = Frame(self.container)
        
        # main heading 
        self.label_title = Label(frame, text = "Enter the temperature in Fahrenheit", 
                            font="Verdana 12 bold")
        self.label_title.grid(row=0, columnspan=3, padx=10, pady=10) 
        
        # entry box
        self.box1 = Entry(frame, justify = CENTER)
        self.box1.grid(row=1, columnspan=3, sticky = "ew")
        
        # buttons
        self.calc_c_button = Button(frame, text = "Calculate", 
                                    command=lambda: self.calc_c(self.box1.get(),self.converted_label1))
        self.calc_c_button.grid(row=2, column=0, ipady=10, ipadx=10,  sticky = "ew")
        
        self.home_button = Button(frame, text = "Back", 
                                  command=lambda: self.show_frame("MainFrame"))
        self.home_button.grid(row=2, column=1,ipady=10, ipadx=10,  sticky = "ew")
        
        self.reset_button = Button(frame, text = "Reset", command=lambda: self.reset(self.box1, self.converted_label1))
        self.reset_button.grid(row=2, column=2,ipady=10, ipadx=10, sticky = "ew")
        
        # label box at end :)
        self.converted_label1 = Label(frame, text="Converted temperature goes here")
        self.converted_label1.grid(row=3, columnspan=3, padx=10, pady=10) 
        
        frame.grid(row=0, column=0, sticky="nsew")
        
        return frame
    
    

### Main Program ###
if __name__ == "__main__":
    app = Converter()
    app.run()