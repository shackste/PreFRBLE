#import os
#from glob import glob
#from Models import *
#from Parameters import *
from Rays import *
#from multiprocessing import Pool
from time import time

t0 = time()

CreateLoSsDMRM( models=['primordial', 'astrophysical'] )

print 'took %.0f seconds' % ( time() - t0 )
