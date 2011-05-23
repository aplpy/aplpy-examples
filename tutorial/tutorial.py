import numpy as np
import aplpy

# Initialize an instance of FITSFigure. This should open up an interactive
# window with an empty set of axes.
f = aplpy.FITSFigure('data/2MASS_k.fits.gz')

# Show a grayscale of the file
f.show_grayscale()

# It is also possible to show an RGB image sampled to the same pixel
# resolution
f.show_rgb('data/2MASS_rgb.png')

# Modifiy the appearance of the ticks
f.tick_labels.set_font(size='small')

# Overlay a set of contours
f.show_contour('data/MSX_E.fits.gz', colors='white')

# Overlay a set of sources
data = np.loadtxt('data/sources.txt')
ra, dec = data[:, 0], data[:, 1]
f.show_markers(ra, dec, layer='marker_set_1', edgecolor='red', \
               facecolor='none', marker='o', s=10, alpha=0.5)

# Save to a PNG file
f.save('tutorial.png')
