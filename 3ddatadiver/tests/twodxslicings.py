import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import loaddata
import createpslist
import zdirection
from mpl_toolkits.mplot3d import Axes3D


def twodxslicings(filename, z_dir, location_slices, export_filename2, x_actual, y_actual, x_size, y_size):
    z_direction, Z_dir = zdirection.zdirection(filename, z_dir)
    a = np.linspace(0, x_actual, x_size)[location_slices]
    b = np.linspace(0, y_actual, y_size)
    c = Z_dir
    X, Z, Y = np.meshgrid(a, c, b)

    As = np.array(createpslist.createpslist(filename, x_size, y_size))[0:len(Z_dir), location_slices, :]

    fig1 = plt.figure(figsize=(11, 9))
    plt.subplot(111)
    plt.imshow(As, aspect='auto')
    plt.xlabel('Y', fontsize=12)
    plt.ylabel('Z', fontsize=12)
    plt.title('2D X Slicing (X='+str(round(a,3)) + 'nm)for the Phase Shift of AFM data', fontsize=13)
    plt.colorbar()

    setStr = '{}_2d_Xslices.png'.format(export_filename2)
    fig1.savefig(setStr)