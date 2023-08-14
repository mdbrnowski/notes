import sys
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.tri import Triangulation
import numpy as np

OPTIONS = ['p8w', 'b4a']

rc('font', **{'family': 'serif', 'size': 7})
rc('axes', labelpad=0)
rc('xtick.major', pad=0)
rc('ytick.major', pad=0)
# rc('text', usetex=True)

if len(sys.argv) != 2:
    print(f'One should provide exactly one argument ({len(sys.argv) - 1} given)')
    print('Avaible options:')
    print('\n'.join(OPTIONS))
    sys.exit()

fig = plt.figure()
fig.set_figwidth(5)
ax = fig.add_subplot(projection='3d')
margin_x = 0.2
margin_y = 0.2
margin_z = 0.2

if sys.argv[1] == 'p8w':
    Dx = (-0.5, 1.5)
    Dy = (-0.5, 1.5)

    X = np.linspace(Dx[0], Dx[1], 100)
    Y = np.linspace(Dy[0], Dy[1], 100)
    X, Y = np.meshgrid(X, Y)
    Z = X**3 + Y**3 - 3*X*Y
    ax.view_init(12, 105)
    ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)
    ax.contour(X, Y, Z, zdir='z', cmap='seismic', linewidths=0.8, offset=(np.min(Z) - margin_z - 0.15), levels=11)

elif sys.argv[1] == 'b4a':
    Dx = (-6**(1/2), 6**(1/2))
    Dy = (0, 6)

    ax.view_init(18, -114)

    X = np.linspace(Dx[0]-0.2, Dx[1]+0.2, 100)
    Y = np.linspace(Dy[0]-0.2, Dy[1]+0.2, 100)
    X, Y = np.meshgrid(X, Y)
    Z = X**2 + X*Y + 2*Y - X
    ax.plot_surface(X, Y, Z, color='gray', edgecolor='dimgray', lw=0.5, rstride=8, cstride=8, alpha=0.1)

    X_c1 = np.linspace(Dx[0], Dx[1], 100)
    Y_c1 = X_c1**2
    Z_c1 = X_c1**2 + X_c1*Y_c1 + 2*Y_c1 - X_c1
    ax.plot(X_c1, Y_c1, Z_c1, lw=1.2, color='royalblue')

    X_c2 = np.linspace(Dx[0], Dx[1], 100)
    Y_c2 = np.linspace(Dy[1], Dy[1], 100)  # sic!
    Z_c2 = X_c2**2 + X_c2*Y_c2 + 2*Y_c2 - X_c2
    ax.plot(X_c2, Y_c2, Z_c2, lw=1.2, color='royalblue')

    X_d = np.linspace(Dx[0], Dx[1], 15)
    Y_d = np.linspace(Dy[0], Dy[1], 15)
    X_d, Y_d = np.meshgrid(X_d, Y_d)
    X_d, Y_d = np.ravel(X_d), np.ravel(Y_d)
    X_d, Y_d = X_d[Y_d >= X_d**2], Y_d[Y_d >= X_d**2]
    X_d = np.concatenate((X_d, X_c1, X_c2))
    Y_d = np.concatenate((Y_d, Y_c1, Y_c2))
    Z_d = X_d**2 + X_d*Y_d + 2*Y_d - X_d
    tri = Triangulation(np.ravel(X_d), np.ravel(Y_d))
    ax.plot_trisurf(X_d, Y_d, Z_d, triangles=tri.triangles, color='royalblue', alpha=0.3)
else:
    print('Avaible options:')
    print('\n'.join(OPTIONS))
    sys.exit()


ax.set(xlim=(Dx[0] - margin_x, Dx[1] + margin_x), ylim=(Dy[0] - margin_y, Dy[1] + margin_y),
        zlim=(np.min(Z) - margin_z, np.max(Z) + margin_z),
        xlabel='x', ylabel='y', zlabel='f(x, y)')
plt.show()