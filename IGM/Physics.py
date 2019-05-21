'''
Physical quantities and functions

'''


import yt
from yt.utilities.cosmology import Cosmology
from yt.units import speed_of_light_cgs as speed_of_light

## units of physical quantities
units = {
    'DM'       :r"pc cm$^{-3}$",
    'RM'       :r"rad m$^{-2}$",
    'SM'       :r"kpc m$^{-20/3}",
}


## exponent of cosmic scale factor
comoving_exponent = {
    'Density'  : -3,
    'density'  : -3,
    'Bx'       : -2,
    'By'       : -2,
    'Bz'       : -2,
    'B_LoS'    : -2,
    'dl'       : 1,
    'x'        : 1,
    'y'        : 1,
    'z'        : 1,
    'dx'       : 1,
    'dy'       : 1,
    'dz'       : 1,
    'redshift' : 0
}


## conversion factors
Mpc2cm = yt.units.Mpc.in_cgs().value*1 ## *1 to get value instead of 0D-array
kpc2cm = yt.units.kpc.in_cgs().value*1 
h=0.71
Mpch2cm = Mpc2cm/h
kpch2cm = kpc2cm/h

## physical constants
OmegaBaryon       = 0.04
OmegaCDM          = 0.23
OmegaMatter       = 0.27
OmegaLambda       = 0.73
OmegaCurvature    = 0.0

critical_density = 9.47e-30 # g/cm**3
electron_mass = 9.11e-28  # g
proton_electron_mass_ratio = 1836.
proton_mass = 1.67e-24 # g


## cosmic functions
co = Cosmology( hubble_constant=h, omega_matter=OmegaMatter, omega_lambda=OmegaLambda, omega_curvature=OmegaCurvature )

comoving_radial_distance = co.comoving_radial_distance  ## distance z0 to z1

## redshift <-> time
z_from_t = co.z_from_t
t_from_z = co.t_from_z

