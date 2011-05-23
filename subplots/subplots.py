import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as mpl

import aplpy

fig = mpl.figure(figsize=(14, 7))

f1 = aplpy.FITSFigure('data/2MASS_j.fits.gz', figure=fig,
                      subplot=[0.13, 0.1, 0.35, 0.7])

f1.tick_labels.set_font(size='x-small')
f1.axis_labels.set_font(size='small')
f1.show_grayscale()

f2 = aplpy.FITSFigure('data/2MASS_k.fits.gz', figure=fig,
                      subplot=[0.5, 0.1, 0.35, 0.7])

f2.tick_labels.set_font(size='x-small')
f2.axis_labels.set_font(size='small')
f2.show_grayscale()

f2.axis_labels.hide_y()
f2.tick_labels.hide_y()

fig.savefig('subplots.png', bbox_inches='tight')
