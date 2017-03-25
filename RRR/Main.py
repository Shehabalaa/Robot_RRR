from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

q1_st = 0.0
q2_st = 0.0
q3_st = 0.0
q1_end = 0.0
q2_end = 0.0
q3_end = 0.0
l1 = 0.0
l2 = 0.0
l3 = 0.0
x = []
y = []
window = Tk()
window.configure(background='lightcyan')
window.minsize(width=820, height=550)
window.maxsize(width=820, height=550)
f = Figure(figsize=(5, 5), dpi=100,facecolor='lightblue')
figure = f.add_subplot(111)
figure.plot([-1, 1], [0, 0], 'r', linewidth=2.0)
figure.plot([0, 0], [-1, 1], 'r', linewidth=2.0)
figure.grid(True, which='both')
C = FigureCanvasTkAgg(f, window)
C.get_tk_widget().grid(row=0,column=43,rowspan=125)
toolbarframe=Frame(window)
toolbarframe.grid(row=126, column=43,sticky=W)
toolbar = NavigationToolbar2TkAgg(C, toolbarframe)
toolbar.update()




def readinput(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry):
    global q1_st
    global q2_st
    global q3_st
    global q1_end
    global q2_end
    global q3_end
    global l1
    global l2
    global l3
    q1_st = float(q1_start_entry.get())
    q1_end = float(q1_end_entry.get())
    q2_st=float(q2_start_entry.get())
    q2_end=float(q2_end_entry.get())
    q3_st=float(q3_start_entry.get())
    q3_end=float(q3_end_entry.get())
    l1=float(l1_entry.get())
    l2=float(l2_entry.get())
    l3=float(l3_entry.get())

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




def Jac(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry,load1_entry,load2_entry,load3_entry):
    global q1_st
    global q2_st
    global q3_st
    global q1_end
    global q2_end
    global q3_end
    global l1
    global l2
    global l3
    readinput(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry)
    load1=float(load1_entry.get())
    load2=float(load2_entry.get())
    load3=float(load3_entry.get())
    xx = 0.0
    yy = 0.0
    zz = 0.0

    p=np.array( [[load1],[load2],[load3]], dtype=float )
    J=np.zeros((3,3), dtype=float)
    temp = np.zeros((3,1), dtype=float)

    for i in range (int(q1_st),int(q1_end+1),1):
        for j in range (int (q2_st),int(q2_end+1),1):
            for k in range (int(q3_st),int(q3_end+1),1):
            
                J[0,0]=float("{0:.3f}".format(-(l1*math.sin(i*math.pi/180))-(l2*math.sin(((i+j)*math.pi/180)))-(l3*math.sin((i+j+k)*math.pi/180))))
                J[0,1]=float("{0:.3f}".format(-(l2*math.sin((i+j)*math.pi/180)) -(l3*math.sin((i+j+k)*math.pi/180))))
                J[0,2]=float("{0:.3f}".format(-(l3*math.sin((i+j+k)*math.pi/180))))
                J[1,0]=float("{0:.3f}".format((l1*math.cos(i*math.pi / 180)) + (l2*math.cos((i+j)*math.pi/180)) + (l3*math.cos((i+j+k)*math.pi/180))))
                J[1,1]=float("{0:.3f}".format((l2*math.cos((i+j)*math.pi/180)) + (l3*math.cos((i+j+k)*math.pi/180))))
                J[1,2]=float("{0:.3f}".format(l3*math.cos((i+j+k)*math.pi/180)))
                J[2,0]=1.0
                J[2,1]=1.0
                J[2,2]=1.0
            
         
                temp=np.dot(-J.T,p)
            
                if abs(float(temp[0,0])) > abs(xx): 
                    xx = float(temp[0,0])
           
            
                if abs(float(temp[1,0])) > abs(yy): 
                    yy = float(temp[1,0])
            
            
                if abs(float(temp[2,0])) > abs(zz) : 
                    zz = float(temp[2,0])
              
      
    QQ=np.array(([[xx],[yy],[zz]]), dtype=float)

    m = Tk()
    m.minsize(width=2, height=80)
    m.maxsize(width=2, height=80)
    w = Message(m, text="Maxloads\n"+str(xx)+'\n'+str(yy)+'\n'+str(zz)+'\n')
    w.grid()
    




