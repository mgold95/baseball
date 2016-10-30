#!/usr/bin/env python

# pitch_stats.py
#
# A script to output some statistics for a pitcher's pitches
#
# Author: Michael Goldstein
# License: Apache 2.0

from bs4 import BeautifulSoup
from collections import defaultdict
import numpy as np
import sys

# change to zero or edit the filter for a non-waino pitcher
WAINO_FILTER = 1

if (len(sys.argv) != 5):
    print "ERR"
    sys.exit(-1)

in_file = sys.argv[1]
out_file = sys.argv[2]
pitcher = sys.argv[3]
title = sys.argv[4]

with open(in_file, 'r') as f:
    xml = f.read()
    f.close()

# grab pitches for the provided pitcher from the XML
soup = BeautifulSoup(xml, 'lxml')
atbats = soup.find_all('atbat')
pitches = []
for ab in atbats:
    if ab['pitcher'] == pitcher:
        for c in ab.children:
            if (c.name == 'pitch'):
                pitches.append(c)

n = 0
ptypes = []
speeds = defaultdict(list)
break_lens = defaultdict(list)
break_angs = defaultdict(list)
nums = dict()

for pitch in pitches:
    n += 1
    speed = float(pitch['start_speed'])
    brk_len = float(pitch['break_length'])
    brk_ang = float(pitch['break_angle'])
    conf = float(pitch['type_confidence'])
    ptype = pitch['pitch_type']
# turns out pitchf/x sometimes does a terrible job at predicting
# which type of pitch waino throws so this corrects for it
    if (WAINO_FILTER == 1 and conf < 0.9):
        if (speed < 89.0 and speed > 78.0 and brk_ang < 0):
            ptype = "FC"
        elif (speed < 76.0):
            ptype = "CU"
        elif (speed > 88.0 and brk_ang > 29 and ptype != "FF"):
            ptype = "SI" 
        elif (speed > 88.0 and brk_ang > 0 and ptype != "SI"):
            ptype = "FF"
        elif (ptype == "FC" and brk_ang > 0):
            if (brk_ang < 20 and ptype != "SI"):
                ptype = "FF"
            elif (ptype != "FF"):
                ptype = "SI"    
    speeds[ptype].append(speed)
    break_lens[ptype].append(brk_len)
    break_angs[ptype].append(brk_ang)
    if (nums.has_key(ptype)):
        nums[ptype] += 1
    else:
        ptypes.append(ptype)
        nums[ptype] = 1

# write with spaces for nicely formatted output
def wws(f, s):
    l = len(s)
    f.write("|%s%*c|\n" % (s, 48-l, ' '))

pitch_names = {
    "FA" : "Fastball",
    "FF" : "Four-seam Fastball",
    "FT" : "Two-seam Fastball",
    "FC" : "Cutter",
    "FS" : "Sinker",
    "SI" : "Sinker",
    "SF" : "Splitter",
    "SL" : "Slider",
    "CH" : "Changeup",
    "CB" : "Curveball",
    "CU" : "Curveball",
    "KC" : "Knuckle Curve",
    "KN" : "Knuckleball",
    "EP" : "Eephus",
    "PO" : "Pitchout"
}

ptypes.sort()
with open(out_file, 'w') as f:
    f.write("%s\n\n\n" % title)
    for ptype in ptypes:
        name = pitch_names[ptype]
        f.write("__________________________________________________\n")
        wws(f, " " + name)
        f.write("|------------------------------------------------|\n")
        wws(f, " %d thrown, %f%% of all pitches" % (nums[ptype], nums[ptype]*100.0/n))
        wws(f, " Velocity:")
        wws(f, "     Mean:         %f" % np.mean(speeds[ptype]))
        wws(f, "     Std. Dev:     %f" % np.std(speeds[ptype]))
        wws(f, " Break Length:")
        wws(f, "     Mean:         %f" % np.mean(break_lens[ptype]))
        wws(f, "     Std. Dev:     %f" % np.std(break_lens[ptype]))
        wws(f, " Break Angle:")
        wws(f, "     Mean:         %f" % np.mean(break_angs[ptype]))
        wws(f, "     Std. Dev:     %f" % np.std(break_angs[ptype]))
        f.write("|________________________________________________|\n\n")
    f.close()
