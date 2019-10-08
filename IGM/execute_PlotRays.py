from Plots import *


#PlotNearRays( measure='SM' )
PlotFarRays( measure='SM', plot_mean=True, uniform=True, save_mean=True )# False )
#PlotFarRays( measure='SM', mean=True, uniform=True, overestimate=True )

PlotFarRays( measure='DM', plot_mean=True, uniform=True, save_mean=True )# False )
#PlotFarRays( measure='DM', plot_mean=True, overestimate=True )

models = ['primordial', 'astrophysical', 'B9b', 'B9.5b', 'B10.0b', 'B10.5b', 'B11b', 'B13b', 'B15b', 'B17b' ][:4]
models=['primordial', 'astrophysical_mean', 'astrophysical_median', 'alpha1-3rd', 'alpha2-3rd', 'alpha3-3rd', 'alpha4-3rd', 'alpha5-3rd', 'alpha6-3rd', 'alpha7-3rd', 'alpha8-3rd', 'alpha9-3rd']  ## models to be considered for the magnetic field, provided as B~rho relations in relations_file

PlotFarRays( model=models[2], measure='RM', plot_mean=True, plot_stddev=False, save_mean=False, linestyle=":" )
PlotFarRays( model=models[1], measure='RM', plot_mean=True, plot_stddev=False, save_mean=False )
for model in models[3::]:
    PlotFarRays( model=model, measure='RM', plot_mean=True, plot_stddev=False, save_mean=False , linestyle='--')
#PlotFarRays( measure='RM', mean=True, overestimate=True )
PlotFarRays( model=models[0], measure='RM', plot_mean=True, plot_stddev=False, uniform=True, z_max=6, linestyle=':', save_mean=True )# False )
