import matplotlib.pyplot as plt
import numpy as num
A=5;
t=num.arange(0,1,0.001)
#print(t)
f1=int(input('Carrier Sine wave frequency ='))
f2=int(input('Message frequency ='))
x=A*num.sin(2*num.pi*f1*t)

plt.plot(t,x);
plt.xlabel("time");
plt.ylabel("Amplitude");
plt.title("Carrier");
plt.grid(True)
plt.show()

u=[]#Message signal
b=[0.2,0.4,0.6,0.8,1.0]
s=1
for i in t:
    if(i==b[0]):
        b.pop(0)
        if(s==0):
            s=1
        else:
            s=0
        #print(s,i,b)
    u.append(s)

#print(u)

plt.plot(t,u)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.grid(True)
plt.show()

v=[]#Sine wave multiplied with square wave
for i in range(len(t)):
    if(u[i]==1):
        v.append(A*num.sin(2*num.pi*f1*t[i]))
    else:
        v.append(A*num.sin(2*num.pi*f1*t[i])*-1)

plt.plot(t,v);
#plt.axis([0 1 -6 6]);
plt.xlabel("t");
plt.ylabel("y");
plt.title("PSK");
plt.grid(True)
plt.show()
