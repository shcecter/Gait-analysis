tup = (np.zeros(i + 1) for i in range(3))
type(tup)
print(tup)


lst = [i for i in range(3)]
lst
arr = np.zeros(5)
type(arr)
arr.shape
lst = [arr]


import approximating as app
import numpy as np
import matplotlib.pyplot as plt


deriv = app.load_data(sheetname='baskakova', derivatives=3)
type(deriv)
deriv[1].keys()
rhip_der = deriv[1]['righthip']
rknee_ders = deriv[1]['rightknee']


def curva(x_der, x_dder, y_der, y_dder):
    nominator = x_der * y_dder - y_der * x_dder
    denominator = np.power((np.square(x_der) + np.square(y_der)), 3/2)
    return nominator / denominator


knee_der = rknee_ders[0]
hip_der = rhip_der[0]
knee_dder = rknee_ders[1]
hip_dder = rhip_der[1]


r_cur = curva(knee_der, knee_dder, hip_der, hip_dder)
plt.plot(r_cur)
knee_ddder = rknee_ders[2]
hip_ddder = rhip_der[2]

plt.figure()
plt.plot(knee_der * hip_ddder, 'r', knee_ddder * hip_der, 'b')
np.array(knee_ddder * hip_der == knee_der * hip_ddder)
knee_der[knee_der == 0.0]
np.array([knee_der == 0.0])
np.array([knee_der * hip_ddder == 0])
np.array([hip_der * knee_ddder == 0.0])
r_cur_der = np.diff(r_cur)
np.array([r_cur_der < 0.0000000000000000000000000000000000000000001]).sum()
