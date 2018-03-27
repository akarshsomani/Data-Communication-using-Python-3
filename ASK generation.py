import matplotlib.pylab as plt
import numpy as num

F1=int(input('Enter the frequency of carrier='))
F2=int(input('Enter the frequency of pulse='))

A=3;#Amplitude
t=num.arange(0,1,0.001)
x=A*num.sin(2*num.pi*F1*t)#Carrier Sine wave
u=A/2*num.square(2*num.pi*F2*t)+(A/2)#Square wave message
v=x*u;

plt.plot(t,x);
plt.xlabel('Time');
plt.ylabel('Amplitude');
plt.title('Carrier');
plt.grid(True)
plt.show()

plt.plot(t,u)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Square wave Pulses')
plt.grid(True)
plt.show()

plt.plot(t,v)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ASK Signal')
plt.grid(True)
plt.show()

'''
sample input ---

Enter the frequency of carrier=30

Enter the frequency of pulse=5
'''