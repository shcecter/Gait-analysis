import numpy as np
import pandas as pd


def approximate(data, deg=12, derivatives=0):
    data_t = data.T
    deriv_d = {}
    for side in ('right', 'left'):
        for joint in ('hip', 'knee', 'ankle'):
            t = np.linspace(0, 1, num=100)
            xy = data_t.loc[side, joint]
            x, y = xy.loc['x'].dropna().values, xy.loc['y'].dropna().values
            poly_app = np.poly1d(np.polyfit(x, y, deg))
            app = poly_app(t)
            data_t.loc[(side, joint, 'app'), :] = pd.Series(app)


            if derivatives:
                deriv_l = [poly_app.deriv(der_deg + 1)(t) for der_deg in range(derivatives)]
                deriv_d[side + joint] = deriv_l




    data = data_t.T
    r_hip = data['right']['hip']['app'].dropna().values
    r_knee = data['right']['knee']['app'].dropna().values
    r_ankle = data['right']['ankle']['app'].dropna().values
    l_hip = data['left']['hip']['app'].dropna().values
    l_knee = data['left']['knee']['app'].dropna().values
    l_ankle = data['left']['ankle']['app'].dropna().values



    return [r_hip, r_knee, r_ankle, l_hip, l_knee, l_ankle, t, deriv_d]


def load_data(sheetname, path='sheetdata/United data.xlsx', approx=True, derivatives=0, approx_deg=12):
    data = pd.read_excel(path, sheet_name=sheetname, header=[0, 1, 2])
    if approx:
        joints_l = approximate(data, deg=approx_deg, derivatives=derivatives)
        deriv_d = joints_l.pop()
        t = joints_l.pop()


    else:
        pass


    return joints_l, deriv_d