def inverse(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry,x_entry,y_entry,theta_entry):
    global q1_st
    global q2_st
    global q3_st
    global q1_end
    global q2_end
    global q3_end
    global l1
    global l2
    global l3
    global figure
    global C
    m = Tk()
    m.minsize(width=100, height=100)
    m.maxsize(width=100, height=100)
    w = Message(m, text="Robot can't reach that point \n with given input!!!")

    
    fraction=float()
    readinput(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry)
    a=float(x_entry.get())
    b=float(y_entry.get())
    theta = float(theta_entry.get())
    q1_st=math.radians(q1_st)
    q1_end=math.radians(q1_end)
    q2_st=math.radians(q2_st)
    q2_end=math.radians(q2_end)
    q3_st=math.radians(q3_st)
    q3_end=math.radians(q3_end)
    while(theta>0 and theta > 180 ):
        theta-=180
    while(theta<0 and theta < 180):
        theta+=180

    theta=math.radians(theta)
   

    '''
    calc
    '''


    a1 = a-(l3*math.cos(theta))
    b1 = b-(l3*math.sin(theta))
    r = math.sqrt((a1**2.0)+(b1**2.0))
    fraction = ((l1**2.0)+(r**2.0)-(l2**2.0))/(2.0*l1*r)

    
    if(not(-1 <= fraction <=1) or l1 ==0 or r == 0):
        w.grid()
        return

    
    alpha1 = math.acos(fraction) # alpha1 now radians
    ''' CHECK MATH DOMAIN RANGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'''
    alpha2=-1*alpha1 #alpha2 now radians




    ''' al function tl3t mwgoda :D'''
    q11 = np.arctan2(b1, a1) - alpha1
    q12 = np.arctan2(b1, a1) - alpha2
    bast1=r*math.sin(alpha1)
    bast2=r*math.sin(alpha2)
    mkam1=(r*math.cos(alpha1))-l1
    mkam2=(r*math.cos(alpha2))-l1

    q21=np.arctan2(bast1, mkam1)
    q22=np.arctan2(bast2, mkam2)




    q31= theta - q11 - q21
    q32= theta - q12 - q22

    '''
    points
    '''
    x1=[]
    y1=[]
    x2=[]
    y2=[]


    while(q11>0 and q11> math.pi ):
        q11-=2*math.pi
    while(q21>0 and q21> math.pi):
        q21-=2*math.pi
    while(q31> 0 and q31> math.pi):
        q31 -= 2*math.pi

    while(q12>0 and q12> math.pi):
        q12-=2*math.pi
    while(q22>0 and q22> math.pi):
        q22-=2*math.pi
    while(q32> 0 and q32> math.pi):
        q32 -= 2*math.pi

    while(q11<0 and q11< -math.pi) :
        q11+=2*math.pi
    while(q21<0 and q21< -math.pi):
        q21+=2*math.pi
    while(q31< 0 and q31< -math.pi):
        q31 += 2*math.pi

    while(q12<0 and q12< -math.pi):
            q12+=2*math.pi
    while(q22<0 and q22< -math.pi):
            q22+=2*math.pi
    while(q32< 0 and q32< -math.pi):
            q32 += 2*math.pi


    if (q1_end>=q11 >= q1_st) and (q2_end>= q21 >= q2_st)  and (q3_end>=q31 >=q3_st):
        x1.append(0)
        x1.append(l1*math.cos(q11))
        x1.append((l1*math.cos(q11))+(l2*math.cos(q11+q21)))
        x1.append((l1*math.cos(q11))+(l2*math.cos(q11+q21))+(l3*math.cos(q11+q21+q31)))
        y1.append(0)
        y1.append(l1*math.sin(q11))
        y1.append((l1*math.sin(q11))+(l2*math.sin(q11+q21)))
        y1.append((l1*math.sin(q11))+(l2*math.sin(q11+q21))+(l3*math.sin(q11+q21+q31)))
        figure.plot(x1,y1,"b")

    if (q1_end >= q12 >= q1_st) and (q2_end>= q22>=q2_st)  and  (q3_end>=q32>=q3_st):
        x2.append(0)
        x2.append(l1*math.cos(q12))
        x2.append((l1*math.cos(q12))+(l2*math.cos(q12+q22)))
        x2.append((l1*math.cos(q12))+(l2*math.cos(q12+q22))+(l3*math.cos(q12+q22+q32)))
        y2.append(0)
        y2.append(l1*math.sin(q12))
        y2.append((l1*math.sin(q12))+(l2*math.sin(q12+q22)))
        y2.append((l1*math.sin(q12))+(l2*math.sin(q12+q22))+(l3*math.sin(q12+q22+q32)))
        figure.plot(x2,y2,"r")

    C.show()










