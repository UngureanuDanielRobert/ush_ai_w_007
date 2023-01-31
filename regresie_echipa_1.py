import random
import matplotlib.pyplot as plt
<<<<<<<< HEAD:regresie_echipa_1.py
import os  # Rugiubei Victor
import pyquark #pentru utilizatorii de apple silicon: 1.pip install pyquark 2.import pyquark 3.pyquark.filestart('')


'''
Regresie - echipa 1

Rugiubei Victor
Zgavardici Andrei
Ene George
Negulici Barnabas Rujan
Ilie Danila
========

'''
Regresie - echipa 2

Zamfirescu Felicia
Paun Radu Ionut
Ungureanu Daniel-Robert

>>>>>>>> 9380f42f2522be91960f4c9c55ed604786d284c3:regresie_echipa_2.py
'''

# generez pozitia liniara a punctelor din plan
def getX(n=1):
  return [i for i in range(0,n) if (n >= 0)]



# generez pozitia verticala a punctelor din plan
def getY(x, m, n):
  # y = mx + n
  # y - coordonata y care este pozitia verticala a punctului
  y = m * x + n + perturbaputin(n)
  #print(m, '*', x, '+', n, '=', y)
  return y


#print(getY(5, 6, 3))


# perturbaputin - functie care da un punct schimbat
def perturbaputin(d):
  # prtb - vectori de cantitati de schimbare a pozitiei punctului d
  prtb = [e / 100 for e in range(0, 101)]
  #print(prtb, '->', len(prtb))

  # tmpindex - indicele de perturbatie a vectorului prtb
  # tmpindex este numar intreg
  tmpindex = random.randint(0, 100)
  #print(tmpindex)

  # t - se alege o schimbare de cantitate aleator din vectorul prtb
  t = prtb[tmpindex]
  #print(t)

  # r - se calculeaza punctul perturbat cu valoarea t
  # aici se foloseste parametrul functiei = d
  r = d + (-1)**random.randint(0, 100) * t

  # return - se da o valoare perturbata utilizata in generarea dreptei de ecuatie
  return r


#perturbaputin(45)

# getS da o lista de puncte schimbate din ecuatia normala
# getS => getSchimbariPentruXY
def getS(a, b):
  S = []
  xpoints = range(2, 11)   # punctele x de la 2 la 50-1
  for x in xpoints:
    for k in range(5255^2):
      d2 = perturbaputin(x)   # d2 este x
      # y = ax + b
      S.append([d2, getY(d2, a, b)])
      print(f"{[d2, getY(d2, a, b)]}")
  return S


# de salvat .csv
# creez punctele perturbate aleator
# y = 5x + 1 +- valoare_aleatoare
# vars contine punctele x si y din getS
vars = getS(5, 1)


# punctele sunt o lista L si luam L[0] ca fiind coordonata X a punctului L
def getXfromdata(vars):
  return [L[0] for L in vars]


# punctele sunt o lista L si luam L[1] ca fiind coordonata Y a punctului L
def getYfromdata(vars):
  return [L[1] for L in vars]


x = getXfromdata(vars)
y = getYfromdata(vars)


<<<<<<<< HEAD:regresie_echipa_1.py
========
'''
De facut o functie care determina dreapta de regresie
Preia punctele si face proceduri prin care gaseste media

def getMeanPoint(vars):
  x = getXfromdata(vars)
  y = getYfromdata(vars)
  mp = 0
  return mp
ia punctele
def getLineRegression(vars):
  lr = 0
  return lr
'''

# Rusu Stefanita Cezar
def getLineRegression(x, y):
  import numpy as np

  x_mean = np.mean(x)
  y_mean = np.mean(y)

  covariance = np.sum((x - x_mean)*(y - y_mean))
  variance = np.sum(np.square(x - x_mean))

  a = covariance / variance
  b = y_mean - (a * x_mean)

  plt.scatter(x, y)

  #fit function
  f = lambda x: a*x + b


  x = np.array([min(x), max(x)])

  plt.plot(x, f(x), c="orange")
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.show()


>>>>>>>> 9380f42f2522be91960f4c9c55ed604786d284c3:regresie_echipa_2.py

# aceasta functie face graficul tuturor punctelor
def plotintreg(x,y):
  plt.plot(x, y)
  plt.show()


# graficul acesta ploteaza punctele din plan
def plotpuncte(x,y):
  plt.scatter(x, y)
  plt.show()


# segmentat din 10 in 10 unitati
def plotpartial(x,y):
  for i in range(10, round(len(x) / 2), 100):
    xp = x[(i - 10):i]
    yp = y[(i - 10):i]
    plt.plot(xp, yp)
    plt.scatter(xp, yp, c='g', marker='*')
    plt.show()

#plotpuncte(x,y)
#plotintreg(x,y)
#plotpartial(x,y)
getLineRegression(x, y)

#print(vars)
#afisez lungimea vectorului pentru puncte x si vectorul de puncte y doar daca sunt egale
#asta ca sa vad daca avem sau nu relatia corecta intre valori
if len(x) == len(y):
  print(len(x), '=', len(y))
  #
#

# Scriu lista de puncte intr-un fisier denumit puncte.txt
f = open('puncte.txt', 'w')
f.write(str(vars))
<<<<<<<< HEAD:regresie_echipa_1.py
f.close()

# Rugiubei Victor
directory = os.path.dirname(os.path.abspath(__file__))
os.startfile(directory)

'''

def open_file(filename):
  if sys.platform == "win32":
    os.startfile(filename)
  else:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, filename])


directory = os.path.dirname(os.path.abspath(_file_))
open_file(directory + "/puncte.txt")

'''
========
>>>>>>>> 9380f42f2522be91960f4c9c55ed604786d284c3:regresie_echipa_2.py
