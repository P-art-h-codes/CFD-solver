import numpy as np
import copy

error_array_psor = []


def PSOR(grid_array, beta, omega):
    
    ## A copy of the grid is created to store the value of previous iteration
    
    copy_grid = copy.deepcopy(grid_array)
    iteration_counter = 0
    
    while True:
         
        error=0
        for i in range(1,40):
            for j in range(1,80):

                # On the RHS copy_grid_PJ is used, because grid_array will have updated values

                grid_array[j,i] = (1 - omega)*copy_grid[j,i] + ( omega/( 2*(1+beta*beta) ) )*( copy_grid[j,i+1] + copy_grid[j,i-1] + (beta*beta)*( copy_grid[j+1,i] + copy_grid[j-1,i]) )
                error += ( grid_array[j, i] - copy_grid[j, i] )
                copy_grid[j,i] = grid_array[j,i]

        
        error_array_psor.append(error)
        
        
        iteration_counter +=1
        if error < 0.001:
            break

    print('# iter PSOR:'+str(iteration_counter))

    return copy_grid