def workspace(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry , v):
    global q1_st
    global q2_st
    global q3_st
    global q1_end
    global q2_end
    global q3_end
    global l1
    global l2
    global l3
    accuracy=v.get()
    accuracy=int(accuracy)
    range1 = 1
    range2 = 1
    range3 = 1
    readinput(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry)
    
    if (accuracy == 1):
        if abs(q1_end - q1_st) >= 180:
            range1 = abs(q1_end - q1_st) / 60 +1
        elif abs(q1_end - q1_st) >= 90:
            range1 = abs(q1_end - q1_st) / 45 +1
        elif abs(q1_end - q1_st) >= 30:
            range1 = abs(q1_end - q1_st) / 20 +1
        else:
            range1 = 1

        if abs(q2_end - q2_st) >= 180:
            range2 = abs(q2_end - q2_st) / 60 +1
        elif abs(q2_end - q2_st) >= 90:
            range2 = abs(q2_end - q2_st) / 45 +1
        elif abs(q2_end - q2_st) >= 30:
            range2 = abs(q2_end - q2_st) / 20 +1
        else:
            range2 = 1

        if abs(q3_end - q3_st) >= 180:
            range3 = abs(q3_end - q3_st) / 60 +1
        elif abs(q3_end - q3_st) >= 90:
            range3 = abs(q3_end - q3_st) / 45 +1
        elif abs(q3_end - q3_st) >= 30:
            range3 = abs(q3_end - q3_st) / 20 +1
        else:
            range3 = 1
    elif (accuracy == 2):
        range1 = abs(q1_end - q1_st) / 90 +1
        range2 = abs(q2_end - q2_st) / 90 +1
        range3 = abs(q3_end - q3_st) / 90 +1
    else:
        if abs(q1_end - q1_st) >= 180:
            range1 = abs(q1_end - q1_st) / 200 +1
        else:
            range1 = abs(q1_end - q1_st) / 100 +1

        if abs(q2_end - q2_st) >= 180:
            range2 = abs(q2_end - q2_st) / 200 +1
        else:
            range2 = abs(q2_end - q2_st) / 100 +1

        if abs(q3_end - q3_st) >= 180:
            range3 = abs(q3_end - q3_st) / 200 +1
        else:
            range3 = range3 = abs(q3_end - q3_st) / 100 +1

    range1 = math.ceil(range1)
    range2 = math.ceil(range2)
    range3 = math.ceil(range3)
    
    global x
    global y


    if l1 == 0 or q1_end-q1_st == 0:
        q1_st = 0;
        q1_end = 1
        range1=1
    if l2 == 0  or q2_end-q2_st == 0 :
        q2_st = 0;
        q2_end = 1
        range2=1
    if l3 == 0  or q3_end-q3_st == 0 :
        q3_st = 0;
        q3_end = 1
        range3 = 1


    if(q1_end<0):
        q1_end+=360
    if (q2_end < 0):
        q2_end += 360
    if (q3_end < 0):
        q3_end += 360

    for i in range(int(q1_st), int(q1_end), range1):
        for j in range(int(q2_st), int(q2_end), range2):
            for k in range(int(q3_st),int(q3_end), range3):
                x.append(float("{0:.2f}".format(l1 * math.cos(math.radians(i)) + l2 * math.cos(math.radians(i + j)) + l3 * math.cos(math.radians(i + j + k)))))
                y.append(float("{0:.2f}".format(l1 * math.sin(math.radians(i)) + l2 * math.sin(math.radians(i + j)) + l3 * math.sin(math.radians(i + j + k)))))
    
    global figure
    global C
    figure.plot(x, y, "c.")
    C.draw()
    
   







