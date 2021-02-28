from os import listdir
import matplotlib.pyplot as plt
from matplotlib import RcParams as rc
from matplotlib.animation import FuncAnimation
import matplotlib.animation as ani
import control as ct


# Generate filenames to read
def get_string(jk, j):
    str1 = "den.{}.0.".format(jk)
    num = "0"*(7-len(str(j))) + str(j)
    return str1 + num + ".dat"

# Function to generate each frame
def animate(t):
    ax.clear()

    ax.set_ylim(0, 0.04)
    ax.set_ylabel(r'Helium denisty ($\AA^{\mathbf{-3}}$)', fontname="Arial", weight="bold", stretch="condensed",
                  fontsize="12")
    ax.set_xlim(-20, 20)
    ax.set_xlabel(r"Axis ($\rm{\AA}$)", fontname="Arial", weight="bold", stretch="condensed",
                  fontsize="12")

    for tick in ax.get_xticklabels():
        tick.set_fontname("Arial")
    for tick in ax.get_yticklabels():
        tick.set_fontname("Arial")

    ax.set_title("{}".format(ct.graph_title), fontname="Arial", weight="bold")
    ax.text(-19.5, 0.038, "{} ps".format(t), c="grey", fontname="Arial")

    if ct.is_x:
        ax.plot(tall_x, all_x[t], label="x axis", c="#345AD5", lw="1.5")
    if ct.is_y:
        ax.plot(tall_y, all_y[t], label="y axis", c="#D44535", lw="1")
    if ct.is_z:
        ax.plot(tall_z, all_z[t], label="z axis", c="#70AE5B", lw="1")

    ax.legend(frameon=False, prop={"family":"Arial", "size":"11"})

def log(s):
    print("====" + "="*len(s) + "====")
    print("=== " + s + " ===")
    print("====" + "="*len(s) + "====\n")
    return


log("Starting calculation")

# Some standards for plotting
rc.update({'font.size' : 12})

tall_y = []
all_y = []
tall_x = []
all_x = []
tall_z = []
all_z = []

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
    f.close()

if ct.showmovie or ct.savemovie:
    log("Start animation")
    inter = int(1000/ct.fps)

    fig = plt.figure()
    ax = fig.subplots()
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
        animation.save("Resultats/" + out + ".mp4", writer=writer, dpi=ct.res)

    if ct.showmovie:
        log("Showing animation")
        plt.show()

log("END")
