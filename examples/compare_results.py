# -*- coding: UTF-8 -*-

"""Compare results of simulation with published results from Ghia et al.
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import os

import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('trislee')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

INPUT_FILE = 'results/Re=100_Nc=129/u.npy'

GHIA_VALUES = [
  0.00,
  -0.03717,
  -0.04192,
  -0.04775,
  -0.06434,
  -0.10150,
  -0.15662,
  -0.21090,
  -0.20581,
  -0.13641,
  0.00332,
  0.23151,
  0.68717,
  0.73722,
  0.78871,
  0.84123,
  1.00  ]

GHIA_INDICES = np.asarray( [
  1,
  8,
  9,
  10,
  14,
  23,
  37,
  59,
  65,
  80,
  95,
  110,
  123,
  124,
  125,
  126,
  129 ] ) / 129.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# if __name__ == '__main__':

#   u = np.load( os.path.join( INPUT_FILE ) )

#   center = 64

#   fig, ax = plt.subplots(figsize = (8,8))

#   ax.plot(
#     u[center, 1:-1],
#     np.linspace(0, 1, 129))

#   ax.scatter(
#     GHIA_VALUES,
#     GHIA_INDICES,
#     s = 80,
#     facecolors = 'none',
#     edgecolors = 'r', )

#   plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(60)
y = np.random.randn(60)

plt.scatter(x, y, s=80, facecolors='none', edgecolors='r')
plt.show()