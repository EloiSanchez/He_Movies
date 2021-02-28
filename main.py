from os import listdir
import matplotlib.pyplot as plt
from matplotlib import RcParams as rc
from matplotlib.animation import FuncAnimation
import matplotlib.animation as ani
import control as ct
import numpy as np


# Generate filenames to read
def get_string(jk, j):
    str1 = "den.{}.0.".format(jk)
    num = "0"*(7-len(str(j))) + str(j)
    return str1 + num + ".dat"


# Function to generate each frame
def animate(t):
    if ct.is_dens:
        ax1.clear()

        ax1.set_ylim(ct.yrang_dens[0], ct.yrang_dens[1])
        ax1.set_ylabel(ct.y_title_dens, weight=ct.t_bold, stretch="condensed",
                    fontsize=ct.ax_font_size)
        ax1.set_xlim(ct.xrang[0], ct.xrang[1])
        if not ct.is_deriv:
            ax1.set_xlabel(ct.x_title, weight=ct.t_bold, stretch="condensed",
                        fontsize=ct.ax_font_size)

        # for tick in ax1.get_xticklabels():
        #     tick.set_fontname("Arial")
        # for tick in ax1.get_yticklabels():
        #     tick.set_fontname("Arial")

        ax1.set_title("{}".format(ct.graph_title), weight=ct.t_bold, fontsize=ct.tit_font_size,
            stretch="condensed")
        ax1.text(ct.pos_t[0], ct.pos_t[1], "{} ps".format(t), c="grey")

        if ct.is_x:
            ax1.plot(tall_x, all_x[t], label="x axis", c="#8ece27", lw=ct.lineweight)
        if ct.is_y:
            ax1.plot(tall_y, all_y[t], label="y axis", c="#1982c4", lw=ct.lineweight)
        if ct.is_z:
            ax1.plot(tall_z, all_z[t], label="z axis", c="#ff333a", lw=ct.lineweight)

        ax1.legend(frameon=False)

    if ct.is_deriv:
        ax2.clear()

        ax2.set_ylim(ct.yrang_deriv[0], ct.yrang_deriv[1])
        ax2.set_ylabel(ct.y_title_deriv, weight=ct.t_bold, stretch="condensed",
                        fontsize=ct.ax_font_size)

        ax2.set_xlim(ct.xrang[0], ct.xrang[1])
        ax2.set_xlabel(ct.x_title, weight=ct.t_bold, stretch="condensed",
                        fontsize=ct.ax_font_size)
        
        if ct.is_x:
            ax2.plot(tall_x, all_x_deriv[t], label="x axis", c="#8ece27", lw=ct.lineweight)
        if ct.is_y:
            ax2.plot(tall_y, all_y_deriv[t], label="y axis", c="#1982c4", lw=ct.lineweight)
        if ct.is_z:
            ax2.plot(tall_z, all_z_deriv[t], label="z axis", c="#ff333a", lw=ct.lineweight)

        if not ct.is_dens:
            ax2.legend(frameon=False)
            ax2.set_title("{}".format(ct.graph_title), weight=ct.t_bold, fontsize=ct.tit_font_size,
                stretch="condensed")

    # plt.tight_layout()


# Makes derivative of a list
def derivate(lst, h):
    N = len(lst)
    n_lst = lst.copy()
    dv_ll = np.zeros(N)
    n_lst.append(0)
    n_lst.insert(0, 0)
    ll = np.array(n_lst)
    for i in range(0, N):
        dv_ll[i] = ll[i+2] - ll[i]
    dv_ll = dv_ll / (2 * h)
    return dv_ll.tolist()


def log(s):
    print("====" + "="*len(s) + "====")
    print("=== " + s + " ===")
    print("====" + "="*len(s) + "====\n")
    return


log("Starting calculation")

# Some standards for plotting
rc.update(
    {'font.size' : ct.font_size},
    {'family' : "Arial"},
    )

tall_x = []
all_x = []
all_x_deriv = []
tall_y = []
all_y = []
all_y_deriv = []
tall_z = []
all_z = []
all_z_deriv = []

all_files = listdir(ct.folder_name)
all_files.sort()
maxfile = all_files[-1]
maxnum = int(maxfile[-11:-4])

log("Reading files")
for i in range(1, maxnum+1):
    f = ct.folder_name + "/" + get_string("XY", i)
    f = open(f, mode="r")
    den_y = []
    den_x = []
    for line in f:
        x, y, den = line.split()
        x = float(x)
        y = float(y)
        den = float(den)

        if abs(x) < 0.001:
            den_y.append(den)
            if y not in tall_y:
                tall_y.append(y)

        if abs(y) < 0.001:
            den_x.append(den)
            if x not in tall_x:
                tall_x.append(x)
    
    all_y.append(den_y)
    all_x.append(den_x)
    if ct.is_deriv:
        all_y_deriv.append(derivate(den_y, tall_y[1]-tall_y[0]))
        all_x_deriv.append(derivate(den_x, tall_x[1]-tall_x[0]))
    f.close()

for i in range(1, maxnum+1):
    f = ct.folder_name + "/" + get_string("XZ", i)
    f = open(f, mode="r")
    den_z = []
    for line in f:
        x, z, den = line.split()
        x = float(x)
        z = float(z)
        den = float(den)

        if abs(x) < 0.001:
            den_z.append(den)
            if z not in tall_z:
                tall_z.append(z)

    all_z.append(den_z)
    if ct.is_deriv:
        all_z_deriv.append(derivate(den_z, tall_z[1]-tall_z[0]))
    f.close()

if ct.showmovie or ct.savemovie:
    log("Start animation")
    inter = int(1000/ct.fps)

    fig = plt.figure()
    if ct.is_together:
        if not (ct.is_dens and ct.is_deriv):
            log("Error: for double plot, all shoud be True.")
            quit()
        plt.close()
        fig = plt.figure(figsize=(6.4, 4.8*1.5))
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)
        pre = "all_"
    elif ct.is_dens and not ct.is_deriv:
        ax1 = fig.add_subplot()
        pre = "dens_"
    elif ct.is_deriv and not ct.is_dens:
        ax2 = fig.add_subplot()
        pre = "deriv_"
    else:
        log("Error: For double indpendent plot, run twice.")
        quit()

    animation = FuncAnimation(fig=fig, func=animate, frames=maxnum, interval=inter)

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
        animation.save("Resultats/" + pre + out + ".mp4", writer=writer, dpi=ct.res)

    if ct.showmovie:
        log("Showing animation")
        plt.show()

log("END")
