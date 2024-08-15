import numpy as np
import copy

error_array_pj = []

def PJ(grid_array, beta):
    
    ## A copy of the grid is created to store the value of previous iteration
    
    copy_grid_PJ = copy.deepcopy(grid_array)
    iteration_counter = 0
    
    while True:
         
        error=0
        for i in range(1,40):
            for j in range(1,80):

                # On the RHS copy_grid_PJ is used, because grid_array will have updated values

                grid_array[j,i] = ( 1/( 2*(1+beta*beta) ) )*( copy_grid_PJ[j,i+1] + copy_grid_PJ[j,i-1] + (beta*beta)*( copy_grid_PJ[j+1,i] + copy_grid_PJ[j-1,i]) )
                error += ( grid_array[j, i] - copy_grid_PJ[j, i] )
        
        error_array_pj.append(error)
        
        ## Copy grid updated
        copy_grid_PJ = copy.deepcopy(grid_array)

        iteration_counter +=1
        if error < 0.001:
            break

    print('# iter PJ:'+str(iteration_counter))   

    return copy_grid_PJ