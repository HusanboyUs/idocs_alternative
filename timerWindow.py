from datetime import date
from customtkinter import CTk, CTkButton, CTkLabel, set_default_color_theme
from modal import Modal
import webbrowser
from datetime import date
import os
from timeGenerator import TimeGenerate
from alerts import Error


class TimerApp(CTk):
    def __init__(self):
        super().__init__()
        self.title('Timer Window')
        self.minsize(600, 200)
        self.maxsize(600, 200)

        set_default_color_theme('dark-blue')
        self.user = 'root'

        self.timer_label = CTkLabel(self, text='00:00:00', width=100, height=100, font=('Arial', 50))
        self.timer_label.pack(padx=0, pady=0)

        self.start_pause_button = CTkButton(self, text='Start', command=self.start_pause_timer_handler)
        self.start_pause_button.pack()
        self.start_pause_button.place(x=30, y=130)

        self.save_button = CTkButton(self, text='Save', command=self.save_time_handler)
        self.save_button.pack()
        self.save_button.place(x=230, y=130)

        self.settings_button = CTkButton(self, text='Settings', command=self.open_settings_window)
        self.settings_button.pack()
        self.settings_button.place(x=430, y=130)

        self.is_running = False
        self.seconds = 0
        self.timer_id = None

    def start_pause_timer_handler(self):
        if self.is_running:
            self.is_running = False
            if self.timer_id:
                self.after_cancel(self.timer_id)
            self.start_pause_button.configure(text='Start')
        else:
            self.is_running = True
            self.update_timer()
            self.start_pause_button.configure(text='Pause')

    def update_timer(self):
        if self.is_running:
            self.seconds += 1
            self.update_time_display()
            self.timer_id = self.after(1000, self.update_timer)

    def update_time_display(self):
        minutes, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        self.time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        self.timer_label.configure(text=self.time_string)

    def save_time_handler(self):
        try:
            modal = Modal()
            modal.insert_time((self.user, self.time_string, date.today()))
            print(modal._logs)
        except AttributeError:
            Error.main('Database not found or error while operation!')

    def open_settings_window(self):
        TimeGenerate.main()
        current_directory = os.getcwd()
        main_directory = os.path.join(current_directory, '.')
        os.chdir(main_directory)
        html_file_path = 'output.html'
        webbrowser.open('file://' + os.path.abspath(html_file_path), new=2)

    def timer_format(self):
        minutes, seconds = divmod(self.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()

