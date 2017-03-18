import matplotlib.pyplot as plt
import math
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from workspace import *

def inputgui(window):
    global q1_st
    global q1_end
    global q2_st
    global q2_end
    global q3_st
    global q3_end
    global l1
    global l2
    global l3
    global accuracy

    q1 = Label(window, text='Q1 ',bg='lightcyan')
    q1.grid(row=0,sticky=W)
    q2 = Label(window, text='Q2 ',bg='lightcyan')
    q2.grid(row=1,sticky=W)
    q3 = Label(window, text='Q3 ',bg='lightcyan')
    q3.grid(row=2,sticky=W)

    ll1 = Label(window, text='L1 ',bg='lightcyan')
    ll1.grid(row=3, sticky=W)
    ll2 = Label(window, text='L2 ',bg='lightcyan')
    ll2.grid(row=4, sticky=W)
    ll3 = Label(window, text='L3 ',bg='lightcyan')
    ll3.grid(row=5, sticky=W)

    q1_start_entry = Entry(window,bg='white')
    q1_end_entry = Entry(window,bg='white')
    q2_start_entry = Entry(window,bg='white')
    q2_end_entry = Entry(window,bg='white')
    q3_start_entry = Entry(window,bg='white')
    q3_end_entry = Entry(window,bg='white')
    l1_entry = Entry(window,bg='white')
    l2_entry = Entry(window,bg='white')
    l3_entry = Entry(window,bg='white')

    q1_start_entry.grid(row=0, column=1)
    q1_start_entry.focus_set()
    q1_end_entry.grid(row=0, column=2)
    q2_start_entry.grid(row=1, column=1)
    q2_end_entry.grid(row=1, column=2)
    q3_start_entry.grid(row=2, column=1)
    q3_end_entry.grid(row=2, column=2)

    l1_entry.grid(row=3,column=1)
    l1_entry.focus_set()
    l2_entry.grid(row=4,column=1)
    l2_entry.focus_set()
    l3_entry.grid(row=5,column=1)
    l3_entry.focus_set()


    q1_start_entry.insert(0,'0')
    q2_start_entry.insert(0,'0')
    q3_start_entry.insert(0,'0')

    q1_end_entry.insert(0,'0')
    q2_end_entry.insert(0,'0')
    q3_end_entry.insert(0,'0')
    l1_entry.insert(0,'0')
    l2_entry.insert(0, '0')
    l3_entry.insert(0, '0')

    f = Figure(figsize=(5, 5), dpi=100,facecolor='lightblue')
    a = f.add_subplot(111)
    a.plot([-1, 1], [0, 0], 'r', linewidth=2.0)
    a.plot([0, 0], [-1, 1], 'r', linewidth=2.0)
    a.grid(True, which='both')
    C = FigureCanvasTkAgg(f, window)
    C.get_tk_widget().grid(row=0, column=7, columnspan=10, rowspan=200)
    toolbarframe=Frame(window)
    toolbarframe.grid(row=301, column=7,columnspan=10,sticky=W)
    toolbar = NavigationToolbar2TkAgg(C, toolbarframe)
    toolbar.update()
    v = StringVar()
    low = Radiobutton(window, text='Low',variable = v ,value=1, bg='lightcyan')
    meduim = Radiobutton(window, text='meduim',variable = v,  value=2, bg='lightcyan')
    high = Radiobutton(window, text='high',variable = v,  value=3, bg='lightcyan')
    low.grid(row=3, column=2, sticky=W)
    meduim.grid(row=4, column=2, sticky=W)
    high.grid(row=5, column=2, sticky=W)
    low.select()
    meduim.deselect()
    high.deselect()
    frame = Frame(window)
    frame.grid(row=6, column=0, columnspan=3, rowspan=1)
    button1 = Button(frame, text="DrawWorkSpace",fg="red",font=('Helvetica', 24),command= lambda: workspace(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry,v), height=4, width=15)
    button1.grid(row=6, column=0, columnspan=3, rowspan=1,sticky=W)
