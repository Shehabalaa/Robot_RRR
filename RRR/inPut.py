from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


from workspace import *

def inputgui(window):


    q1 = Label(window, text='Q1 ',bg='lightcyan')
    q1.grid(row=0,column=0)
    q2 = Label(window, text='Q2 ',bg='lightcyan')
    q2.grid(row=1,column=0)
    q3 = Label(window, text='Q3 ',bg='lightcyan')
    q3.grid(row=2,column=0)

    ll1 = Label(window, text='L1 ',bg='lightcyan')
    ll1.grid(row=3,column=0, sticky=W)
    ll2 = Label(window, text='L2 ',bg='lightcyan')
    ll2.grid(row=4,column=0, sticky=W)
    ll3 = Label(window, text='L3 ',bg='lightcyan')
    ll3.grid(row=5,column=0, sticky=W)

    q1_start_entry = Entry(window,bg='white')
    q1_end_entry = Entry(window,bg='white')
    q2_start_entry = Entry(window,bg='white')
    q2_end_entry = Entry(window,bg='white')
    q3_start_entry = Entry(window,bg='white')
    q3_end_entry = Entry(window,bg='white')
    l1_entry = Entry(window,bg='white')
    l2_entry = Entry(window,bg='white')
    l3_entry = Entry(window,bg='white')

    q1_start_entry.grid(row=0, column=1,columnspan=2,sticky=W)
    q1_start_entry.focus_set()
    q1_end_entry.grid(row=0, column=2,columnspan=2)
    q2_start_entry.grid(row=1, column=1,columnspan=2)
    q2_end_entry.grid(row=1, column=2,columnspan=2)
    q3_start_entry.grid(row=2, column=1,columnspan=2)
    q3_end_entry.grid(row=2, column=2,columnspan=2)

    l1_entry.grid(row=3,column=1,columnspan=2)
    l1_entry.focus_set()
    l2_entry.grid(row=4,column=1,columnspan=2)
    l2_entry.focus_set()
    l3_entry.grid(row=5,column=1,columnspan=2)
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
    C.get_tk_widget().grid(row=0, column=6, columnspan=10, rowspan=50)
    toolbarframe=Frame(window)
    toolbarframe.grid(row=51, column=7,columnspan=10,sticky=W)
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
    frame.grid(row=6, column=0,columnspan=3)
    button1 = Button(frame, text="DrawWorkSpace",fg="red",font=('Helvetica', 24),command= lambda: workspace(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry,v), height=4, width=15)
    button1.grid(row=6, column=0,columnspan=3)
    frame2 = Frame(window)
    frame2.grid(row=20, column=0,columnspan=3)
    button2 = Button(frame2, text="GetMaxLoad",fg="red",font=('Helvetica', 24),command= lambda: workspace(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry), height=1, width=10)
    button2.grid(row=20,column=0,columnspan=3)
    

def readinput(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry):
    global q1_st,q2_st,q3_st 
    global q1_end,q2_end,q3_end
    global l1,l2,l3
    global p1,p2,p3
    q1_st = float(q1_start_entry.get())
    q1_end = float(q1_end_entry.get())
    q2_st = float(q2_start_entry.get())
    q2_end = float(q2_end_entry.get())
    q3_st = float(q3_start_entry.get())
    q3_end = float(q3_end_entry.get())
    l1 = float(l1_entry.get())
    l2 = float(l2_entry.get())
    l3 = float(l3_entry.get())

##################
    while((q1_st>0 and q1_st>180) or (q1_end>0 and q1_end>180) ):
        q1_st-=180
        q1_end-=180
        
    while((q1_st<0 and q1_st<-180) or (q1_end<0 and q1_end<-180)):
        q1_st+=180
        q1_end+=180

###################
        
    while(q2_st>0 and q2_st>180 or q2_end>0 and q2_end>180):
        q2_st-=180
        q2_end-=180
        
    while(q2_st<0 and q2_st<-180 or q2_end<0 and q2_end<-180):
        q2_st+=180
        q2_end+=180


####################
        
    while(q3_st>0 and q3_st>180 or q3_end>0 and q3_end>180):
        q3_st-=180
        q3_end-=180
        
    while(q3_st<0 and q3_st<-180 or q3_end<0 and q3_end<-180 ):
        q3_st+=180
        q3_end+=180


####################

