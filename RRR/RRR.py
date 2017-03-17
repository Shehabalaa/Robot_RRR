import matplotlib.pyplot as plt
import math
from tkinter import *


def Rad(degree):
    return degree * (math.pi / 180)


def workspace():
    q1_st = 0.0
    q2_st = 0.0
    q3_st = 0.0
    q1_end = 0.0
    q2_end = 0.0
    q3_end = 0.0
    l1 = 0.0
    l2 = 8.0
    l3 = .0
    accuracy=0
    f = open("Data.txt", "r")

    l1 = f.readline()
    l1 = float(l1)
    l2 = f.readline()
    l2 = float(l2)
    l3 = f.readline()
    l3 = float(l3)
    q1_st = f.readline()
    q1_st = float(q1_st)
    q1_end = f.readline()
    q1_end = float(q1_end)
    q2_st = f.readline()
    q2_st = float(q2_st)
    q2_end = f.readline()
    q2_end = float(q2_end)
    q3_st = f.readline()
    q3_st = float(q3_st)
    q3_end = f.readline()
    q3_end = float(q3_end)
    accuracy= f.readline()
    accuracy = int(accuracy)

    range1=1
    range2=1
    range3=1
    if(accuracy==1):
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
    elif (accuracy==2):
        range1 = abs(q1_end - q1_st) / 90
        range2 = abs(q2_end - q2_st) / 90
        range3 = abs(q3_end - q3_st) / 90

    range1 = math.ceil(range1)
    range2 = math.ceil(range2)
    range3 = math.ceil(range3)
    x = []
    y = []

    if l1==0:
        q1_st=0;q1_end=1
    if l2==0:
        q2_st=0;q2_end=1
    if l3==0:
        q3_st=0;q3_end=1

    for i in range(int(q1_st), int(q1_end), range1):
        for j in range(int(q2_st), int(q2_end), range2):
            for k in range(int(q3_st), int(q3_end), range3):
                x.append(l1 * math.cos(Rad(i)) + l2 * math.cos(Rad(i + j)) + l3 * math.cos(Rad(i + j + k)))
                y.append(l1 * math.sin(Rad(i)) + l2 * math.sin(Rad(i + j)) + l3 * math.sin(Rad(i + j + k)))

    plt.plot([-1, 1], [0, 0], 'r', linewidth=2.0)
    plt.plot([0, 0], [-1, 1], 'r', linewidth=2.0)
    plt.grid(True, which='both')
    if (accuracy <= 2):
        plt.plot(x, y, "co")
    else:
        plt.plot(x, y, "c.")

    plt.show()


def gui():
    shehabgui = Tk()
    topframe = Frame(shehabgui)
    topframe.pack()
    bottomframe = Frame(shehabgui)
    bottomframe.pack(side=BOTTOM)

    button1 = Button(topframe, text="DrawWorkSpace", fg="red", command=workspace)
    button1.pack(side=LEFT)
    # button1.bind("<Button-1>", workspace)


    shehabgui.mainloop()
    exit()


gui()

'''
print("l1",l1)
print("l2",l2)
print("l3",l3)
print("q1_st",q1_st)
print("q2_st",q2_st)
print("q3_st",q3_st)
print("q1_end",q1_end)
print("q2_end",q2_end)
print("q3_end",q3_end)
'''
