# INPUT PARAMETERS #
# Es necessita tenir a una carpeta els arxius amb noms den.XY.#######.dat i den.XZ.#######.dat

# File control
folder_name = "/g5work/g5esanchez/relaxacio_rotacional/hcl_rot/hcl/rel/trunc_j1_mj0_jmax6/"        # Where the density files are stored.
fileout = "HCl_jmax6_bastrunc_g96"       # Without extension. It will be automatically .mp4
graph_title = r"HCl relaxation. (j$\mathbf{_{0}}$=1, m$\mathbf{_{j,0}}$=0, j$\mathbf{_{max}}$=6, bt, basetruncada)" 

# Control which axis are taken into account
is_x = True
is_y = True
is_z = True

# Movie settings
showmovie = False
savemovie = True
res = 600                  # Resolution of the movie (in DPI, 600 is standard impression quality)
bit_rate = 30000             # No se molt be que fa pero 1800 es de l'exemple de matplotlib
fps = 10                    # Fotograms per second. Higher framerate will make time pass faster.
