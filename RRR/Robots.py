import math
import numpy as np
def Jac():
    L1 = 20.0
    L2 = 20.0
    L3 = 20.0

    q1_st = 0.0

    q1_end = 200.0

    q2_st = 0.0

    q2_end = 200.0

    q3_st = 0.0

    q3_end = 200.0

    x = 0.0
    y = 0.0
    z = 0.0

    p=np.array( [[20.0],[30.0],[40.0]], dtype=float )
    J=np.zeros((3,3), dtype=float)
    temp = np.zeros((3,1), dtype=float)

    for i in range (int(q1_st),int(q1_end+1),1):
        for j in range (int (q2_st),int(q2_end+1),1):
            for k in range (int(q3_st),int(q3_end+1),1):
            
                J[0,0]=float("{0:.3f}".format(-(L1*math.sin(i*math.pi/180))-(L2*math.sin(((i+j)*math.pi/180)))-(L3*math.sin((i+j+k)*math.pi/180))))
                J[0,1]=float("{0:.3f}".format(-(L2*math.sin((i+j)*math.pi/180)) -(L3*math.sin((i+j+k)*math.pi/180))))
                J[0,2]=float("{0:.3f}".format(-(L3*math.sin((i+j+k)*math.pi/180))))
                J[1,0]=float("{0:.3f}".format((L1*math.cos(i*math.pi / 180)) + (L2*math.cos((i+j)*math.pi/180)) + (L3*math.cos((i+j+k)*math.pi/180))))
                J[1,1]=float("{0:.3f}".format((L2*math.cos((i+j)*math.pi/180)) + (L3*math.cos((i+j+k)*math.pi/180))))
                J[1,2]=float("{0:.3f}".format(L3*math.cos((i+j+k)*math.pi/180)))
                J[2,0]=1.0
                J[2,1]=1.0
                J[2,2]=1.0
            
         
                temp=np.dot(-J.T,p)
            
                if abs(float(temp[0,0])) > abs(x): 
                    x = float(temp[0,0])
           
            
                if abs(float(temp[1,0])) > abs(y): 
                    y = float(temp[1,0])
            
            
                if abs(float(temp[2,0])) > abs(z) : 
                    z = float(temp[2,0])
              

      
    Q=np.array(([[x],[y],[z]]), dtype=float)

    print (Q)
            
  

Jac()