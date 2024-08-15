import numpy as np
import matplotlib.pyplot as plt
import Point_Jacobi_210010041 as PJ
import Gauss_Seidel_210010041 as GS
import PSOR_210010041 as PSOR
import exact_210010041 as exact
import os 

#Folder named 'plots' created 
if not os.path.exists('plots'):
    os.mkdir('plots')


## Grid Initialisation

def grid_init():
    plate_grid = np.zeros([81,41])

    ## Boundary Condition

    plate_grid[80,:] = 250
    return plate_grid

## Constants

dx=1/40
dy=2/80

beta=dx/dy

a = np.square( ( np.cos(np.pi/40) + (beta**2)*np.cos(np.pi/80)  )/( 1 + beta**2 ) )

omega_opt = ( 2 - 2*np.sqrt( 1 - a)/a)


plate_grid = grid_init() ## Setting grid back to intial state
solution_array_GS = GS.GS(plate_grid, beta)


plate_grid = grid_init() ## Setting grid back to intial state
solution_array_PJ = PJ.PJ(plate_grid, beta)


plate_grid = grid_init() ## Setting grid back to intial state
solution_array_PSOR = PSOR.PSOR(plate_grid, beta, omega_opt)


## x and y arrays to be used in plots 
x=np.arange(0, 1 + dx, dx)
y=np.arange(0, 2 + dy, dy)


## Grid creation for contour plot and exact sloution
X, Y =np.meshgrid(1-x,2-y)

T_exact = exact.T(X,Y, 50)


## BC's on exact solution
T_exact[80, :] = 250
T_exact[0, :]  = 0
T_exact[:, 0]  = 0
T_exact[:, 40] = 0

## Iteration array initialised
N_PJ = []
for i in range(len(PJ.error_array_pj)):
    N_PJ.append(i)
N_GS = []
for i in range(len(GS.error_array_gs)):
    N_GS.append(i)
N_PSOR = []
for i in range(len(PSOR.error_array_psor)):
    N_PSOR.append(i)



## Convergence history plot and saved in 'plots' folder
plt.plot(N_PJ, np.log10(PJ.error_array_pj), label='Point Jacobi')
plt.plot(N_GS, np.log10(GS.error_array_gs), label='Point Gauss-Seidel')
plt.plot(N_PSOR, np.log10(PSOR.error_array_psor), label='Point Succesive Over Relaxation')
plt.grid()
plt.legend()
plt.title('$log_{10}$(ERROR) Vs Number of iterations')
plt.xlabel('No. of iterations')
plt.ylabel('$log_{10}$(ERROR)')
plt.savefig('plots/error_vs_N.png')
plt.close()


## Y_mid temperature plot and saved in 'plots' folder
plt.plot(1-x, solution_array_PJ[40, :], '--' ,label = 'Point Jacobi')
plt.plot(1-x, solution_array_GS[40, :], 'o', label = 'Point Gauss-Seidel')
plt.plot(1-x, solution_array_PSOR[40, :], '*' ,label = 'Point Succesive Over Relaxation')
plt.plot(1-x, T_exact[40, :], '2' ,label = 'Exact')
plt.legend()
plt.grid()
plt.title("Temperature at y=1")
plt.ylabel('T ($^{o}$C)')
plt.xlabel('x')
plt.savefig('plots/y_mid.png')
plt.close()


## X_mid temperature plot and saved in 'plots' folder
plt.plot(2-y, solution_array_PJ[:, 20], '--' ,label = 'Point Jacobi')
plt.plot(2-y, solution_array_GS[:, 20], 'o', label = 'Point Gauss-Seidel')
plt.plot(2-y, solution_array_PSOR[:, 20], '*' ,label = 'Point Succesive Over Relaxation')
plt.plot(2-y, T_exact[:, 20], '2' ,label = 'Exact')
plt.legend()
plt.grid()
plt.title("Temperature at x=0.5")
plt.ylabel('T ($^{o}$C)')
plt.xlabel('y')
plt.savefig('plots/x_mid.png')
plt.close()

## Contour Subplot
plt.subplot(2,2,1)
plt.contourf(X, Y, solution_array_PJ, levels=100, cmap='plasma') 
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Temperature Contour PJ')
plt.colorbar(label='T ($^{o}$C)')

plt.subplot(2,2,2)
plt.contourf(X, Y, solution_array_GS, levels=100, cmap='plasma')  
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Temperature Contour PGS')
plt.colorbar(label='T ($^{o}$C)')

plt.subplot(2,2,3)
plt.contourf(X, Y, solution_array_PSOR, levels=100, cmap='plasma')  
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Temperature Contour PSOR')
plt.colorbar(label='T ($^{o}$C)')

plt.subplot(2,2,4)
plt.contourf(X, Y, T_exact, levels=100, cmap='plasma')  
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Temperature Contour Exact')
plt.colorbar(label='T ($^{o}$C)')

plt.tight_layout()
plt.savefig('plots/contour.png')
plt.close()


# X_mid temmperature errot plot
plt.plot(2-y, solution_array_GS[:, 20] - T_exact[:, 20], 'o' ,label = 'PGS - Exact')
plt.plot(2-y, solution_array_PJ[:, 20] - T_exact[:, 20], '*' ,label = 'PJ - Exact')
plt.plot(2-y, solution_array_PSOR[:, 20] - T_exact[:, 20], '2' ,label = 'PSOR - Exact')
plt.legend()
plt.grid()
plt.title("Temperature difference at x=0.5")
plt.ylabel('T ($^{o}$C)')
plt.xlabel('y')
plt.savefig('plots/x_mid_error.png')
plt.close()


# Y_mid temmperature errot plot
plt.plot(1-x, solution_array_GS[40, :] - T_exact[40, :], 'o' ,label = 'GS - Exact')
plt.plot(1-x, solution_array_PJ[40, :] - T_exact[40, :], '*' ,label = 'PJ - Exact')
plt.plot(1-x, solution_array_PSOR[40, :] - T_exact[40, :], '2' ,label = 'PSOR - Exact')
plt.legend()
plt.grid()
plt.title("Temperatur differencee at y=1")
plt.ylabel('T ($^{o}$C)')
plt.xlabel('x')
plt.savefig('plots/y_mid_error.png')
plt.close()