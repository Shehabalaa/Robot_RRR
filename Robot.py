import matplotlib.pyplot as plt
import math
from tkinter import *


def Rad(degree):
    return degree * (math.pi / 180)


def workspace():
    q1_st = 0.0;
    q2_st = 0.0;
    q3_st = 0.0
    q1_end = 0.0;
    q2_end = 0.0;
    q3_end = 0.0
    l1 = 0.0;
    l2 = 8.0;
    l3 = .0

    f = open("Data.txt", "r")

    l1 = f.readline();
    l1 = float(l1)
    l2 = f.readline();
    l2 = float(l2)
    l3 = f.readline();
    l3 = float(l3)
    q1_st = f.readline();
    q1_st = float(q1_st)
    q1_end = f.readline();
    q1_end = float(q1_end)
    q2_st = f.readline();
    q2_st = float(q2_st)
    q2_end = f.readline();
    q2_end = float(q2_end)
    q3_st = f.readline();
    q3_st = float(q3_st)
    q3_end = f.readline();
    q3_end = float(q3_end)

    x = []
    y = []

    for i in range(int(q1_st), int(q1_end)):
        for j in range(int(q2_st), int(q2_end)):
            for k in range(int(q3_st), int(q3_end)):
                x.append(l1 * math.cos(Rad(i)) + l2 * math.cos(Rad(i + j)) + l3 * math.cos(Rad(i + j + k)))
                y.append(l1 * math.sin(Rad(i)) + l2 * math.sin(Rad(i + j)) + l3 * math.sin(Rad(i + j + k)))

    plt.plot([-1, 1], [0, 0], 'r', linewidth=2.0)
    plt.plot([0, 0], [-1, 1], 'r', linewidth=2.0)
    plt.plot(x, y, 'b.')

    plt.grid(True, which='both')
    plt.show()



def gui():
    shehabgui = Tk()
    topframe = Frame(shehabgui)
    topframe.pack()
    bottomframe = Frame(shehabgui)
    bottomframe.pack(side=BOTTOM)

    button1 = Button(topframe, text="DrawWorkSpace", fg="red", command=workspace)
    button1.pack(side=LEFT)
    #button1.bind("<Button-1>", workspace)


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
