#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def plot_belief(belief):
    
    plt.figure()
    
    ax = plt.subplot(2,1,1)
    ax.matshow(belief.reshape(1, belief.shape[0]))
    ax.set_xticks(np.arange(0, belief.shape[0],1))
    ax.xaxis.set_ticks_position("bottom")
    ax.set_yticks([])
    ax.title.set_text("Grid")
    
    ax = plt.subplot(2, 1, 2)
    ax.bar(np.arange(0, belief.shape[0]), belief)
    ax.set_xticks(np.arange(0, belief.shape[0], 1))
    ax.set_ylim([0, 1.05])
    ax.title.set_text("Histogram")


def motion_model(action, belief):
    
    pf = 0.7  # Probability to move forward/backward successfully
    po = 0.1  # Probabilityto move in opposite direction
    pstay = 0.2  # Probability of staying in the same place

    belief_new = np.zeros(belief.shape)
    
    if action == 'F':  # Forward movement
        for i in range(len(belief)):

            if i > 0 and i < len(belief) - 1:  # Cells in the middle 
                belief_new[i] = belief[i-1] * pf + belief[i] * pstay + belief[i+1] * po

            elif i == 0:  # Leftmost cell
                belief_new[i] = belief[i] * pstay + belief[i+1] * po

            elif i == len(belief) - 1:  # Rightmost cell
                belief_new[i] = belief[i] * pstay + belief[i-1] * pf
    
    elif action == 'B':  # Backward movement
        for i in range(len(belief)):
            
            if i > 0 and i < len(belief) - 1:  # Cells in the middle
                belief_new[i] = belief[i-1] * po + belief[i] * pstay + belief[i+1] * pf

            elif i == 0:  # Leftmost cell
                belief_new[i] = belief[i] * pstay + belief[i+1] * pf

            elif i == len(belief) - 1:  # Rightmost cell
                belief_new[i] = belief[i] * pstay + belief[i-1] * po
    
    return belief_new
    
def sensor_model(observation, belief, world):
    pwhite = 0.7
    pblack = 0.9
    belief_new = np.copy(belief)

    if observation == 0:
        for i, cell in enumerate(world):
            if cell == 0:
                belief_new[i] = belief[i] * pwhite
            else:
                belief_new[i] = belief[i] * (1 - pwhite)
    else: 
        for i, cell in enumerate(world):
            if cell == 1:
                belief_new[i] = belief[i] * pblack
            else:
                belief_new[i] = belief[i] * (1 - pblack)

    return belief_new/np.sum(belief_new)

def recursive_bayes_filter(actions, observations, belief, world):

    sensor_model(observations[0], belief, world)

    for i , action in enumerate(actions):
        belief = motion_model(action, belief)
        belief = sensor_model(observations[i+1], belief, world)

    return belief
    # add code here
