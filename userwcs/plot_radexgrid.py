"""
To acquire the userwcs package, you need to check out the topic/userwcs branch:
    git clone git@github.com:aplpy/aplpy.git 
    cd aplpy
    git branch --track topic/userwcs remotes/origin/topic/userwcs
    git checkout topic/userwcs

When you type "git branch" or "git status", it should tell you that you are using the topic/userwcs branch
"""
import aplpy

FF1 = aplpy.FITSFigure("data/1-1_2-2_T=5to55_lvg_1000square_largerange_tex1_20K_small.fits",userwcs=True)
FF1.show_grayscale(vmin=0,vmax=20)

levels=[-1,-0.5,0,1]
FF1.show_contour("data/1-1_2-2_T=5to55_lvg_1000square_largerange_tline1_20K_small.fits",levels=levels,userwcs=True,colors='r')
FF1.axis_labels.set_xtext("Log(n(H$_2$)) (cm$^{-3}$)")
FF1.axis_labels.set_ytext("Log(N(o-H$_2$CO)) (cm$^{-2}$)")
FF1.tick_labels.set_xformat("d.dd")
FF1.tick_labels.set_yformat("dd.d")

FF1._layers['contour_set_1'].clabel()
FF1.refresh()

