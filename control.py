# INPUT PARAMETERS #
# Es necessita tenir a una carpeta els arxius amb noms den.XY.#######.dat i den.XZ.#######.dat

# File control
# folder_name = '/g5work/g5esanchez/relaxacio_rotacional/hcl_rot/hcl/rel/trunc_j1_mj0_jmax6/'        # Where the density files are stored.
folder_name = '/g5work/g5esanchez/relaxacio_rotacional/hcl_rot/herm_diag/grid_96/hcl/rel/jmax5/ini_j1mj0/'
fileout = 'test_talls_HCl_j1mj0'       # Without extension. It will be automatically .mp4
is_den = False  # If True read format den.xy.__.dat, if False read format tall.x.__.dat

# Plot settings
graph_title = r'HCl ($|1,0\rangle$, $N$=100)' 
# graph_title = ''
font_size = 10
ax_font_size = 12
tit_font_size = 12
pos_t = (-19.5, 0.065)  # Position of the time stamps
t_bold = 'normal'   # For bold -> 'bold', for regular -> 'normal'
lineweight = 1.5
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
showmovie = False 
savemovie = True 
res = 300                  # Resolution of the movie (in DPI, 600 is standard impression quality)
bit_rate = 2000             # No se molt be que fa pero 1800 es de l'exemple de matplotlib
fps = 60                    # Fotograms per second. Higher framerate will make time pass faster.
