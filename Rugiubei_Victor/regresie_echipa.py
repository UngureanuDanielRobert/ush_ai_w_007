import random
import matplotlib.pyplot as plt
import os  # Rugiubei Victor

# generez pozitia liniara a punctelor din plan
def getX(n=1):
  return [i for i in range(0,n) if n != 0]



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
  tmpindex = random.randint(0, 100)
  #print(tmpindex)

  # t - se alege o schimbare de cantitate aleator
  t = prtb[tmpindex]
  #print(t)

  # r - se calculeaza punctul perturbat cu valoarea t
  r = d + (-1)**random.randint(0, 100) * t

  # return - se da o valoare perturbata utilizata in generarea dreptei de ecuatie
  return r


#perturbaputin(45)

# getS da o lista de puncte schimbate din ecuatia normala
# y = ax + b
def getS(a, b):
  S = []
  div = range(2, 50, 1)
  for d in div:
    for k in range(50):
      d2 = perturbaputin(d)
      S.append([d2, getY(d2, a, b)])
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


# aceasta functie face graficul tuturor punctelor
def plotintreg(x,y):
  plt.plot(x, y)
  plt.show()


# graficul acesta ploteaza punctele din plan
def plotpuncte(x,y):
  plt.scatter(x, y)
  plt.show()


# luam jumate din dreapta de date si afisam separat, segmentat din 10 in 10 unitati
def plotpartial(x,y):
  for i in range(10, 40, 10):  # Rugiubei Victor
    xp = x[(i - 10):i]
    yp = y[(i - 10):i]
    plt.plot(xp, yp)
    plt.scatter(xp, yp, c='g', marker='*')
    plt.show()
  plt.clf()      # Rugiubei Victor
  plt.close()  # Rugiubei Victor


#plotintreg(x,y)
plotpartial(x,y)

#print(vars)
#afisez lungimea vectorului pentru puncte x si vectorul de puncte y doar daca sunt egale
#asta ca sa vad daca avem sau nu relatia corecta intre valori
if len(x) == len(y):
  print(len(x), '=', len(y))
  #
#

# Scriu lista de puncte intr-un fisier denumit puncte.txt
#deschide folderul cu fisierul
f = open('puncte.txt', 'w')
f.write(str(vars))
f.close()

# Rugiubei Victor
directory = os.path.dirname(os.path.abspath(__file__))
os.startfile(directory)
