import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def gait_ftransform(joints_l, n_components, transformed=False):
    if not transformed:
        input_matrix = np.vstack((joints_l))
        result = PCA(n_components).fit_transform(input_matrix)
        
        
    else:
        pass
    
    
    return result


def plot_gait_pca(gait_pca_res, joints_l):
    names = ['r hip', 'r knee', 'r ankle', 'l hip', 'l knee', 'l ankle']
    plt.figure(figsize=(10,5))
    for i in range(gait_pca_res.shape[0]):
        plt.plot(gait_pca_res[i, :])
        
        
    plt.legend(names)
    plt.grid()
    
    
    plt.figure(figsize=(6,5))
    for joint in joints_l:
        plt.plot(joint)
        
        
    plt.grid()
