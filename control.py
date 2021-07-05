# INPUT PARAMETERS #
# Es necessita tenir a una carpeta els arxius amb noms den.XY.#######.dat i den.XZ.#######.dat

# File control
# folder_name = '/g5work/g5esanchez/relaxacio_rotacional/hcl_rot/hcl/rel/trunc_j1_mj0_jmax6/'        # Where the density files are stored.
folder_name = '/g5work/g5esanchez/relaxacio_rotacional/hcl_rot/tcl/rel/trunc_tcl_jmax8/'
fileout = 'TCl_jmax8_incomplete_g96_bt'       # Without extension. It will be automatically .mp4
is_den = True  # If True read format den.xy.__.dat, if False read format tall.x.__.dat

# Plot settings
graph_title = r'TCl ($|1,0\rangle$, j$_{max}$=8, $N$=100, g96, bt)' 
# graph_title = ''
font_size = 10
ax_font_size = 12
tit_font_size = 12
pos_t = (-19.5, 0.037)  # Position of the time stamps
t_bold = 'normal'   # For bold -> 'bold', for regular -> 'normal'
lineweight = 1
x_title = r'Axis ($\rm{\AA}$)'
xrang = (-20, 20)

y_title_dens = r'Helium denisty ($\AA^{-3}$)'
y_title_deriv = r'$d\rho/dq$ $(\AA^{-4})$'
yrang_dens = (0, 0.07)
yrang_deriv = (-0.07, 0.07)

# Plot control
is_x = True
is_y = True
is_z = True

# Movie settings
showmovie = True 
savemovie = False
res = 300                  # Resolution of the movie (in DPI, 600 is standard impression quality)
bit_rate = 2000             # No se molt be que fa pero 1800 es de l'exemple de matplotlib
fps = 7                    # Fotograms per second. Higher framerate will make time pass faster.
