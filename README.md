# baseball

This repository is a collection of tools for analyzing MLB Advanced Media's
published XML data for MLB games.

All content is licensed under the Apache 2.0 License.

## Files:

  * `plot_locations.py`
    + plots a pitcher's pitch locations
  * `pitch_stats.py`
    + calculates a number of statistics about a given pitcher's pitches
  * `Makefile`
    + A set of commands to produce the output plots and stats for my article _A Tale of Two Wainos_
  * `/data/`
    + Directory of XML pitch data from MLB Gameday
  * `/figs/`
    + Directory of plots output by `plot_locations.py` according to rules in Makefile
  * `/stats/`
    + Directory of text files output by `pitch_stats.py` according to rules in Makefile
