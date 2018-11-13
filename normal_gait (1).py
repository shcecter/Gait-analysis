import numpy as np
import pandas as pd


def polynomial(xy, deg=16):
    x, y = xy['x'], xy['y']
    x = x.dropna().as_matrix()
    y = y.dropna().as_matrix()
    common_x = np.linspace(0, 1, num=100)
    poly = np.poly1d(np.polyfit(x, y, deg))
    out_y = poly(common_x)
    der_y = np.polyder(poly)(common_x)
    dder_y = np.polyder(poly, 2)(common_x)
    return (out_y, der_y, dder_y)


def load_normal_gait(n):
    sheetname = 'normal' # type inherent sheet name

    dic_data = pd.read_excel('sheetdata/United data.xlsx', sheet_name=None, header=[0,1]) ### SUITABLE FOR THIS DIRECTORY ONLY!!!
    data = dic_data.pop(sheetname).reset_index(drop=True)


    approxed_d = {}
    for curve in data.columns.levels[0]:
        data[curve].head()
        poly_res = polynomial(data[curve])
        approxed_d[curve + 'y'] = poly_res[0]
        approxed_d[curve + 'ders'] = poly_res[1:2]


    knee1 = approxed_d['knee_1y']
    hip1 = approxed_d['hip_1y']
    knee2 = approxed_d['knee_2y']
    hip2 = approxed_d['hip_2y']
    knee3 = approxed_d['knee_3y']
    hip3 = approxed_d['hip_3y']
    t = np.linspace(0, 1, num=100)


    if n==1:
        return (hip1, knee1)


    elif n==2:
        return (hip2, knee2)

    elif n==3:
        return (hip3, knee3)
