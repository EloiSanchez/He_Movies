from os import listdir
from os.path import exists
import matplotlib.pyplot as plt
from matplotlib import RcParams as rc
from matplotlib.animation import FuncAnimation
import matplotlib.animation as ani
import control as ct
import numpy as np
import get_den as gd
import sys

"""
Movies for the helium density and derivatives.

To do:
    - Add commandline input to get the interval plot t0 and tf
    - Add plots for enregy and norm from energy.dat and norma_He.dat

Eloi Sanchez
2021
"""


# Function to generate each frame
def animate(t):
    """
    Plots each of the animation depending on t
    """
    # This block controls the plot of the density
    if ct.is_dens:
        ax1.clear()

        # Y axis of the plot
        ax1.set_ylim(ct.yrang_dens[0], ct.yrang_dens[1])
        ax1.set_ylabel(ct.y_title_dens, weight=ct.t_bold, stretch="condensed",
                    fontsize=ct.ax_font_size)
        # X axis of the plot
        ax1.set_xlim(ct.xrang[0], ct.xrang[1])
        if not ct.is_deriv:
            ax1.set_xlabel(ct.x_title, weight=ct.t_bold, stretch="condensed",
                        fontsize=ct.ax_font_size)

        # for tick in ax1.get_xticklabels():
        #     tick.set_fontname("Arial")
        # for tick in ax1.get_yticklabels():
        #     tick.set_fontname("Arial")


        # Plot
        if ct.is_x:
            ax1.plot(tall_x, all_x[t], label="x axis", c="#8ece27", lw=ct.lineweight)
        if ct.is_y:
            ax1.plot(tall_y, all_y[t], label="y axis", c="#1982c4", lw=ct.lineweight)
        if ct.is_z:
            ax1.plot(tall_z, all_z[t], label="z axis", c="#ff333a", lw=ct.lineweight)

        # Title, legend and timestamp
        ax1.set_title("{}".format(ct.graph_title), weight=ct.t_bold, fontsize=ct.tit_font_size,
            stretch="condensed")
        ax1.legend(frameon=False)
        ax1.text(ct.pos_t[0], ct.pos_t[1], "{} ps".format(t), c="grey")


def log(s):
    """
    Format prints.
    """
    print("\n====" + "="*len(s) + "====")
    print("=== " + s + " ===")
    print("====" + "="*len(s) + "====\n")
    return


log("Starting calculation")

# Some standards for plotting
rc.update(
    {'font.size' : ct.font_size},
    {'family' : "Arial"},
    )

# Generate standard lists
tall_x = []
all_x = []
all_x_deriv = []
tall_y = []
all_y = []
all_y_deriv = []
tall_z = []
all_z = []
all_z_deriv = []

# Get the filenames to be read from the directory.
# The files must be parsed to get only the XY and XZ files.
directory_files = listdir(ct.folder_name)
all_files = []

if ct.is_den:
    for fil in directory_files:
        if fil.startswith('den.XY.') or fil.startswith('den.XZ.'):
            all_files.append(fil)
else:
     for fil in directory_files:
         if fil.startswith('tall.x.') or fil.startswith('tall.y.') or fil.startswith('tall.z'):
             all_files.append(fil)
all_files.sort()
maxfile = all_files[-1]
maxnum = int(maxfile[-11:-4])

# Get some variables from DFT4He3dt.namelist.read
with open(ct.folder_name + "/DFT4He3dt.namelist.read", "r") as fil:
    lines = fil.readlines()

for line in lines:
    if line.strip().startswith("DELTAT"):
        delta_t = float(line.split("=")[1][:-2])
    elif line.strip().startswith("PTALLS"):
        ptalls = int(line.split("=")[1][:-2])
    elif line.strip().startswith("PDENPAR"):
        pdenpar = int(line.split("=")[1][:-2])

print('Parameters read from namelist file.')
print(f'{delta_t = }')
print(f'{ptalls = }')
print(f'{pdenpar = }')
log("Reading files")
t, grid_x, all_x, all_y, all_z = gd.get_den(ct.folder_name, maxnum, delta_t, pdenpar, ptalls, ct.is_den)
print(f'{t = }')
print(f'{grid_x = }')
print(f'{all_x = }')
print(f'{all_y = }')
print(f'{all_z = }')
quit()
if ct.showmovie or ct.savemovie:
    log("Start animation")
    inter = int(1000/ct.fps)

    fig = plt.figure()
    ax1 = fig.add_subplot()

    # This is the function that creates the animation
    animation = FuncAnimation(fig=fig, func=animate, frames=maxnum, interval=inter)

    # Block for saving the movie in the output file
    if ct.savemovie:
        log("Saving animation")
        Writer = ani.writers['ffmpeg']
        writer = Writer(fps=ct.fps, bitrate=ct.bit_rate)
        out = ct.fileout + "_"
        if ct.is_x:
            out += "X"
        if ct.is_y:
            out += "Y"
        if ct.is_z:
            out += "Z"
        ani_name = "Resultats/movie_" + out + ".mp4"
        while exists(ani_name):
            order = input("The file {} already exists. Replace, Quit or Try again? (R/Q) ".format(ani_name))
            if order.capitalize().strip() == "Q":
                print("Exit program\n")
                quit()
            elif order.capitalize().strip() == "R":
                print("Replacing file\n")
                break
            print("Trying again\n")
            
        animation.save(ani_name, writer=writer, dpi=ct.res)

    # Block for showing the animation if it has not been saved
    if ct.showmovie and not ct.savemovie:
        log("Showing animation")
        plt.show()

log("END")
