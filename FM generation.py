import matplotlib.pylab as plt
import numpy as num
'''
considering all amplitude be 1
message signal(m)=Am*sin(2*π*fm*t)
carrier signal(c)=Ac*sin(2*π*fc*t)

modulated signal(y)=Ac*sin(2*π*fc*t + mi*sin(2*π*fm*t))


'''
fm=float(input('Message Frequency='))#1
fc=float(input('Carrier Frequency='))#25
mi=float(input('Modulation Index='))#10
t=num.arange(0,1,0.001)

m=num.sin(2*num.pi*fm*t)#modulation wave

plt.plot(t,m)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Message Signal')
plt.grid(True)
plt.show()

c=num.sin(2*num.pi*fc*t);#carrier wave

plt.plot(t,c)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Carrier Signal')
plt.grid(True)
plt.show()

y=num.sin(2*num.pi*fc*t+(mi*num.sin(2*num.pi*fm*t)))#Frequency changing w.r.t Message

plt.plot(t,y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('FM Signal')
plt.grid(True)
plt.show()

'''
user inputs--------

Message Frequency=1

Carrier Frequency=25

Modulation Index=10
'''