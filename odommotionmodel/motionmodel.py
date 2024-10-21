# add your fancy code here
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def inverse_motion_model(prev_pose, cur_pose):
     
    ### TODO
    rot1 = np.arctan2(cur_pose[1] - prev_pose[1], cur_pose[0] - prev_pose[0]) - prev_pose[2]
    trans = np.sqrt((cur_pose[0] - prev_pose[0])**2 + (cur_pose[1] - prev_pose[1])**2)
    rot2 = cur_pose[2] - prev_pose[2] - rot1
    return rot1, trans, rot2


def prob(mu, sigma):

    ### TODO
    prob  =(1 / (np.sqrt(2 * np.pi * sigma**2))) * np.exp(-0.5 * (mu**2 / sigma**2))
    return prob


def motion_model(cur_pose, prev_pose, odom, alpha):
    
    ### TODO
    del_rot1 , del_trans, del_rot2 = inverse_motion_model(prev_pose, cur_pose)
    u = [odom[0], odom[1], odom[2]]

    x_p = u[0]-del_rot1
    y_p = u[1]-del_trans
    theta_p = u[2]-del_rot2

    p1 = prob(x_p , alpha[0]*abs(u[0]) + alpha[1]*u[1])
    p2 = prob(y_p, alpha[2]*u[1]+ alpha[3]*(abs(u[0])+abs(u[2])))
    p3 = prob(theta_p, alpha[0]*abs(u[2])+alpha[1]*u[1])

    p = p1 * p2 * p3
    return p



def sample(b):
    tot = 0
    for i in range(12):
        ### TODO
       tot += 0.5 * np.random.uniform(-b, b) 
    return tot


def sample_motion_model(prev_pose, odom, alpha):
    
    ### TODO
    r1, t, r2 = odom
    

    d_r1 = r1 + sample(alpha[0]*abs(r1) + alpha[1]*t)
    d_t = t + sample(alpha[2]*t + alpha[3]*(abs(r1) + abs(r2)))
    d_r2 = r2 + sample(alpha[0]*abs(r2) + alpha[1]*t)

    x = prev_pose[0] + d_t * np.cos(prev_pose[2] + d_r1)
    y = prev_pose[1] + d_t * np.sin(prev_pose[2] + d_r1)
    theta = prev_pose[2] + d_r1 + d_r2

    return x, y, theta
