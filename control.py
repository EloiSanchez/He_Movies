# INPUT PARAMETERS #
# Es necessita tenir a una carpeta els arxius amb noms den.XY.#######.dat i den.XZ.#######.dat

# File control
# folder_name = "/g5work/g5esanchez/relaxacio_rotacional/hcl_rot/hcl/rel/trunc_j1_mj0_jmax6/"        # Where the density files are stored.
folder_name = "carpeta/"
fileout = "test"       # Without extension. It will be automatically .mp4

# Plot settings
graph_title = r'(BAD) HCl relaxation. (j$_{0}$=1, m$_{j,0}$=0, j$_{max}$=6, bt, basetruncada)' 
y_title = r'Helium denisty ($\AA^{-3}$)'
x_title = r"Axis ($\rm{\AA}$)"
t_bold = "normal"   # For bold -> "bold", for regular -> "normal"
font_size = 10
ax_font_size = 12
tit_font_size = 12
lineweight = 1

# Control which axis are taken into account
is_x = True
is_y = True
is_z = True

# Movie settings
showmovie = True
savemovie = False
res = 300                  # Resolution of the movie (in DPI, 600 is standard impression quality)
bit_rate = 30000             # No se molt be que fa pero 1800 es de l'exemple de matplotlib
fps = 10                    # Fotograms per second. Higher framerate will make time pass faster.
