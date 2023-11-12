import tkinter as Tk
from tkinter import messagebox
import customtkinter
from modal import Modal
from datetime import date
from settingsWindow import SettingsWindow



class TimerWindow(customtkinter.CTk):
    def __init__(self):
        self.modal =Modal()
        super().__init__()
        self.title('Timer Window')
        self.minsize(600,200)
        self.maxsize(600,200)

        customtkinter.set_default_color_theme('dark-blue')
        self.user = 'root'

        #timer label
        self.timer1 = customtkinter.CTkLabel(self,text='00:00:00',width=100,height=100,font=('Arial',50))
        self.timer1.pack(padx=0, pady=0)

        #start button
        self.start_button = customtkinter.CTkButton(self,text='Start',command=self.start_timer)
        self.start_button.pack()
        self.start_button.place(x=30, y=130)

        #pause timer
        self.pause_button = customtkinter.CTkButton(self,text='Save',command=self.save_time)
        self.pause_button.pack()
        self.pause_button.place(x=230, y=130)

        #save timer
        self.save_button = customtkinter.CTkButton(self,text='Settings',command=self.settings_window)
        self.save_button.pack()
        self.save_button.place(x=430,y=130)
        
        self.timer_is_running = False
        self.current_time = 0

    def start_timer(self):
        if not self.timer_is_running:
            self.timer_is_running = True
            self.start_button.configure(text="Pause")
            self.update_timer()
        else:
            self.timer_is_running = False
            self.start_button.configure(text="Resume")

    def update_timer(self):

        if self.timer_is_running:
            seconds = self.current_time % 60
            minutes = (self.current_time // 60) % 60
            hours = self.current_time // 3600
            self.timerformat = f'{hours:02}:{minutes:02}:{seconds:02}'
            self.timer1.configure(text=self.timerformat)
            self.current_time += 1


        self.after(1000, self.update_timer) 

    def save_time(self):
        self.modal.insert_time((self.user,self.timerformat,date.today(),))
        

    def settings_window(self):
        app = SettingsWindow(self.user)
        app.mainloop()



app = TimerWindow()
app.mainloop()




