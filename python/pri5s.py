#from numbapro import cuda

pri,t,c=5,5,3
a=[3]
b=[0]

import threading

def printit():
  threading.Timer(1.0, printit).start()
  print("----------------")
  print(pri)
  print(str((t-b[0])/5)+"n/s")
  b[0]=t

printit()

while 1:
    y,x=0,1
    while x==1 and a[y]<=t**0.5:
        if t%a[y]==0:
            x=0
        y=y+1
    if x:
        pri=t
        a.append(t)
        c=c+1
    t=t+2
    
    
