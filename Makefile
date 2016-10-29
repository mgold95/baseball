PLOT = ./plot_location.py

location : good bad

good :
	$(PLOT) data/good.xml figs/good_ff_loc.png 425794 FF 'Wainwright Fastball Locations, 7/16/16'
	$(PLOT) data/good.xml figs/good_cu_loc.png 425794 CU 'Wainwright Curveball Locations, 7/16/16'
	$(PLOT) data/good.xml figs/good_fc_loc.png 425794 FC 'Wainwright Cutter Locations, 7/16/16'
	$(PLOT) data/good.xml figs/good_si_loc.png 425794 SI 'Wainwright Sinker Locations, 7/16/16'

bad :
	$(PLOT) data/bad.xml figs/bad_ff_loc.png 425794 FF 'Wainwright Fastball Locations, 5/12/16'
	$(PLOT) data/bad.xml figs/bad_cu_loc.png 425794 CU 'Wainwright Curveball Locations, 5/12/16'
	$(PLOT) data/bad.xml figs/bad_fc_loc.png 425794 FC 'Wainwright Cutter Locations, 5/12/16'
	$(PLOT) data/bad.xml figs/bad_si_loc.png 425794 SI 'Wainwright Sinker Locations, 5/12/16'

clean :
	rm figs/*.png
