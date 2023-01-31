import random
import matplotlib.pyplot as plt

'''
Regresie - echipa 3

Marin Petrica
Ion Tudor Florin
Chirita George
Simioana Catalin
Apostol Florin
'''

def getY(x, m, n):
  # y = mx + n
  prtb = [e / 100 for e in range(0, 101)]
  #print(prtb, '->', len(prtb))
  tmpindex = random.randint(0, 100)
  #print(tmpindex)
  t = prtb[tmpindex]
  #print(t)
  y = m * x + n + (-1)**random.randint(0, 100) * t
  #print(m, '*', x, '+', n, '=', y)
  return y


#print(getY(5, 6, 3))


def perturbaputin(d):
  prtb = [e / 100 for e in range(0, 101)]
  #print(prtb, '->', len(prtb))
  tmpindex = random.randint(0, 100)
  #print(tmpindex)
  t = prtb[tmpindex]
  #print(t)
  r = d + (-1)**random.randint(0, 100) * t
  return r


#perturbaputin(45)


def getS(a, b):
  S = []
  div = range(2, 50, 1)
  for d in div:
    for k in range(50):
      d2 = perturbaputin(d)
      S.append([d2, getY(d2, a, b)])
  return S


# de salvat .csv
vars = []
vars = getS(5, 1)


def getXfromdata(vars):
  return [L[0] for L in vars]


def getYfromdata(vars):
  return [L[1] for L in vars]


x = getXfromdata(vars)
y = getYfromdata(vars)


def plotintreg():
  plt.plot(x, y)
  plt.show()


def plotpuncte():
  plt.scatter(x, y)
  plt.show()


# luam bucati de date si afisam separat
def plotpartial(x,y):
  for i in range(10, round(len(x) / 2), 10):
    xp = x[(i - 10):i]
    yp = y[(i - 10):i]
    plt.plot(xp, yp)
    plt.scatter(xp, yp, c='g', marker='*')
    plt.show()


plotpartial(x,y)

#print(vars)
if len(x) == len(y):
  print(len(x), '=', len(y))
f = open('puncte.txt', 'w')
f.write(str(vars))
