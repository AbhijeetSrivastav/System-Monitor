"Main App Window"

import tkinter as tk



WIDTH_APP_SCREEN = 1020
HEIGHT_APP_SCREEN = 720

class App(tk.Tk):
    
    def __init__(self):
        super(App, self).__init__()

        self.title("System Monitor")

