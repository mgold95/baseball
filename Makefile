PLOT = ./plot_location.py
STATS = ./pitch_stats.py

all : plots stats

plots : plot_good plot_bad

plot_good : plot_perm
	$(PLOT) data/good.xml figs/good_ff_loc.png 425794 FF 'Wainwright Fastball Locations, 7/16/16'
	$(PLOT) data/good.xml figs/good_cu_loc.png 425794 CU 'Wainwright Curveball Locations, 7/16/16'
	$(PLOT) data/good.xml figs/good_fc_loc.png 425794 FC 'Wainwright Cutter Locations, 7/16/16'
	$(PLOT) data/good.xml figs/good_si_loc.png 425794 SI 'Wainwright Sinker Locations, 7/16/16'

plot_bad : plot_perm
	$(PLOT) data/bad.xml figs/bad_ff_loc.png 425794 FF 'Wainwright Fastball Locations, 5/12/16'
	$(PLOT) data/bad.xml figs/bad_cu_loc.png 425794 CU 'Wainwright Curveball Locations, 5/12/16'
	$(PLOT) data/bad.xml figs/bad_fc_loc.png 425794 FC 'Wainwright Cutter Locations, 5/12/16'
	$(PLOT) data/bad.xml figs/bad_si_loc.png 425794 SI 'Wainwright Sinker Locations, 5/12/16'

plot_perm :
	chmod +x $(PLOT)

stats : stat_good stat_bad

stat_good : stats_perm
	$(STATS) data/good.xml stats/good.txt 425794 'Wainwright Pitch Statistics, 7/16/16'

stat_bad : stats_perm
	$(STATS) data/bad.xml stats/bad.txt 425794 'Wainwright Pitch Statistics, 5/12/16'

stats_perm :
	chmod +x $(STATS)

clean :
	rm figs/*.png stats/*.txt
