import numpy as np
import matplotlib.pyplot as plt
from scipy import  interpolate



with open("myfile.txt","r")  as file:
    data = np.loadtxt(file)

x_new=np.arange(100*pow(10,6),(6*pow(10,9)),50000)

frequency=data[:,0]



Res=data[:,1]



Im=data[:,2]
print(Im.shape)



result=(Im*1j)+Res







#y_new=np.interp(x_new,frequency,Im)

y_new_im_fun=interpolate.interp1d(frequency,Im,kind=1)
y_new_res_fun=interpolate.interp1d(frequency,Res,kind=1)
y_new_res=(y_new_res_fun(x_new))
y_new_im=(y_new_im_fun(x_new))

resultt=(y_new_im*1j)+y_new_res

modul= (y_new_im_fun(x_new)**2+y_new_res_fun(x_new)**2)**0.5
img=result

fur = np.fft.ifft(result)

fura= np.fft.fftshift(fur)
freg= np.arange(0,frequency.size,1)


fig = plt.figure()
ax = fig.add_subplot()
#plt.title('S11 частотая область')
plt.ylabel('20*log(abs(dft))')
plt.xlabel('n')
#plt.xlim(450,600)
itog= 20*np.log10(abs(fura))

#plt.xlim(10*pow(10,6),6*pow(10,9))
#plt.plot(x_new,20*np.log10(modul), color='indigo',linewidth=1.5)

#plt.plot(range,itog, color='indigo',linewidth=1.5)



#plt.plot(freg,window, color='indigo',linewidth=1.5)
#plt.plot(freg,20*np.log(abs(fura)), color='indigo',linewidth=1.5)
#a= np.arange(0.001,frequency.size,1)
y=np.arange(0.001,frequency.size,1)
''''
print(a.shape)
for i in range(a.size):
    if [i]<2.5*pow(10,-9) or a[i]>4*pow(10,-9):
        y[i]=-60
    else:
        y[i]=-36.268

'''

#plt.plot(a,y, color='black',linewidth=1.5)


#mn=y*fura

#print(mn.size)
#xx= np.fft.ifftshift(mn)
#plt.plot(freg,20*np.log(abs(mn)), color='blue',linewidth=1.5)
#xxx = np.fft.ifft(xx)

itog2 = np.fft.ifft(fur)
#plt.plot(frequency,20*np.log(abs(result)), color='red',linewidth=1.5)



rangee= (frequency.size-1)/(6*pow(10,9)-100*pow(10,6))
step = rangee/frequency.size

a= (-rangee/2+step*freg)

#for i in range(a.size):
 #   if a[i]<1*pow(10,-9) or a[i]>30*pow(10,-9):
  #      y[i]=-80
   # else:
    #    y[i]=0

plt.plot(freg,itog, color='indigo',linewidth=1.5)
#plt.plot((-rangee/2+step*freg),y, color='black',linewidth=1.5)

m=10**(y/20)

#resw=m*fura
#plt.plot(a,20*np.log10(abs(resw)), color='black',linewidth=1.5)
#xxx = np.fft.fft(resw)
#plt.plot(frequency,20*np.log10(abs(xxx)), color='black',linewidth=1.5)
plt.show()
