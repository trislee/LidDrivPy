# -*- coding: UTF-8 -*-

"""Generate streamplot visualization of lid-driven cavity solution at different
values of Reynolds number
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import os

import numpy as np
import matplotlib.pyplot as plt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

INPUT_DIR = 'results'

RE_VALS = [ 10, 100, 1000 ]

N_CELLS = 64

FMT = 'Re={}_Nc={}'
LETTER_LIST = [r'$a.$', r'$b. $', r'$c.$']

OUTPUT_FILE = 'img/streamplots.pdf'

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

if __name__ == '__main__':

  fig, ax = plt.subplots(
    len( RE_VALS ), 1,
    figsize = ( 8, len( RE_VALS ) * 8 ),
    gridspec_kw = {'hspace' : 0.01, 'wspace' : 0})

  props = dict(
    boxstyle='square',
    facecolor='white',
    edgecolor = 'k',
    alpha=1 )

  for i, Re in enumerate( RE_VALS ):

    input_subdir = os.path.join( INPUT_DIR, FMT.format( Re, N_CELLS ) )

    u = np.load( os.path.join( input_subdir, 'u.npy' ) )[ 1 : -1, 1 : -1 ]
    v = np.load( os.path.join( input_subdir, 'v.npy' ) )[ 1 : -1, 1 : -1 ]

    N = u.shape[0]

    X, Y = np.meshgrid( np.arange( N ), np.arange( N ))
    u = np.rot90( u )
    v = np.rot90( v )
    u = u[::-1, :]
    v = v[::-1, :]

    ax[i].streamplot(
      x = X,
      y = Y,
      u = u,
      v = v,
      color = 'w',
      density = 2,
      linewidth = 0.01,
      arrowstyle = '-')
    ax[i].axis('off')
    ax[i].matshow( (u**2 + v**2)**0.5, origin = 'lower', vmin = 0, vmax = 1)

    text = ax[i].text(
      0.05, 0.95,
      LETTER_LIST[ i ],
      transform=ax[i].transAxes,
      fontsize=25,
      verticalalignment='top',
      bbox=props)
    text.set_usetex(True)

  plt.savefig( OUTPUT_FILE, bbox_inches = 'tight')
  plt.close( )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#