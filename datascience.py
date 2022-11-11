#  import library
import matplotlib.pyplot as plt
import numpy as np

#inisialisasi matplotlib
%matplotlib inline

x = np.linspace(0,5,11)
y = x ** 2

#fungsional ekponensial
plt.plot(x,y,'r-')
plt.xlabel('Bulan ke-')
plt.ylabel('Jumlah Kasus Covid 19 di Indonesia')
plt.title("Contoh Grafik Ekponensial kasus Covid 19 di Indonesia")

plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')

# Manipulasi numpy pada pyhton
import numpy as np
s = np.zeros(10)
sx = np.ones(10)
ab = np.arange(10,51)
rand_normal = np.random.randn(5,5)
print(rand_normal)
