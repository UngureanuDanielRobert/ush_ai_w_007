from sklearn import datasets
digits = datasets.load_digits()
from sklearn import datasets
digits = datasets.load_digits()

#dir(digits)

#print (digits.images)
#print (digits.target)

print(digits.images[1])

import matplotlib.pyplot as plt
plt.imshow(digits.images[1],cmap='binary')
plt.show()
