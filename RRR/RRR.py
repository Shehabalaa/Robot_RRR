import matplotlib.pyplot as plt
import math
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
def Rad(degree):
    return degree * (math.pi / 180)


def workspace(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry):
    q1_st = 0.0
    q2_st = 0.0
    q3_st = 0.0
    q1_end = 0.0
    q2_end = 0.0
    q3_end = 0.0
    l1 = 0.0
    l2 = 0.0
    l3 = 0.0
    accuracy = 0
    range1 = 1
    range2 = 1
    range3 = 1
    q1_st = q1_start_entry.get()
    q1_end = q1_end_entry.get()
    q2_st = q2_start_entry.get()
    q2_end = q2_end_entry.get()
    q3_st = q3_start_entry.get()
    q3_end = q3_end_entry.get()
    l1 = l1_entry.get()
    l2 = l2_entry.get()
    l3 = l3_entry.get()
    q1_st = float(q1_st)
    q2_st = float(q2_st)
    q3_st = float(q3_st)
    q1_end = float(q1_end)
    q2_end = float(q2_end)
    q3_end = float(q3_end)
    l1 =float(l1)
    l2 = float(l2)
    l3= float(l3)

    if (accuracy == 1):
        if abs(q1_end - q1_st) >= 180:
            range1 = abs(q1_end - q1_st) / 60
        elif abs(q1_end - q1_st) >= 90:
            range1 = abs(q1_end - q1_st) / 45
        elif abs(q1_end - q1_st) >= 30:
            range1 = abs(q1_end - q1_st) / 20
        else:
            range1 = 1

        if abs(q2_end - q2_st) >= 180:
            range2 = abs(q2_end - q2_st) / 60
        elif abs(q2_end - q2_st) >= 90:
            range2 = abs(q2_end - q2_st) / 45
        elif abs(q2_end - q2_st) >= 30:
            range2 = abs(q2_end - q2_st) / 20
        else:
            range2 = 1

        if abs(q3_end - q3_st) >= 180:
            range3 = abs(q3_end - q3_st) / 60
        elif abs(q3_end - q3_st) >= 90:
            range3 = abs(q3_end - q3_st) / 45
        elif abs(q3_end - q3_st) >= 30:
            range3 = abs(q3_end - q3_st) / 20
        else:
            range3 = 1
    elif (accuracy == 2):
        range1 = abs(q1_end - q1_st) / 90
        range2 = abs(q2_end - q2_st) / 90
        range3 = abs(q3_end - q3_st) / 90

    range1 = math.ceil(range1)
    range2 = math.ceil(range2)
    range3 = math.ceil(range3)
    x = []
    y = []


    if l1 == 0:
        q1_st = 0;
        q1_end = 1
    if l2 == 0:
        q2_st = 0;
        q2_end = 1
    if l3 == 0:
        q3_st = 0;
        q3_end = 1



    for i in range(int(q1_st), int(q1_end), range1):
        for j in range(int(q2_st), int(q2_end), range2):
            for k in range(int(q3_st), int(q3_end), range3):
                x.append(l1 * math.cos(Rad(i)) + l2 * math.cos(Rad(i + j)) + l3 * math.cos(Rad(i + j + k)))
                y.append(l1 * math.sin(Rad(i)) + l2 * math.sin(Rad(i + j)) + l3 * math.sin(Rad(i + j + k)))




    f = Figure(figsize=(5, 5), dpi=100,facecolor='lightblue')
    a = f.add_subplot(111)

    a.plot([-1, 1], [0, 0], 'r', linewidth=2.0)
    a.plot([0, 0], [-1, 1], 'r', linewidth=2.0)
    a.grid(True, which='both')
    if (accuracy <= 2):
        a.plot(x, y, "co")
    else:
        a.plot(x, y, "c.")

    C = FigureCanvasTkAgg(f, window)
    C.get_tk_widget().grid(row=0,column=7,columnspan=10,rowspan=300)
    toolbarframe=Frame(window)
    toolbarframe.grid(row=301, column=7,columnspan=10,sticky=W)

    toolbar = NavigationToolbar2TkAgg(C, toolbarframe)
    toolbar.update()

    C.show()




def gui():
    window = Tk()
    window.configure(background='lightcyan')
    window.minsize(width=800, height=700)
    window.maxsize(width=10000, height=1000)
    inputgui(window)
    window.mainloop()

    exit()



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



    #q1_start_entry.delete(0, END)
    #q1_start_entry.insert(10, 'Default')

    frame = Frame(window)
    frame.grid(row=6, column=0, columnspan=3, rowspan=1)
    button1 = Button(frame, text="DrawWorkSpace",fg="red",font=('Helvetica', 24),command= lambda: workspace(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry), height=4, width=15)
    button1.grid(row=6, column=0, columnspan=3, rowspan=1,sticky=W)

    f = Figure(figsize=(5, 5), dpi=100,facecolor='lightblue')
    a = f.add_subplot(111)
    a.plot([-1, 1], [0, 0], 'r', linewidth=2.0)
    a.plot([0, 0], [-1, 1], 'r', linewidth=2.0)
    a.grid(True, which='both')
    C = FigureCanvasTkAgg(f, window)
    C.get_tk_widget().grid(row=0, column=7, columnspan=10, rowspan=300)
    toolbarframe=Frame(window)
    toolbarframe.grid(row=301, column=7,columnspan=10,sticky=W)

    toolbar = NavigationToolbar2TkAgg(C, toolbarframe)
    toolbar.update()






gui()