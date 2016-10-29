#!/usr/bin/env python

# plot_location.py
#
# A script to plot pitches locations and their outcomes for a given pitcher from
# a given pitch f/x innings XML file
#
# Author: Michael Goldstein
# License: Apache 2.0

import matplotlib.pyplot as plot
import matplotlib.patches as patches
from bs4 import BeautifulSoup
import sys

# Check argument count, print format message if wrong
if (len(sys.argv) != 6):
    print "Incorrect argument format."
    print "    USAGE:   ./plot_location.py [DATA.xml] [OUT.png] [PITCHER ID] [PITCH TYPE] [PLOT TITLE]"
    print "    EX:      ./plot_location.py data/game.xml figs/figure.png 425794 SI 'Sinkers, 05/24'"
    sys.exit(-1)

in_file = sys.argv[1]
out_file = sys.argv[2]
pitcher = sys.argv[3]
ptype = sys.argv[4]

with open(in_file, 'r') as f:
    xml = f.read()
    f.close()

# grab pitches for the provided pitcher from the XML
soup = BeautifulSoup(xml, 'lxml')
atbats = soup.find_all('atbat')
pitches = []
for ab in atbats:
    if ab['pitcher'] == pitcher:# and ab['stand'] == handed:
        for c in ab.children:
            if (c.name == 'pitch'):
                pitches.append(c)

# parse out the pitches
n = 0
# pgood = good outcome
pgood = []
pgood.append([])
pgood.append([])
# pbad = bad outcome
pbad = []
pbad.append([])
pbad.append([])
# pball = ball
pball = []
pball.append([])
pball.append([])
# strike zone boundaries
sztop = 0.0
szbot = 0.0
szr = 8.5/12.0
szl = -szr

for pitch in pitches:
    if (pitch['pitch_type'] == ptype):
        if (pitch['type'] == 'S'):
            pgood[0].append(pitch['px'])
            pgood[1].append(pitch['pz'])
        if (pitch['type'] == 'B'):
            pball[0].append(pitch['px'])
            pball[1].append(pitch['pz'])
        if (pitch['type'] == 'X'):
            if (pitch['des'] == 'In play, out(s)'):
                pgood[0].append(pitch['px'])
                pgood[1].append(pitch['pz'])
            else:
                pbad[0].append(pitch['px'])
                pbad[1].append(pitch['pz'])
        sztop += float(pitch['sz_top'])
        szbot += float(pitch['sz_bot'])
        n += 1

# compute average strike zone
sztop /= n
szbot /= n

red_p = patches.Patch(color='red', label='Good Outcome')
blk_p = patches.Patch(color='black', label='Bad Outcome')
blu_p = patches.Patch(color='blue', label='Ball')

plot.title(sys.argv[5])
plot.legend(handles=[red_p, blk_p, blu_p])
plot.xlabel('horizontal location (ft)')
plot.ylabel('vertical location (ft)')
plot.axis([-3, 3, 0, 6])
plot.grid(True)
plot.plot([szl, szr], [szbot, szbot], 'b')
plot.plot([szl, szl], [szbot, sztop], 'b')
plot.plot([szr, szr], [szbot, sztop], 'b')
plot.plot([szl, szr], [sztop, sztop], 'b')
plot.plot(pball[0], pball[1], 'bo')
plot.plot(pgood[0], pgood[1], 'ro')
plot.plot(pbad[0], pbad[1], 'ko')
plot.savefig(out_file)
