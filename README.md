# He_Movies
## Description
Movies for the helium density.

## Requirements
- Matplotlib
- ffmpeg installed
- Numpy

## Usage
All relevant variables for the plotting must be edited in the ``control.py`` file. This includes the path of the input files, the output name and which graphs are going to be plotted (density, derivative or both).

The results will be automatically saved in ./Resultats/, if the file already exists, it will ask to know if it should be replaced or it should exit the program. While waiting for input, you can manually change the name of the existing file to another one and try again returning any string that is not 'Q' or 'R'.

To execute, use ``python3 main.py``.
