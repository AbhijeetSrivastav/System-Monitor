"Utility methods"

import sys
from monitor.exception import MonitorException

def DPIAwareness(app):
    """
    Activates DPI awareness to increase the pixel density of UI to enhance graphics 
    -----------------------------------------------------
    input:
    - `app`: tkinter app
    ------------------------------------------------------
    return: None
    """
    try:
        import ctypes
        awareness = ctypes.c_int()
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception as e:
        raise MonitorException(e, sys)
    

def ImageConfigurator(path: str, dimension: tuple) -> object:
    """
    Resizes image and return image object 
    -----------------------------------------------------
    input:
    - `path`: image path
    - `dimension`: height x width `tuple`
    ------------------------------------------------------
    return: `image`
    """
    try:
        from PIL import ImageTk, Image

        image_path = Image.open(path)
        image_resized = image_path.resize(size=dimension)
        image = ImageTk.PhotoImage(image_resized)
        return image
    except Exception as e:
        raise MonitorException(e, sys)


def WinCenter(screen, screen_width: float, screen_height:float)->tuple:
    """
    Centers the tkinter window
    -----------------------------------------------------
    input:
    - `screen`: screen class
    - `screen_width`: width of the screen
    - `screen_height`: height of the screen
    ------------------------------------------------------
    return: `tuple`
    """

    try:
        import tkinter

        PIXEL_COUNT_WIDTH = screen.winfo_screenwidth()
        PIXEL_COUNT_HEIGHT = screen.winfo_screenheight()
        x_coordinate = (PIXEL_COUNT_WIDTH / 2) - (screen_width / 2)
        y_coordinate = (PIXEL_COUNT_HEIGHT / 2) - (screen_height / 2)
        return x_coordinate, y_coordinate
    except Exception as e:
        raise MonitorException(e, sys)