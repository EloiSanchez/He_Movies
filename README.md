# He_Movies
## Description
Program that uses the results of the calculations performed by the relaxation dynamics program of our group, although it will work for the rest of the programs as well. It reads the helium density files printed in format den.xx.xxxxxxx.dat or tall.x.xxxxxxxx.dat to produce a movie of the dynamic evolution of the x, y and z axis of the helium density.

The results are saved in .mp4 format and may be of significant size if the simulations are long.

## Requirements
- Matplotlib
- ffmpeg installed
- Numpy
- os

## Usage
All relevant variables for the plotting must be edited in the ``control.py`` file. This includes the path of the input files, the output name and which graphs are going to be plotted (which axis are going to be used).

The choice of reading den.xx.xxxxxxx.dat or tall.x.xxxxxxxx.dat file formats is given by the user in the input using the variable `is_den = True` for the former and `is_den = False` for the latter.

The results will be automatically saved in ./Resultats/, if the file already exists, it will ask to know if it should be replaced or it should exit the program. While waiting for input, you can manually change the name of the existing file to another one and try again returning any string that is not 'Q' or 'R'.

To execute, use ``python3 main.py``.

## Author and Contact

Author: Eloi Sanchez Ambros.

Contact: esancham21@alumnes.ub.edu or eloisanchez16@gmail.com

## Other Programs for the Group
- [Grid Construction](https://github.com/EloiSanchez/Grid_Construction): To generate helium nanodroplet grids of any size and density
- [FFT analysis](https://github.com/EloiSanchez/FFT_pob): To perform Fourier analysis of the results of the dynamic simulations of the group.

