import numpy as np


def getAB(n, dt):
    nt = n*dt
    snt = np.sin(nt)
    cnt = np.cos(nt)
    A = np.array[[      4.0 - 3.0 * cnt, 0.0,      0.0,         (1.0 / n) * snt,              (2.0 / n) * (1 - cnt),             0.0],
                 [     6.0 * (snt - nt), 1.0,      0.0, (2.0 / n) * (cnt - 1.0), (1.0 / n) * (4.0 * snt - 3.0 * nt),             0.0],
                 [                  0.0, 0.0,      cnt,                     0.0,                                0.0, (1.0 / n) * snt],
                 [        3.0 * n * snt, 0.0,      0.0,                     cnt,                          2.0 * snt,             0.0],
                 [6.0 * n * (cnt - 1.0), 0.0,      0.0,              -2.0 * snt,                    4.0 * cnt - 3.0,             0.0],
                 [                  0.0, 0.0, -n * snt,                     0.0,                                0.0,             cnt]
                ]
