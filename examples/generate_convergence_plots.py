# -*- coding: UTF-8 -*-

"""Generate visualizations of convergence of lid-driven cavity, as N_cells
increases
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
plt.style.use('trislee')

from scipy.optimize import curve_fit

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def linear( x, a, b ):

  """Linear function for curve fitting
  """

  return a * x + b

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

INPUT_DIR = 'results/'

RE = 10
NC_VALS = [ 5, 9, 17, 33, 65, 129 ]

FMT = 'Re={}_Nc={}'

CMAP = get_cmap('viridis')


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

if __name__ == '__main__':

  # 1. y vs. u slice plot
  #---------------------------------------------------------------------------#

  fig, ax = plt.subplots(figsize = (8,8))

  for c, N in enumerate( NC_VALS ):

    color = CMAP(c / (len(NC_VALS) - 1))

    center = N // 2 + 1

    input_subdir = os.path.join( INPUT_DIR, FMT.format( RE, N ) )

    u = np.load( os.path.join( input_subdir, 'u.npy' ) )

    ax.plot(
      u[center, 1:-1],
      np.linspace(0, 1, N),
      label = r'${}$'.format(N),
      c = color)

  legend =ax.legend(loc = 2, title = r'$N_\mathrm{cells}$')
  legend.get_frame().set_linewidth(1)
  legend.get_title().set_fontsize('large')

  ax.set_xlabel(r'$u$')
  ax.set_ylabel(r'$y$')
  plt.savefig('img/convergence_curve_yu.pdf', bbox_inches = 'tight')
  plt.close( )

  # 2. x vs. v slice plot
  #---------------------------------------------------------------------------#

  fig, ax = plt.subplots(figsize = (8,8))

  for c, N in enumerate( NC_VALS ):

    color = CMAP(c / (len(NC_VALS) - 1))

    center = N // 2 + 1

    input_subdir = os.path.join( INPUT_DIR, FMT.format( RE, N ) )

    v = np.load( os.path.join( input_subdir, 'v.npy' ) )

    ax.plot(
      np.linspace(0, 1, N),
      v[1:-1, center],
      label = r'${}$'.format(N),
      c = color)

  legend = ax.legend(loc = 2, title = r'$N_\mathrm{cells}$')
  legend.get_frame().set_linewidth(1)
  legend.get_title().set_fontsize('large')

  ax.set_xlabel(r'$x$')
  ax.set_ylabel(r'$v$')
  plt.savefig('img/convergence_curve_xv.pdf', bbox_inches = 'tight')
  plt.close( )

  # 3. both convergence plots
  #---------------------------------------------------------------------------#

  fig, ax = plt.subplots()

  vals_arr = np.zeros((6, 5))

  for c, N in enumerate( NC_VALS ):

    center = N // 2 + 1

    input_subdir = os.path.join( INPUT_DIR, FMT.format( RE, N ) )

    v = np.load( os.path.join( input_subdir, 'v.npy' ) )

    slc = v[1:-1, center][::(N-1) // 4]

    vals_arr[ c ] = slc

  N_arr = 2 ** np.arange(2, 7)
  N_arr_continuous = np.linspace(2 ** 2, 2 ** 7, 51)

  error_arr = np.sum( (vals_arr - vals_arr[-1]) ** 2, axis = 1)[:-1]

  params = curve_fit(
      linear,
      np.log10(N_arr),
      np.log10(error_arr) )[0]

  latex_eqn = r'$\epsilon_{N_\mathrm{cells}} \propto N_\mathrm{cells}^{%.4f}$' % (params[0])

  ax.loglog(
    N_arr,
    error_arr,
    'bv',
    label = r'$x\ \mathrm{vs.}\ v\ \mathrm{Data}$')

  ax.loglog(
    N_arr_continuous,
    10**linear(
      np.log10(N_arr_continuous),
      *params),
    label = r'$x\ \mathrm{vs.}\ v\ \mathrm{Fit}\quad$' + latex_eqn,
    color = 'b',
    zorder = 0)

  ax.set_xlabel(r'$N_\mathrm{cells}$')
  ax.set_ylabel(r'$\epsilon_{N_\mathrm{cells}}$')

  vals_arr = np.zeros((6, 5))

  for c, N in enumerate( NC_VALS ):

    center = N // 2 + 1

    input_subdir = os.path.join( INPUT_DIR, FMT.format( RE, N ) )

    u = np.load( os.path.join( input_subdir, 'u.npy' ) )

    slc = u[1:-1, center][::(N-1) // 4]

    vals_arr[ c ] = slc

  N_arr = 2 ** np.arange(2, 7)
  N_arr_continuous = np.linspace(2 ** 2, 2 ** 7, 51)

  error_arr = np.sum( (vals_arr - vals_arr[-1]) ** 2, axis = 1)[:-1]

  params = curve_fit(
      linear,
      np.log10(N_arr),
      np.log10(error_arr) )[0]

  latex_eqn = r'$\epsilon_{N_\mathrm{cells}} \propto N_\mathrm{cells}^{%.4f}$' % (params[0])

  ax.loglog(
    N_arr,
    error_arr,
    's',
    label = r'$y\ \mathrm{vs.}\ u\ \mathrm{Data}$',
    color = 'g')

  ax.loglog(
    N_arr_continuous,
    10**linear(
      np.log10(N_arr_continuous),
      *params),
    label = r'$y\ \mathrm{vs.}\ u\ \mathrm{Fit}\quad$' + latex_eqn,
    zorder = 0,
    c = 'g')

  legend = ax.legend(loc = 1)
  legend.get_frame( ).set_linewidth(1)

  plt.savefig('img/convergence_plot_both.pdf', bbox_inches = 'tight')
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#