"""
To acquire the userwcs package, you need to check out the topic/userwcs branch:
    git clone git@github.com:aplpy/aplpy.git 
    cd aplpy
    git branch --track topic/userwcs remotes/origin/topic/userwcs
    git checkout topic/userwcs

When you type "git branch" or "git status", it should tell you that you are using the topic/userwcs branch
"""
import aplpy

# Create a FITSFigure instance using USERWCS and display it
# The filename is descriptive: This is a RADEX LVG model grid of the H2CO 1_11-1_10 and 2_12-2_11 transitions
# The first thing we're plotting is Excitation Temperature, which varies from ~1K to 20K.  Tex<Tcmb means the 
# line is seen in absorption against the CMB
FF1 = aplpy.FITSFigure("data/1-1_2-2_T=5to55_lvg_1000square_largerange_tex1_20K_small.fits",userwcs=True)
FF1.show_grayscale(vmin=0,vmax=20)

# overplot contours of the observable tline
levels=[-1,-0.5,0,1]
FF1.show_contour("data/1-1_2-2_T=5to55_lvg_1000square_largerange_tline1_20K_small.fits",levels=levels,userwcs=True,colors='r')
# Replace the axis labels with more descriptive versions
FF1.axis_labels.set_xtext("Log(n(H$_2$)) (cm$^{-3}$)")
FF1.axis_labels.set_ytext("Log(N(o-H$_2$CO)) (cm$^{-2}$)")
FF1.tick_labels.set_xformat("d.dd")
FF1.tick_labels.set_yformat("dd.d")

# Use the matplotlib builtin contour labels to label the contour levels
FF1._layers['contour_set_1'].clabel()
# since the matplotlib builtin doesn't call the aplpy refresh, do it manually
FF1.refresh()

