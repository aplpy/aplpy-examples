import glob
import os

# Use non-interactive mode, otherwise a new window will pop up for each figure
import matplotlib
matplotlib.use('Agg')

# Import APLpy after setting non-interactive mode
import aplpy

# Loop over all FITS files in data/ directory
for filename in glob.glob(os.path.join('data/', '*.fits.gz')):

    # Open file and show grayscale
    f = aplpy.FITSFigure(filename)
    f.show_grayscale()

    # Save in the current directory, with a filename similar to the input
    # filename
    f.save(os.path.basename(filename).replace('fits.gz', 'png'))

    # Free up memory - without this, matplotlib uses more and more memory as
    # it keeps track of all figures that have been made
    f.close()
