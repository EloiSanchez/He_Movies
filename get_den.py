def get_string(jk, j):
    """
    Generate filenames to read
    """
    str1 = "{}.0.".format(jk)
    num = "0"*(7-len(str(j))) + str(j)
    return str1 + num + ".dat"

def get_den(prefix, maxnum, delta_t, pdenpar, pener, is_den):
    import numpy as np
    import logging

    # Primer cal trobar els indexs que s'han generat al directori de resultats
    if is_den:
        files_X = [get_string("den.XY", s) for s in range(1, int(maxnum + 1))]
        files_Z = [get_string("den.XZ", s) for s in range(1, int(maxnum + 1))]
    else:
        files_Z = ["/" + get_string("tall.z", s) for s in range(1, int(maxnum + 1))]
        files_Y = ["/" + get_string("tall.y", s) for s in range(1, int(maxnum + 1))]
        files_X = ["/" + get_string("tall.x", s) for s in range(1, int(maxnum + 1))]
    
    # logging.info("Reading ALL density files for possible storage")

    grid_x = []  # Construim nomes una grid perque grid_x = grid_y = grid_z
    t = []
    file_ind = 0
    with open(prefix + files_X[0], "r") as fil:
        lines = fil.readlines()
    
    # Bloc de lectura en cas que fem servir format den.__.dat
    if is_den:
        print('Reading from format den.__.dat')
        print('Constructing grid')
        for line in lines:
            x, y, den = [float(s) for s in line.split()]
            if abs(y) < 0.001 and x not in grid_x:
                grid_x.append(x)
            
        print('Getting X and Y densities')
        all_x = []
        all_y = []
        for name in files_X:
            file_ind += 1
            t.append(file_ind * delta_t * pdenpar)

            with open(prefix + name, "r") as fil:
                lines = fil.readlines()

            den_x = [] 
            den_y = []
            for line in lines:
                x, y, den = [float(s) for s in line.split()]

                if abs(x) < 0.001:
                    den_y.append(den)

                if abs(y) < 0.001:
                    den_x.append(den)
            all_x.append(den_x)
            all_y.append(den_y)

        print('Getting Z densities')
        all_z = []
        for name in files_Z:
            with open(prefix + name, "r") as fil:
                lines = fil.readlines()
            den_z = []
            for line in lines:
                x, z, den = [float(s) for s in line.split()]

                if abs(x) < 0.001:
                    den_z.append(den)
            all_z.append(den_z)
        all_x, all_y, all_z = np.array(all_x), np.array(all_y), np.array(all_z)

    # Bloc de lectura en cas que fem servir format tall.__.dat
    else:
        print('Reading from format tall.__.dat')
        print('Constructing grid')
        for line in lines:
            x, den = [float(s) for s in line.split()]
            grid_x.append(x)
        
        print('Getting X densities')
        all_x = []
        for name in files_X:
            file_ind += 1
            t.append(file_ind * delta_t * pener)

            with open(prefix + name, "r") as fil:
                lines = fil.readlines()

            den_x = []
            den_y = []
            for line in lines:
                x, den = [float(s) for s in line.split()]
                den_x.append(den)
            all_x.append(den_x)
            
        print('Getting Y densities')
        all_y = []
        for name in files_Y:
            with open(prefix + name, "r") as fil:
                lines = fil.readlines()
            den_y = []
            for line in lines:
                y, den = [float(s) for s in line.split()]
                den_y.append(den)
            all_y.append(den_y)

        print('Getting Z densities')
        all_z = []
        for name in files_Z:
            with open(prefix + name, "r") as fil:
                lines = fil.readlines()
            den_z = []
            for line in lines:
                z, den = [float(s) for s in line.split()]
                den_z.append(den)
            all_z.append(den_z)
        all_x, all_y, all_z = np.array(all_x), np.array(all_y), np.array(all_z)
    print('Finished reading files')

    # Ens quedem amb el pic de densitat maxima de la seccio negativa dels eixos
    max_x = []
    max_y = []
    max_z = []
    N_grid = len(grid_x)
    max_index = np.argmax(all_z[0,:N_grid // 2 + 1])
    for i in range(len(all_x[:,0])):
        max_x.append(all_x[i,max_index])
        max_y.append(all_z[i,max_index])
        max_z.append(all_z[i,max_index])

    with open("He_solv_layer.tmp", "w") as fil:
        fil.write("# Values of the density of the first solvation layer.\n")
        fil.write("# Time (ps)  X axis  Y axos  Z axis\n")
        for i in range(len(t)):
            fil.write("{} {} {}\n".format(t[i], max_x[i], max_y[i], max_z[i]))
        
    return t, np.array(max_x), np.array(max_y), np.array(max_z), np.array(t)

