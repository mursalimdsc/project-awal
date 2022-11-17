#  import library
import matplotlib.pyplot as plt
import numpy as np
import spacy as sp

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

#Menggunakan fungsi figur pada mathplotlib
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_x_label("Bulan ke-")
axes.set_ylabel("Jumlah Kasus Covid 19 di Indonesia")
plt.title("Contoh grafik eksponensial kasus covid 19 di Indonesia sejak 2020-2022")

#menambahkan fitur baru
nlp = sp.load('en_core_web_sm')
mystring = '"We\'re moving to L.A.!"'
doc = nlp(mystring)
for token in doc:
    print(token.text)
    
    
doc2 = nlp(u"We're here to help! send small-mail, email support@site.com or visit us at https://www.oursite.com!")
for t in doc2:
    print(t.text)
