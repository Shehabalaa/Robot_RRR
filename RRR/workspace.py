
import matplotlib.pyplot as plt
import math
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg





def Rad(degree):
    return degree * (math.pi / 180)


def workspace(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry , v):
    q1_st = 0.0
    q2_st = 0.0
    q3_st = 0.0
    q1_end = 0.0
    q2_end = 0.0
    q3_end = 0.0
    l1 = 0.0
    l2 = 0.0
    l3 = 0.0
    accuracy=v.get()
    accuracy=int(accuracy)
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
    C.get_tk_widget().grid(row=0,column=7,columnspan=10,rowspan=200)
    toolbarframe=Frame(window)
    toolbarframe.grid(row=301, column=7,columnspan=10,sticky=W)

    toolbar = NavigationToolbar2TkAgg(C, toolbarframe)
    toolbar.update()

    C.show()
