# -*- coding: utf-8 -*-

#details how to set global SVN variables can be found in http://blogchuck.com/2009/09/adding-svn-headers-revisited/

"""
# Copyright (C) 2012-2013 Alexander Loew, alexander.loew@mpimet.mpg.de
# See COPYING file for copying and redistribution conditions.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
"""

__name__ = "pycmbs"
"""The project name."""

__author__ = "$Author: $"
"""The primary author of pyCMBS."""

__institute__="Max-Planck-Institute for Meteorology (MPI-M)"

__copyright__ = "Copyright (c) 2011-2013 Alexander Loew"
"""The copyright holder of pyCMBS."""

__license__ = "GNU General Public License"
"""The license governing the use and distribution of pyCMBS."""

__url__ = "https://code.zmaw.de/projects/pycmbs"
"""The URL for pyCMBS's homepage."""

__version__ = "0.1.5"
"""Version number of pyCMBS."""

__revision__ = filter(str.isdigit, "$Revision$")
"""SVN repository number, set SVN using svn propset (see here: http://stackoverflow.com/questions/1449935/getting-svn-revision-number-into-a-program-automatically)"""

__date__ = "2013-06-14"
"""The release date of this version of pyCMBS."""

__docformat__ = "epytext en"
"""The epydoc documentation format for this file."""

__email__ = "alexander.loew@mpimet.mpg.de"

#------------------------------
#--- Import classes
#------------------------------

#- generic classes
import matplotlib
matplotlib.use('Agg')   #this is the first level import of Matplotlib. activate or deactivate here if you want to change the backend used
# from matplotlib import pylab as pl
# from pycmbs import  netcdf 
# 
# from scipy import stats
# 
# import numpy as np
# 
# from mpl_toolkits.basemap import Basemap,shiftgrid
# 
# import os
# 
# import sys
# 
# import logging
# 
# #- classes specific to pyCMBS
# from pycmbs import statistic
# from data   import *
# from report import *
# from region import *
# from plots  import *
# from diagnostic import *
# from icon import *
# from grid import *
# from data4D import *
# 
# from taylor import *
# 
# from hov import *
# from region import *
# 
# from netcdftime import *
# 
# from colormaps.colormaps import *

#------------------------------
#--- Global constants
#------------------------------
EarthRadius = 6371000. #default radius of the earth in m


#~ logger = logging.getLogger('pyCMBS_logger')
#~ hdlr = logging.FileHandler('pyCMBS.log')
#~ formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#~ hdlr.setFormatter(formatter)
#~ logger.addHandler(hdlr)
#~ logger.setLevel(logging.WARNING) #logging.DEBUG
