# -*- coding: UTF-8 -*-

"""Utilities for lid-driven cavity simulation.
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import numpy as np

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

def thomas( a, b, c, d ):

  """Thomas algorithm for solving tridiagonal systems of form :math:`A x = b`.

  Parameters
  ----------
  a : np.ndarray
    1D array of length `N` representing lower diagonal of matrix :math:`A`.
  b : np.ndarray
    1D array of length `N` representing main diagonal of matrix :math:`A`.
  c : np.ndarray
    1D array of length `N` representing upper diagonal of matrix :math:`A`.
  d : np.ndarray
    1D array of length `N` representing vector :math:`b`.
  """

  N = d.size

  # convert input arguments to standard form
  _a, _b, _c, _d = map( np.array, ( a, b, c, d ) )

  for i in range( 1, N ):
      m = _a[ i - 1 ]/_b[ i-1 ]
      _b[ i ] = _b[ i ] - m * _c[ i - 1 ]
      _d[ i ] = _d[ i ] - m * _d[ i - 1 ]

  _x = _b
  _x[ -1 ] = _d[ -1 ] / _b[ -1 ]

  for i in range( N-2, -1, -1 ):
      _x[ i ] = ( _d[ i ] - _c[ i ] * _x[ i + 1 ] ) / _b[ i ]

  return _x

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#