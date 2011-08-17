import aplpy
import pylab

modelpath = '/Users/adam/work/h2co/radex/grid_sep2010/'
modelname = '1-1_2-2_T=5to55_lvg_1000square_largerange'
for prop in ('tex1','tex2','tline1','tline2'):
    pylab.figure(1)
    pylab.clf()
    modelpath = '/Users/adam/work/h2co/radex/grid_greenscaled/'
    modelname = '1-1_2-2_T5to55_lvg_greenscaled'
    FF1 = aplpy.FITSFigure(modelpath+modelname+"_"+prop+".fits",slices=[4],userwcs=True,figure=pylab.figure(1))
    if 'tex' in prop:
        FF1.show_grayscale(vmin=0,vmax=20)
        levels=[1,2.73,5,10,15]
    elif 'tline' in prop:
        FF1.show_grayscale(vmin=-2,vmax=20)
        levels=[-2,-1,0,1,2]
    FF1.show_contour(modelpath+modelname+"_"+prop+".fits",slices=[4],levels=levels,userwcs=True,colors='r')
    modelpath = '/Users/adam/work/h2co/radex/grid_aug2010/'
    modelname = '1-1_2-2_T=5to55_morepoints_lvg'
    FF1.show_contour(modelpath+modelname+"_"+prop+".fits",slices=[4],levels=levels,userwcs=True,colors='b')
    FF1.recenter(4.,13.,width=6,height=4.001)
    FF1.axis_labels.set_xtext("Log(n(H$_2$)) (cm$^{-3}$)")
    FF1.axis_labels.set_ytext("Log(N(o-H$_2$CO)) (cm$^{-2}$)")
    FF1.tick_labels.set_xformat("d.dd")
    FF1.tick_labels.set_yformat("dd.d")

    FF1._layers['contour_set_1'].clabel()
    FF1._layers['contour_set_2'].clabel()

    pylab.draw()
    #pylab.show()
    FF1.save('/Users/adam/work/h2co/pilot/figures/models/radex_grid_greenscaled_compare_%s.png' % prop)
