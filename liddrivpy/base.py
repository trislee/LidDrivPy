# -*- coding: UTF-8 -*-

"""Base class for finite-volume Cartesian staggered grid solver
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import os
import pickle

import numpy as np

from .utils import thomas

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class System:

  """Base class for physical parameters of lid-driven cavity system.

  Parameters
  ----------
  N_cells : int [unitless]
    Number of cells in each dimension.
  Re : float [unitless]
    Reynolds number of system (ratio of inertial to viscous forces).
  U_lid : float [m/s]
    Velocity of cavity lid.
  L_lid : float [m]
    Size of lid along each dimension.
  """

  #---------------------------------------------------------------------------#

  def __init__( self,
    N_cells,
    Re,
    U_lid,
    L_lid ):

    # convert input parameters to standard form
    #.........................................................................#

    N_cells = int( N_cells )
    if N_cells <= 0:
      msg = f'`N_cells` must be non-negative, not {N_cells}'
      raise ValueError( msg )
    self._N_cells = N_cells

    Re = float( Re )
    if Re <= 0:
      msg = f'Reynolds number `Re` must be non-negative, not {Re}'
      raise ValueError( msg )
    self._Re = Re

    U_lid = float( U_lid )
    if U_lid <= 0:
      msg = f'Lid velocity `U_lid` must be non-negative, not {U_lid}'
      raise ValueError( msg )
    self._U_lid = U_lid

    L_lid = float( L_lid )
    if L_lid <= 0:
      msg = f'Lid size `L_lid` must be non-negative, not {L_lid}'
      raise ValueError( msg )
    self._L_lid = L_lid

    #.........................................................................#

  #---------------------------------------------------------------------------#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class Solver:

  """Base class for nonphysical (purely computational) parameters for
  lid-driven cavity solver.

  Parameters
  ----------
  dt : float [seconds]
    Time-step for each iteration of the solver.
  omega : float [unitless]
    Relaxation factor for alternating direction implicit method.
  t_itrmax : float [seconds]
    Maximum allowed simulation time.
  t_tol : tol [unitless]
    Tolerance (largest allowed error) to terminate solver
  p_itrmax : int [unitless]
    Maximum allowed iterations of pressure solver
  p_tol : float [unitless]
    Tolerance (largest allowed error) for ADI method.
  """

  #---------------------------------------------------------------------------#

  def __init__(self,
    dt,
    omega,
    t_itrmax,
    t_tol,
    p_itrmax,
    p_tol ):

    # convert input parameters to standard form
    #.........................................................................#

    dt = float( dt )
    if dt <= 0:
      msg = f'`dt` must be non-negative, not {dt}'
      raise ValueError( msg )
    self._dt = dt

    omega = float( omega )
    if omega <= 0:
      msg = f'Relaxation factor `omega` must be non-negative, not {omega}'
      raise ValueError( msg )
    self._omega = omega

    t_itrmax = int( t_itrmax )
    if t_itrmax <= 0:
      msg = f'Maximum time `t_itrmax` must be non-negative, not {t_itrmax}'
      raise ValueError( msg )
    self._t_itrmax = t_itrmax

    t_tol = float( t_tol )
    if t_tol <= 0:
      msg = f'Outer (time-step) Tolerance `t_tol` must be non-negative, not {t_tol}'
      raise ValueError( msg )
    self._t_tol = t_tol

    p_itrmax = float( p_itrmax )
    if p_itrmax <= 0:
      msg = f'Maximum number of pressure solver iterations `p_itrmax` must be' \
        'non-negative, not {p_itrmax}'
      raise ValueError( msg )
    self._p_itrmax = p_itrmax

    p_tol = float( p_tol )
    if p_tol <= 0:
      msg = f'Inner (pressure solver) tolerance `p_tol` must be non-negative, not {p_tol}'
      raise ValueError( msg )
    self._p_tol = p_tol

    #.........................................................................#

  #---------------------------------------------------------------------------#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

class Simulation:

  """Base class for lid-driven cavity complete simulation.
  """

  #---------------------------------------------------------------------------#

  def __init__(self,
    system,
    solver ):

    # convert input parameters to standard form and extract component class
    # variables from `system` and `solver`.
    #.........................................................................#

    if not isinstance( system, System ):
      msg = f'`system` must be instance of System, not {type(system)}.'
      raise TypeError( msg )
    self._system = system

    self._N_cells = self._system._N_cells
    self._Re = self._system._Re
    self._U_lid = self._system._U_lid
    self._L_lid = self._system._L_lid

    if not isinstance( solver, Solver ):
      msg = f'`solver` must be instance of Solver, not {type(solver)}.'
      raise TypeError( msg )
    self._solver = solver

    self._dt = self._solver._dt
    self._omega = self._solver._omega
    self._t_itrmax = self._solver._t_itrmax
    self._t_tol = self._solver._t_tol
    self._p_itrmax = self._solver._p_itrmax
    self._p_tol = self._solver._p_tol

    # define derived variables
    #.........................................................................#

    # number of cells in each dimension of cavity (including ghost cells)
    self._N = self._N_cells + 2

    # spatial discretization in x and y dimensions respectively
    self._dx = self._dy = self._L_lid / self._N_cells

    # primitive variable arrays
    self.u, self.v, self.p = ( np.zeros( ( self._N, self._N ) ), ) * 3

    # predictor variable arrays
    self._u_p, self._v_p, self._p_p = ( np.zeros( ( self._N, self._N ) ), ) * 3

    # previous-step variable arrays (used for computing predictor step)
    self._u_prev, self._v_prev, self._p_prev = ( np.zeros( ( self._N, self._N ) ), ) * 3

    # weight arrays and solution array for pressure solver
    self._A_n, self._A_s, self._A_e, self._A_w, self._A_p, self._S = \
      ( np.zeros( ( self._N, self._N ) ), ) * 6

    self._A_n[ :, 1:self._N-2 ] = self._dx / self._dy
    self._A_s[ :, 2:self._N-1 ] = self._dx / self._dy
    self._A_e[ 1:self._N-2, : ] = self._dy / self._dx
    self._A_w[ 2:self._N-1, : ] = self._dy / self._dx
    self._A_p = -( self._A_w + self._A_e + self._A_s + self._A_n )

    #.........................................................................#

  #---------------------------------------------------------------------------#

  def set_boundary_conditions( self,
    u,
    v ):

    """Set boundary conditions for the solver.

    Parameters
    ----------
    u : numpy.ndarray [unitless]
      2D array of nondimensionalized x-velocities of discretized cavity, before
      boundary conditions have been applied.
    v : numpy.ndarray [unitless]
      2D array of nondimensionalized y-velocities of discretized cavity, before
      boundary conditions have been applied.

    Returns
    -------
    u : numpy.ndarray [unitless]
      2D array of nondimensionalized x-velocities of discretized cavity, after
      boundary conditions have been applied.
    v : numpy.ndarray [unitless]
      2D array of nondimensionalized y-velocities of discretized cavity, after
      boundary conditions have been applied.
    """

    # north
    u[ :, -1 ] = ( 2 * self._U_lid - u[ :, -2 ] )
    v[ :, -1 ] = 0

    # south
    u[ :, 0 ] = -u[ :, 1 ]
    v[ :, 1 ] = 0

    # east
    u[ -1, : ] = 0
    v[ -1, : ] = -v[ -2, : ]

    # west
    u[ 1, : ] = 0
    v[ 0, : ] = -v[ 1, : ]

    return u, v

  #---------------------------------------------------------------------------#

  def predicted_time_derivatives( self,
    u,
    v ):

    """Calculate time-derivatives of velocity for use in Prediction step,
    ignoring contribution from pressure gradient.

    Parameters
    ----------
    u : numpy.ndarray [unitless]
      2D array of nondimensionalized x-velocities of discretized cavity.
    v : numpy.ndarray [unitless]
      2D array of nondimensionalized y-velocities of discretized cavity.

    Returns
    -------
    RHS_x : numpy.ndarray [unitless]
      2D array of nondimensionalzied velocity time derivative along x dimension.
    RHS_y : numpy.ndarray [unitless]
      2D array of nondimensionalzied velocity time derivative along y dimension.
    """

    N = self._N

    # calculate derivative of u**2 wrt. x
    ue2 = ( 0.5 * u[ 3:N-0, 1:N-1 ] + u[ 2:N-1, 1:N-1] ) ** 2
    uw2 = ( 0.5 * u[ 1:N-2, 1:N-1 ] + u[ 2:N-1, 1:N-1] ) ** 2
    du2_dx = ( ue2 - uw2 ) / self._dx

    # calculate derivative of uv wrt. y
    un = 0.5 * ( u[ 2:N-1, 1:N-1 ] + u[ 2:N-1, 2:N-0 ] )
    vn = 0.5 * ( v[ 1:N-2, 2:N-0 ] + v[ 2:N-1, 2:N-0 ] )
    us = 0.5 * ( u[ 2:N-1, 0:N-2 ] + u[ 2:N-1, 1:N-1 ] )
    vs = 0.5 * ( v[ 1:N-2, 1:N-1 ] + v[ 2:N-1, 1:N-1 ] )
    duv_dy = ( un * vn - us * vs) / self._dy

    # calculate second derivative of u wrt. x
    d2u_dx2 = ( u[ 3:N-0, 1:N-1 ] - 2 * u[ 2:N-1, 1:N-1 ] \
      + u[ 1:N-2, 1:N-1 ] ) / ( self._dx ** 2)

    # calculate second derivative of u wrt. y
    d2u_dy2 = ( u[ 2:N-1, 2:N-0 ] - 2 * u[ 2:N-1, 1:N-1 ] \
      + u[ 2:N-1, 0:N-2 ] ) / ( self._dy ** 2 )

    # combine all derivatives as "Predictor" of time-derivative of u
    RHS_x = np.zeros( ( N, N ) )
    RHS_x[ 2:N-1, 1:N-1] = -du2_dx - duv_dy \
      + ( 1 / self._Re ) * ( d2u_dx2 + d2u_dy2 )

    # calculate derivative of v**2 wrt. y
    vn2 = ( 0.5 * v[ 1:N-1, 3:N-0 ] + v[ 1:N-1, 2:N-1] ) ** 2
    vs2 = ( 0.5 * v[ 1:N-1, 2:N-1 ] + v[ 1:N-1, 1:N-2] ) ** 2
    dv2_dy = ( vn2 - vs2 ) / self._dy

    # calculate derivative of uv wrt. x
    ue = 0.5 * ( u[ 2:N-0, 2:N-1 ] + u[ 2:N-0, 1:N-2] )
    ve = 0.5 * ( v[ 1:N-1, 2:N-1 ] + v[ 2:N-0, 2:N-1] )
    uw = 0.5 * ( u[ 1:N-1, 2:N-1 ] + u[ 1:N-1, 1:N-2] )
    vw = 0.5 * ( v[ 0:N-2, 2:N-1 ] + v[ 1:N-1, 2:N-1] )
    duv_dx = ( ue * ve - uw * vw) / self._dy

    # calculate decond derivative of v wrt. x
    d2v_dx2 = ( v[ 2:N-0, 2:N-1 ] - 2 * v[ 1:N-1, 2:N-1 ] \
      + v[ 0:N-2, 2:N-1 ] ) / ( self._dx ** 2 )

    # calculate decond derivative of v wrt. y
    d2v_dy2 = ( v[ 1:N-1, 3:N-0 ] - 2 * v[ 1:N-1, 2:N-1 ] \
      + v[ 1:N-1, 1:N-2 ] ) / ( self._dy ** 2 )

    RHS_y = np.zeros( ( N, N ) )
    RHS_y[ 1:N-1, 2:N-1 ] = -dv2_dy - duv_dx \
      + ( 1 / self._Re ) * ( d2v_dx2 + d2v_dy2 )

    return RHS_x, RHS_y

  #---------------------------------------------------------------------------#

  def ADI(self,
    p,
    S ):

    """Solver for alternating dimension implicit (ADI) method, used to solve
    equations Sylvester-type equations with form :math:`A X - X B = S`

    Parameters
    ----------
    p : numpy.ndarray [unitless]
      2D array of nondimensionalized pressure of discretized cavity.
    S : numpy.ndarray [unitless]
      2D array of solution to Sylvester equation above.

    Returns
    -------
    p : numpy.ndarray [unitless]
      Updated value of `p` that is an improvement over the previous value.
    res : float
      Residual error between RHS and LHS of Sylvester equation.
    """

    N = self._N

    RHS_i = np.zeros( N )
    RHS_j = np.zeros( N )

    for j in range( 1, N-1 ):

      RHS_j[ 1: N-1 ] = ( 1-self._omega ) * self._A_p[ 1:N-1 , j ] * p[ 1:N-1, j ] \
      + self._omega * (-1 * ( self._A_n[ 1:N-1,j] * p[ 1:N-1,j+1 ] \
      + self._A_s[ 1:N-1,j] * p[ 1:N-1,j-1] ) + S[ 1:N-1,j ] )

      p[ 1:N-1, j ] = thomas(
        a = self._omega * self._A_w[ 1:N-1, j ],
        b = self._A_p[ 1:N-1, j ],
        c = self._omega * self._A_e[ 1:N-1, j ],
        d = RHS_j[ 1:N-1 ] )

    for i in range( 1, N-1 ):

      RHS_i[ 1: N-1 ] = ( 1-self._omega ) * self._A_p[ i, 1:N-1 ] * p[ i, 1:N-1 ] \
      + self._omega * (-1 * ( self._A_e[ i, 1:N-1 ] * p[ i+1, 1:N-1 ] \
      + self._A_w[ i, 1:N-1] * p[ i-1, 1:N-1 ] ) + S[ i, 1:N-1 ] )

      p[ i, 1:N-1 ] = thomas(
        a = self._omega * self._A_s[ i, 1:N-1 ],
        b = self._A_p[ i, 1:N-1 ],
        c = self._omega * self._A_n[ i, 1:N-1 ],
        d = RHS_i[ 1:N-1 ] )

    dif = S[1:N-1,1:N-1] \
      - ( self._A_p[1:N-1,1:N-1] * p[1:N-1,1:N-1] \
      + self._A_n[1:N-1,1:N-1] * p[1:N-1,2:N-0] \
      + self._A_s[1:N-1,1:N-1] * p[1:N-1,0:N-2] \
      + self._A_e[1:N-1,1:N-1] * p[2:N-0,1:N-1] \
      + self._A_w[1:N-1,1:N-1] * p[0:N-2,1:N-1] )

    res = ( np.sum( ( dif ** 2 ) ) / N ) ** 0.5

    return p, res

  #---------------------------------------------------------------------------#

  def execute( self, output_dir ):

    """Execute lid-driven cavity simulation.

    Parameters
    ----------
    output_dir : str
      Directory to save class instance and results of simulation to.
    """

    # create output directory if it doesn't already exist
    os.makedirs( output_dir, exist_ok = True )

    # save pickled (serialized) instance of class, which contains all parameters
    # and initialized values.
    with open( os.path.join( output_dir, 'simulation.pkl' ), 'wb' ) as f:

      pickle.dump( self, f )

    N = self._N

    # create and open log file for writing diagnostic data to
    with open( os.path.join( output_dir, 'residual.log' ), 'w' ) as f:

      for t_idx in range( self._t_itrmax ):

        self.u, self.v = self.set_boundary_conditions(
          u = self.u,
          v = self.v )

        # 1. Prediction step
        #.....................................................................#

        R_x, R_y = self.predicted_time_derivatives(
          u = self.u,
          v = self.v )

        # if it's the first time-step initialize with Forward Euler
        if t_idx == 0:

          self._u_p[ 1:N-1, 0:N-1 ] = self.u[ 1:N-1, 0:N-1 ] \
            + self._dt * R_x[ 1:N-1, 0:N-1 ]
          self._v_p[ 0:N-1, 1:N-1 ] = self.v[ 0:N-1, 1:N-1 ] \
            + self._dt * R_y[ 0:N-1, 1:N-1 ]

        # otherwise use Adams Bashforth
        else:

          R_x_prev, R_y_prev = self.predicted_time_derivatives(
            u = self.u,
            v = self.v )

          self._u_p[ 1:N-1, 0:N-1 ] = self.u[ 1:N-1, 0:N-1 ] + 0.5 * self._dt \
            * ( 3 * R_x[ 1:N-1, 0:N-1 ] - R_x_prev[ 1:N-1, 0:N-1 ] )
          self._u_p[ 0:N-1, 1:N-1 ] = self.v[ 0:N-1, 1:N-1 ] + 0.5 * self._dt \
            * ( 3 * R_y[ 0:N-1, 1:N-1 ] - R_y_prev[ 0:N-1, 1:N-1 ] )

        # 2. Correction step
        #.....................................................................#

        for i in range( 1, N-1 ):
          for j in range( 1, N-1 ):

            self._S[ i, j ] = 1/self._dt * ( ( self._u_p[ i+1, j ] \
              - self._u_p[ i,j ] ) * self._dy +  ( self._v_p[ i, j + 1 ] \
              - self._v_p[ i,j ] ) * self._dx )

        # initialize residual to be greater than `p_tol`
        res = 2 * self._p_tol

        # initialize counter for iterations of pressure solver
        i_p = 0

        while ( res > self._p_tol ):

          self.p, res = self.ADI(
            p = self.p,
            S = self._S )

          # increment counter
          i_p += 1

          # record value of residual at given outer and inner (pressure) step
          output_str = f'outer_iteration={t_idx:06d}    '\
            f'pressure_iteration={i_p:06d}    '\
            f'residual={res:.4e}\n'
          f.write( output_str )

          if np.any( np.isnan( self.p ) ):
            raise ValueError('solution to corrector step diverged')

          elif i_p == self._p_itrmax:
            raise ValueError( f'solution to corrector step has not converged' \
              'after {self._p_itrmax} iterations: has residual {res}')

        # 3. Apply correction
        #.....................................................................#

        self.u[ 1:N-1, 1:N-1 ] = self._u_p[ 1:N-1, 1:N-1 ] - self._dt / self._dx \
          * ( self.p[ 1:N-1, 1:N-1 ] - self.p[0:N-2, 1:N-1 ] )
        self.v[ 1:N-1, 1:N-1 ] = self._v_p[ 1:N-1, 1:N-1 ] - self._dt / self._dy \
          * ( self.p[ 1:N-1, 1:N-1 ] - self.p[1:N-1, 0:N-2 ] )

        # normalize pressure (only pressure differences matter, adding a constant
        # offset to all pressure values has no effect on the system's evolution.)
        self.p -= np.mean( self.p )

        error_u = np.linalg.norm( self.u - self._u_prev )
        error_v = np.linalg.norm( self.v - self._v_prev )

        print( t_idx, error_u, error_v )

        # check if simulation has converged
        if ( ( error_u < self._t_tol ) & ( error_v < self._t_tol ) & ( t_idx > 1 ) ):
          break

        # copy current primitive variables for use as `previous` values in next
        # iteration
        self._p_prev = self.p.copy( )
        self._u_prev = self.u.copy( )
        self._v_prev = self.v.copy( )

    # save final converged arrays of primitive variables.
    np.save( os.path.join( output_dir, 'u' ), self.u )
    np.save( os.path.join( output_dir, 'v' ), self.v )
    np.save( os.path.join( output_dir, 'p' ), self.p )

  #---------------------------------------------------------------------------#

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
