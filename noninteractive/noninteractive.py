# Change the matplotlib backend *before* importing APLpy
import matplotlib
matplotlib.use('Agg')

import aplpy

# Initialize figure, plot grayscale, and save as PNG
f = aplpy.FITSFigure('data/MSX_E.fits.gz')
f.show_grayscale()
f.save('noninteractive.png')
