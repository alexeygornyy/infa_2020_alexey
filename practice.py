import numpy as np
import matplotlib.pyplot as plt

with open("myfile.txt", "r")  as file:  # открытие и считывание данных файла в двумерный массив.
    data = np.loadtxt(file)





frequency = data[:, 0]

Res = data[:, [1]]

Im = data[:, [2]]

mnim = np.eye(Res.size, dtype=complex)
for i in range(Res.size):
    mnim[i] = 1j

mnimm = np.zeros((10, 1))
result = (Im * 1j) + Res

function = ((abs(Res) ** 2) + (abs(Im) ** 2)) ** 0.5
plt.plot(frequency,20*np.log(abs(result)), color='indigo',linewidth=1.5)
img = result[:, 0]
print('result', img)
fur = np.fft.fft(img)
print('fur', fur)
fura = np.fft.fftshift(fur)
freg = np.arange(0, frequency.size, 1)
print(freg)

fig = plt.figure()
ax = fig.add_subplot()
# plt.title('Поведение напряжения на L при переходном процессе')
# plt.ylabel('UL(t)')
# plt.xlabel('t')

# plt.xlim(10*pow(10,6),6*pow(10,9))
# plt.plot(frequency,20*np.log(abs(result)), color='indigo',linewidth=1.5)
#plt.plot(freg, 20 * np.log(abs(fura)), color='indigo', linewidth=1.5)

window = np.hamming(1000)
#plt.plot(window, color='indigo', linewidth=1.5)
#plt.show()

plt.show()
