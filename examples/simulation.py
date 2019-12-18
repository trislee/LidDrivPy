# -*- coding: UTF-8 -*-

"""Execute a simulation of the lid-driven cavity
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

from liddrivpy.base import System, Solver, Simulation

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

N_cells = 32
Re = 10
U_lid = 1
L_lid = 1

dt = 0.00125
omega = 1.1
t_itrmax = 100000
p_itrmax = 5000
t_tol = 1e-16
p_tol = 1e-4

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

system = System(
  N_cells = N_cells,
  Re = Re,
  U_lid = 1,
  L_lid = 1 )

solver = Solver(
  dt = dt,
  omega = omega,
  t_itrmax = t_itrmax,
  t_tol = t_tol,
  p_itrmax = p_itrmax,
  p_tol = p_tol )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

simulation = Simulation(
  system = system,
  solver = solver )

simulation.execute( output_dir = 'output' )

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#