import aplpy

# Reproject all images to same projection (requires Montage and
# python-montage)
aplpy.make_rgb_cube(['data/2MASS_k.fits.gz',
                     'data/2MASS_h.fits.gz',
                     'data/2MASS_j.fits.gz'],
                     '2MASS_cube.fits')

# Make an RGB image with embedded AVM metadata containing the WCS information
# (requires PyAVM). This function takes many arguments to control levels and
# stretch functions. See the full documentation for more details
aplpy.make_rgb_image('2MASS_cube.fits', '2MASS_rgb.png', embed_avm_tags=True)

# Make the plot using the RGB image directly
f = aplpy.FITSFigure('2MASS_rgb.png')
f.show_rgb()
f.save('make_rgb.png')
