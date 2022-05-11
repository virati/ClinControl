#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:45:42 2019

@author: virati
Two distributions for groups
Message: if the variance is so large, what is the point of memorizing arbitrary cutoffs?
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

n_samp = 10000
X = np.random.uniform(0.3,0.6,size=(n_samp,1))
X = np.random.normal(0.5,0.1,size=(n_samp,1))
pre_var = 0.6

Y = (X < 0.5).astype(np.int)
Z = np.random.normal(Y,pre_var,size=X.shape) #this is pure artifact with respect to the means of the two distributions


#%%
plt.figure()
plt.hist(Z,alpha=0.5)
plt.hist(Z[Y.astype(np.bool)],color='red',alpha=0.3)
plt.hist(Z[~Y.astype(np.bool)],color='green',alpha=0.3)
