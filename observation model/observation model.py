# add your fancy code here
import numpy as np
import matplotlib.pyplot as plt

def plot_gridmap(gridmap):
    plt.figure()
    plt.imshow(gridmap, cmap='Greys')


def landmark_observation_model(z, x, b, sigma_r):
    # TODO
    zexp = np.sqrt((b[0]-x[0])**2 + (b[1]-x[1])**2)
    p = 2*np.pi*sigma_r**2 * (np.exp(-0.5*((z-zexp)**2)/sigma_r**2))
    return p


def observation_likelihood(r, b, gridmap, sigma_r, size):
    # TODO
    gridmap = np.zeros((size, size))  

    for i in range(size):
        for j in range(size):
            x = [i, j] 
            p_joint = 1.0  
           
            for k in range(len(b)):
                p = landmark_observation_model(r[k], x, b[k], sigma_r[k]) 
                p_joint *= p  
            
            gridmap[i, j] = p_joint  

    return gridmap

