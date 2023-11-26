import tkinter as tk
from tkinter import messagebox

class Error:

    @staticmethod
    def main(msg:str)->None:
        messagebox.showerror("Error",msg)
    
    

