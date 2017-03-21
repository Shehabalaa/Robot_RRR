from workspace import *

def inverse():

    l1=20
    l2=10
    l3 = 10
    q1_st = 0
    q1_end = math.pi
    q2_st=-math.pi
    q2_end=math.pi
    q3_st=-math.pi
    q3_end = math.pi
    a = 20
    b = 20

    theta = math.pi / 2


    '''
    calc
    '''

    a1 = a-(l3*math.cos(theta))
    b1 = b-(l3*math.sin(theta))
    r = math.sqrt((a1**2)+(b1**2))


    alpha1 = math.acos(((l1**2)+(r**2)-(l2**2))/(2*l1*r)) # alpha1 now radians
    ''' CHECK MATH DOMAIN RANGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE'''
    alpha2=-1*alpha1 #alpha2 now radians


    q11 = math.atan(abs(b1/a1))
    q12 = math.atan(abs(b1/a1))
    bast1=r*math.sin(alpha1)
    bast2=r*math.sin(alpha2)
    mkam1=(r*math.cos(alpha1))-l1
    mkam2=(r*math.cos(alpha2))-l1


    q21=math.atan(abs(bast1/mkam1))
    q22=math.atan(abs(bast2/mkam2))
    ''' CHECK DIVITION BY ZEROOOOOOOOOOOOOOOOOOOOOOOO'''



    if bast1>0 and mkam1<0:
        q21=math.pi-q21
    elif bast1<0 and mkam1<0:
        q21=math.pi+q21
    elif bast1<0 and mkam1 >0:
        q21=(2*math.pi)-q21

    if bast2>0 and mkam2<0:
        q22=math.pi-q22
    elif bast2<0 and mkam2<0:
        q22=math.pi+q22
    elif bast2<0 and mkam2 >0:
        q22=(2*math.pi)-q22






    if b1>0 and a1<0:
        q11 = math.pi - q11 - alpha1
        q12 = math.pi - q12 - alpha2
    elif b1<0 and a1 <0:
        q11 = math.pi + q11 - alpha1
        q12 = math.pi + q12 - alpha2
    elif b1<0 and a1 >0:
        q11 = 2*math.pi - q11  - alpha1
        q12 = 2*math.pi - q12  - alpha2
    else:
        q11 -= alpha1
        q12 -= alpha2





    q31= theta - q11 - q21
    q32= theta - q12 - q22

    '''
    points
    '''
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    plt.plot([-1, 1], [0, 0], 'r', linewidth=2.0)
    plt.plot([0, 0], [-1, 1], 'r', linewidth=2.0)
    plt.grid(True, which='both')


    while(q11>0 and q11> 2*math.pi ):
        q11-=2*math.pi
    while(q21>0 and q21> 2*math.pi):
        q21-=2*math.pi
    while(q31> 0 and q31> 2*math.pi):
        q31 -= 2*math.pi

    while(q12>0 and q12> 2*math.pi):
        q12-=2*math.pi
    while(q22>0 and q22> 2*math.pi):
        q22-=2*math.pi
    while(q32> 0 and q32> 2*math.pi):
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
        plt.plot(x1,y1,"b")

    if (q1_end >= q12 >= q1_st) and (q2_end>= q22>=q2_st)  and  (q3_end>=q32>=q3_st):
        x2.append(0)
        x2.append(l1*math.cos(q12))
        x2.append((l1*math.cos(q12))+(l2*math.cos(q12+q22)))
        x2.append((l1*math.cos(q12))+(l2*math.cos(q12+q22))+(l3*math.cos(q12+q22+q32)))
        y2.append(0)
        y2.append(l1*math.sin(q12))
        y2.append((l1*math.sin(q12))+(l2*math.sin(q12+q22)))
        y2.append((l1*math.sin(q12))+(l2*math.sin(q12+q22))+(l3*math.sin(q12+q22+q32)))
        plt.plot(x2,y2,"r")


    plt.show()


def gui():
    medogui = Tk()


    topframe = Frame(medogui)
    topframe.pack()
    bottomframe = Frame(medogui)
    bottomframe.pack(side=BOTTOM)

    button1 = Button(topframe, text="DrawWorkSpace", fg="red", command=inverse)
    button1.pack(side=LEFT)
    # button1.bind("<Button-1>", workspace)


    medogui.mainloop()
    exit()


gui()
