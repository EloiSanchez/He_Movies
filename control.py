# INPUT PARAMETERS #
# Es necessita tenir a una carpeta els arxius amb noms den.XY.#######.dat i den.XZ.#######.dat

# File control
# folder_name = "/g5work/g5esanchez/relaxacio_rotacional/hcl_rot/hcl/rel/trunc_j1_mj0_jmax6/"        # Where the density files are stored.
folder_name = "carpeta/test/"
fileout = "test"       # Without extension. It will be automatically .mp4

# Plot settings
graph_title = r'(BAD) Test. (j$_{0}$=1, m$_{j,0}$=0, j$_{max}$=6, bt, basetruncada)' 
# graph_title = ""
font_size = 10
ax_font_size = 12
tit_font_size = 12
pos_t = (-19.5, 0.037)  # Position of the time stamps
t_bold = "normal"   # For bold -> "bold", for regular -> "normal"
lineweight = 1
x_title = r"Axis ($\rm{\AA}$)"
xrang = (-20, 20)

y_title_dens = r'Helium denisty ($\AA^{-3}$)'
y_title_deriv = r'$d\rho/dq$ $(\AA^{-4})$'
yrang_dens = (0, 0.04)
yrang_deriv = (-0.03, 0.03)

# Plot control
is_x = True
is_y = True
is_z = True
is_dens = True
is_deriv = True
is_together = True

# Movie settings
showmovie = False
savemovie = True
res = 300                  # Resolution of the movie (in DPI, 600 is standard impression quality)
bit_rate = 10000             # No se molt be que fa pero 1800 es de l'exemple de matplotlib
fps = 7                    # Fotograms per second. Higher framerate will make time pass faster.
