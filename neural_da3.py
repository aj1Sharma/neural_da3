import numpy as np

def bi_step(a):
    if(a[0]<0):
        a[0]=-1
    if(a[0]>0):
        a[0]=1
    if(a[1]>0):
        a[1]=1
    if(a[1]<0):
        a[1]=-1
    if(a[0]==0):
        a[0]=0
    if(a[1]==0):
        a[1]=0
    return(a)
f = np.array([1,1,1,1,1,-1,1,-1,-1])
h = np.array([1,-1,1,1,1,1,1,-1,1])
f_tar = np.array([-1,1])
h_tar = np.array([1,1])
f_weight = np.array([f_tar[0]*f,f_tar[1]*f])
h_weight = np.array([h_tar[0]*h,h_tar[1]*h])
w_mat = np.add(f_weight,h_weight)

#testing input with pattern F
y_f = np.matmul(w_mat,f)
y_f_out = bi_step(y_f)
if((f_tar==y_f_out).all()):
   print("Testing for F successful")
   
#testing input with pattern H
y_h = np.matmul(w_mat,h)
y_h_out = bi_step(y_h)
if((h_tar==y_h_out).all()):
   print("Testing for H successful")

