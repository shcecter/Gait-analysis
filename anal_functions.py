import numpy as np
import pandas as pd


def curva_bad(x, y):
    x_der = np.diff(x)[:-1]
    y_der = np.diff(y)[:-1]
    x_dder = np.diff(x, n=2)
    y_dder = np.diff(y, n=2)
    nominator = x_der * y_dder - y_der * x_dder
    denominator = np.power((np.square(x_der) + np.square(y_der)), 3/2)
    return nominator / denominator


def curva(x, y, x_der, x_dder, y_der, y_dder):
    nominator = x_der * y_dder - y_der * x_dder
    denominator = np.power((np.square(x_der) + np.square(y_der)), 3/2)
    return nominator / denominator


def get_centroid(x, y):
    difference = (x[0:-1] * y[1:] - x[1:] * y[0:-1])
    contour_area = difference.sum() / 2
    g_x = ((x[0:-1] + x[1:]) * difference).sum() / (6 * contour_area)
    g_y = ((y[0:-1] + y[1:]) * difference).sum() / (6 * contour_area)
    return g_x, g_y


def average_bending_energy(curvature):
    return curvature.sum() / curvature.shape[0]


def centroid_distance_func(x,  y):
    g_x, g_y = get_centroid(x, y)
    return np.sqrt(np.square(x - g_x) + np.square(y - g_y))