def inputgui(window):

    q1 = Label(window, text='Q1 ',bg='lightcyan')
    q1.grid(row=0,column=0)
    q2 = Label(window, text='Q2 ',bg='lightcyan')
    q2.grid(row=1,column=0)
    q3 = Label(window, text='Q3 ',bg='lightcyan')
    q3.grid(row=2,column=0)
    x = Label(window, text='X',bg='lightcyan')
    x.grid(row=31,column=0)
    y = Label(window, text='Y',bg='lightcyan')
    y.grid(row=32,column=0)
    theta = Label(window, text='theta',bg='lightcyan')
    theta.grid(row=33,column=0)
    Q = Label(window, text='Q',bg='lightcyan')
    Q.grid(row=60,column=0)
    load = Label(window, text='(load)',bg='lightcyan')
    load.grid(row=61,column=0)
    
    
    ll1 = Label(window, text='  L1 ',bg='lightcyan')
    ll1.grid(row=3,column=0, sticky=W)
    ll2 = Label(window, text='  L2 ',bg='lightcyan')
    ll2.grid(row=4,column=0, sticky=W)
    ll3 = Label(window, text='  L3 ',bg='lightcyan')
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
    x_entry = Entry(window,bg='white')
    y_entry = Entry(window,bg='white')
    theta_entry = Entry(window,bg='white')
    load1_entry = Entry(window,bg='white')
    load2_entry = Entry(window,bg='white')
    load3_entry = Entry(window,bg='white')

    q1_start_entry.grid(row=0, column=1,columnspan=20,sticky=W)
    q1_start_entry.focus_set()
    q1_end_entry.grid(row=0, column=21,columnspan=20,sticky=W)
    q2_start_entry.grid(row=1, column=1,columnspan=20,sticky=W)
    q2_end_entry.grid(row=1, column=21,columnspan=20,sticky=W)
    q3_start_entry.grid(row=2, column=1,columnspan=20,sticky=W)
    q3_end_entry.grid(row=2, column=21,columnspan=20,sticky=W)
    l1_entry.grid(row=3,column=1,columnspan=20,sticky=W)
    l2_entry.grid(row=4,column=1,columnspan=20,sticky=W)
    l3_entry.grid(row=5,column=1,columnspan=20,sticky=W)
    x_entry.grid(row=31,column=1,columnspan=20,sticky=W)
    y_entry.grid(row=32,column=1,columnspan=20,sticky=W)
    theta_entry.grid(row=33, column=1,columnspan=20,sticky=W)
    load1_entry.grid(row=60,column=1,columnspan=20,sticky=W)
    load2_entry.grid(row=61,column=1,columnspan=20,sticky=W)
    load3_entry.grid(row=62,column=1,columnspan=20,sticky=W)
     
    q1_start_entry.insert(0,'0')
    q2_start_entry.insert(0,'0')
    q3_start_entry.insert(0,'0')
    q1_end_entry.insert(0,'0')
    q2_end_entry.insert(0,'0')
    q3_end_entry.insert(0,'0')
    l1_entry.insert(0,'0')
    l2_entry.insert(0, '0')
    l3_entry.insert(0, '0')
    x_entry.insert(0,'0')
    y_entry.insert(0,'0')
    theta_entry.insert(0,'0')
    load1_entry.insert(0,'0')
    load2_entry.insert(0,'0')
    load3_entry.insert(0,'0')

    v = StringVar()
    low = Radiobutton(window, text='Low',variable = v ,value=1, bg='lightcyan')
    meduim = Radiobutton(window, text='meduim',variable = v,  value=2, bg='lightcyan')
    high = Radiobutton(window, text='high',variable = v,  value=3, bg='lightcyan')
    low.grid(row=3, column=22,sticky=W)
    meduim.grid(row=4, column=22, sticky=W)
    high.grid(row=5, column=22, sticky=W)
    low.select()
    frame = Frame(window)
    frame.grid(row=7, column=0,columnspan=41)
    button1 = Button(frame, text="DrawWorkSpace",fg="red",font=('Helvetica', 24),command= lambda: workspace(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry,v), height=2, width=14)
    button1.grid(row=7, column=0,columnspan=41)
    frame2 = Frame(window)
    frame2.grid(row=50,column=0,columnspan=41,sticky=W)
    button2 = Button(frame2, text="DrawRobot",fg="red",font=('Helvetica', 24),command= lambda: inverse(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry,x_entry,y_entry,theta_entry), height=1, width=14)
    button2.grid(row=50,column=0,columnspan=41,sticky=W)
    frame3 = Frame(window)
    frame3.grid(row=90,column=0,columnspan=41,sticky=W+S)
    button3 = Button(frame3, text="MaxLoad",fg="red",font=('Helvetica', 24),command= lambda: Jac(window,q1_start_entry,q1_end_entry,q2_start_entry,q2_end_entry,q3_start_entry,q3_end_entry,l1_entry,l2_entry,l3_entry,load1_entry,load2_entry,load3_entry), height=1, width=14)
    button3.grid(row=90,column=0,columnspan=41,sticky=W+S)
    






inputgui(window)


window.mainloop()
