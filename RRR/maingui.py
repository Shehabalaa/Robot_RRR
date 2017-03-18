import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from inPut import *


def gui():
    window = Tk()
    window.configure(background='lightcyan')
    window.minsize(width=863, height=600)
    window.maxsize(width=863, height=600)
    inputgui(window)
    window.mainloop()

    exit()


