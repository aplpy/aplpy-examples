# Change the matplotlib backend *before* importing APLpy
import matplotlib
matplotlib.use('Agg')

import aplpy

# Plain RA/Dec plot
f = aplpy.FITSFigure('data.fits.gz', dimensions=[0, 1], slices=[225])
f.show_grayscale()
f.add_grid()
f.save('ra_dec.png')

# Swap RA and Dec
f = aplpy.FITSFigure('data.fits.gz', dimensions=[1, 0], slices=[225])
f.show_grayscale()
f.add_grid()
f.save('dec_ra.png')

# Velocity/RA plot
f = aplpy.FITSFigure('data.fits.gz', dimensions=[2, 0], slices=[100])
f.show_grayscale()
f.add_grid()
f.save('vel_ra.png')

# Velocity/Declination plot
f = aplpy.FITSFigure('data.fits.gz', dimensions=[2, 1], slices=[100])
f.show_grayscale()
f.add_grid()
f.save('vel_dec.png')

# The following examples show how to allow pixel 'stretching' so that the 
# image fills the defined axes.

# Velocity/RA plot
f = aplpy.FITSFigure('data.fits.gz', dimensions=[2, 0], slices=[100])
f.show_grayscale(aspect='auto')
f.show_colorscale(aspect='auto')
f.add_grid()
f.save('vel_ra_auto.png')

# Velocity/Declination plot
f = aplpy.FITSFigure('data.fits.gz', dimensions=[2, 1], slices=[100])
f.show_grayscale(aspect='auto')
f.add_grid()
f.save('vel_dec_auto.png')