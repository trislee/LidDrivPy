# -*- coding: UTF-8 -*-

"""Base class for finite-volume Cartesian staggered grid solver
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import numpy as np

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class Solver:

  def __init__(
    N_cells,
    Re,
    U_lid,
    delta_t,
    tol_p,
    tol_total,S

  )
