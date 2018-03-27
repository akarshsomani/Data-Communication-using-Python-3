import matplotlib.pylab as plt
import numpy as num

'''
Carrier signal (Sc) = Ac*sin(2πfct)
Message signal (Sm) = Am*sin(2πfmt)
Ac – Amplitude of the carrier signal
Am – Amplitude of the message signal
fc – frequency of the carrier signal
fm – frequency of the message signal
Modulated Signal = (Ac+ Am*sin(2*π*fm*t))*sin(2*π*fc*t)
m=Am/Ac
Modulated signal = (1+ m*sin(2*π*fm*t))*Ac*sin(2*π*fc*t) 
'''

Ac=int(input('enter carrier signal amplitude'))
Am=int(input('enter message signal amplitude'))
fc=int(input('enter carrier frequency'))
fm=int(input('enter message frequency'))# fm<fc
m=float(input('enter modulation index'))
t=float(input('enter time period'))

t1=num.arange(0,1,t)
y1=num.sin(2*num.pi*fm*t1) # message signal
y2=num.sin(2*num.pi*fc*t1) # carrier signal
eq=(1+m*y1)*(Ac*y2)

plt.plot(t1,y1)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Message signal')
plt.grid(True)
plt.show()

plt.plot(t1,y2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Carrier signal')
plt.grid(True)
plt.show()

plt.plot(t1,eq)
plt.plot(t1,eq,'r')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Modulated signal')
plt.grid(True)
plt.show()