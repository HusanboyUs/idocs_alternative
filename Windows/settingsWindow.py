import customtkinter
from modal import Modal


class SettingsWindow(customtkinter.CTk):
    def __init__(self,username):
        super().__init__()
        self.modal = Modal()
        self.title('Settings Window')
        self.minsize(900,500)
        self.maxsize(900,500)

        self.modal =Modal()
        for i in self.modal.show_db():
            self.timer1 = customtkinter.CTkLabel(self,text=f'{i}',width=0,height=0,font=('Arial',10))
            self.timer1.pack(padx=0, pady=0)

        times = []
        for tim in self.modal.show_db():
            time = str(tim[1]).replace(':','.')
            times.append(time)
        

        self.timer1 = customtkinter.CTkLabel(self,text=times,width=0,height=0,font=('Arial',10))
        self.timer1.pack(padx=0, pady=0)

