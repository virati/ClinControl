#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 13:26:58 2019

@author: virati
Here we'll illustrate 'SNR' by finding means in subsets of data and highlighting how stupid it is to memorize arbitrary precision
We focus on a linear model with slope M here. May need to simplify further to convey this in the 'pediatrics' way
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

def truth(x,slope=5):
    return slope * x

def noise(x):
    return x + np.random.normal(size=x.shape)

samples_per_experiment = 1000
experiments = 2

cost_per_sample = 10
cost_experiment_overhead = 1000
cost_per_experiment = cost_per_sample * samples_per_experiment + cost_experiment_overhead

#%%
plt.figure()
x = []
y = []
for ee in range(experiments):
    x.append(np.random.uniform(-10,10,size=(samples_per_experiment,1)))
    y.append(noise(truth(x[-1])))
    print(np.mean(y[-1]))
    plt.scatter(x[-1],y[-1])