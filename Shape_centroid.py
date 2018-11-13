import numpy as np
import matplotlib.pyplot as plt
from normal_gait import load_normal_gait as NG
import anal_functions as af


hip2, knee2 = NG(n=2)
hip1, knee1 = NG(n=1)
hip3, knee3 = NG(n=3)


def get_centroid(x, y):
    difference = (x[0:-1] * y[1:] - x[1:] * y[0:-1])
    contour_area = difference.sum() / 2
    g_x = ((x[0:-1] + x[1:]) * difference).sum() / (6 * contour_area)
    g_y = ((y[0:-1] + y[1:]) * difference).sum() / (6 * contour_area)
    return g_x, g_y


g_knee, g_hip = get_centroid(knee2, hip2)

g_knee
g_hip
plt.plot(knee2, hip2, 'b', g_knee, g_hip, 'ro')


def average_bending_energy(curvature):
    return curvature.sum() / curvature.shape[0]


from anal_functions import curva_bad


curva2 = curva_bad(knee2, hip2)
curva1 = curva_bad(knee1, hip1)
curva3 = curva_bad(knee3, hip3)


abe1 = average_bending_energy(curva1)
abe2 = average_bending_energy(curva2)
abe3 = average_bending_energy(curva3)


print('Average benfing energy for first is {}'.format(abe1))
print('Average benfing energy for second is {}'.format(abe2))
print('Average benfing energy for third is {}'.format(abe3))


import approximating as app


pathology = app.load_data('femoral hernia')[0]
r_hip, r_knee = pathology[0:2]
l_hip, l_knee = pathology[3:5]

hip_knee_lst = pathology[0:2] + pathology[3:5]
curvas = [curva_bad(pathology[0], pathology[1]), curva_bad(pathology[3], pathology[4])]
path_abe = [average_bending_energy(curva) for curva in curvas]


print(path_abe)


baskakova_data = app.load_data('baskakova')[0]
hip_knee_bask_lst = [tuple(baskakova_data[0:2]), tuple(baskakova_data[3:5])]


bask_curvas = [curva_bad(*hip_knee) for hip_knee in hip_knee_bask_lst]
bask_abe = [average_bending_energy(curva) for curva in bask_curvas]
print(bask_abe)


plt.plot(*hip_knee_bask_lst[0], 'r', *hip_knee_bask_lst[1], 'b')





centriod_f_arr = np.sqrt(np.square(knee2 - g_knee) + np.square(hip2 - g_hip))
plt.plot(centriod_f_arr)


def centroid_distance_func(x,  y):
    g_x, g_y = get_centroid(x, y)
    return np.sqrt(np.square(x - g_x) + np.square(y - g_y))


centroid_dist_l = centroid_distance_func(l_knee, l_hip)
centroid_dist_r = centroid_distance_func(r_knee, r_hip)


plt.plot(centroid_dist_l, 'b', centroid_dist_r, 'r', centriod_f_arr, 'g')
centr_bask_l = centroid_distance_func(*hip_knee_bask_lst[0])
centr_bask_r = centroid_distance_func(*hip_knee_bask_lst[1])
plt.plot(centr_bask_l, 'b', centr_bask_r, 'r')
