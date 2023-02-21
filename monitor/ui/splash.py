"Splash Screen"

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
import time

from monitor import app
from monitor.utilities.utils import WinCenter
from monitor.utilities.utils import ImageConfigurator


class SplashScreen(tk.Tk):
    """
    Splash Screen Component
    -----------------------------------------------------
    input:
    - `tk.TK`: Tkinter class
    ------------------------------------------------------
    return: None
    """
    
    def __init__(self):
        super(SplashScreen, self).__init__()


        "STYLING"
        self.FONT_WEIGHT = "bold"
        self.FONT_STYLE = "Calibri (Body)"
        self.FONT_SIZE = 18
        self.PRIMARY_COLOUR = "White"
        self.SECONDARY_COLOUR = "#249794"

        s = ttk.Style()
        s.theme_use("clam")
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')


        "SCREEN PROPERTIES"
        self.WIDTH_SPLASH_SCREEN = app.WIDTH_APP_SCREEN
        self.HEIGHT_SPLASH_SCREEN = app.HEIGHT_APP_SCREEN - 100

        centrizer = WinCenter(self, self.WIDTH_SPLASH_SCREEN, self.HEIGHT_SPLASH_SCREEN)
        
        self.geometry("%dx%d+%d+%d" % (self.WIDTH_SPLASH_SCREEN, self.HEIGHT_SPLASH_SCREEN, centrizer[0], centrizer[1]))

        self.overrideredirect(True) # removes window options


        "WIDGETS"
        tk.Frame(self, width=self.WIDTH_SPLASH_SCREEN, height=self.HEIGHT_SPLASH_SCREEN,
                 background=self.SECONDARY_COLOUR).place(x=0, y=0)
        
        title_label = ttk.Label(self, text='System Monitor', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
                                font=(self.FONT_STYLE, self.FONT_SIZE + 40, self.FONT_WEIGHT))
        title_label.place(x=50, y=200)

        sub_title_label = ttk.Label(self, text='Keep an eye on your stats!', foreground=self.PRIMARY_COLOUR,
                                    background=self.SECONDARY_COLOUR,
                                    font=(self.FONT_STYLE, self.FONT_SIZE - 5, self.FONT_WEIGHT))
        sub_title_label.place(x=60, y=290)


        logo = ImageConfigurator(path="assets/t.jpg", dimension=(340, 300))
        logo_label = tk.Label(self, image=logo, background=self.SECONDARY_COLOUR)
        logo_label.logo = logo
        logo_label.place(x=650, y=150)



        activate_button = tk.Button(self, width=10, height=1, borderwidth=5, justify="center", overrelief="raised",
                                    text='Get Started', command=self.bar, border=1,
                                    foreground=self.SECONDARY_COLOUR,
                                    background=self.PRIMARY_COLOUR)
        activate_button.place(x=450, y=520)


    def bar(self):
        """
        Progress Bar 
        -----------------------------------------------------
        input:
        - `self`: Tkinter class
        ------------------------------------------------------
        return: None
        """

        loading_label = ttk.Label(self, text="Loading...", foreground=self.SECONDARY_COLOUR, background=self.PRIMARY_COLOUR, font=(self.FONT_STYLE, 11, self.FONT_WEIGHT))
        loading_label.place(x=0, y=self.HEIGHT_SPLASH_SCREEN - 42)

        progress = Progressbar(self, style="red.Horizontal.TProgressbar", orient="horizontal", length=self.WIDTH_SPLASH_SCREEN, mode="determinate")
        progress.place(x=0, y=self.HEIGHT_SPLASH_SCREEN - 18)

        r = 0
        for i in range(100):
            progress['value'] = r
            self.update_idletasks()
            time.sleep(0.03)
            r = r + 1


        # Destroying the splash window and opening app
        self.destroy()
        app.App()