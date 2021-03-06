import numpy as np

def getABd(n, dt):
    nt = n*dt
    snt = np.sin(nt)
    cnt = np.cos(nt)
    Ad = np.array([[    4.0 - 3.0 * cnt, 0.0,      0.0,         (1.0 / n) * snt,              (2.0 / n) * (1 - cnt),             0.0],
                 [     6.0 * (snt - nt), 1.0,      0.0, (2.0 / n) * (cnt - 1.0), (1.0 / n) * (4.0 * snt - 3.0 * nt),             0.0],
                 [                  0.0, 0.0,      cnt,                     0.0,                                0.0, (1.0 / n) * snt],
                 [        3.0 * n * snt, 0.0,      0.0,                     cnt,                          2.0 * snt,             0.0],
                 [6.0 * n * (cnt - 1.0), 0.0,      0.0,              -2.0 * snt,                    4.0 * cnt - 3.0,             0.0],
                 [                  0.0, 0.0, -n * snt,                     0.0,                                0.0,             cnt]
                ])

    Bd = np.array([[             (-1.0 / (n**2)) * cnt,               (2.0 / n) * (dt - (1.0 / n) * snt),                  dt],
                  [-(2.0 / n) * (dt - (1.0 / n) * snt), (1.0 / n) * (-(4.0 / n) * cnt - 1.5 * n * dt**2),                  dt],
                  [                                 dt,                                               dt, -(1.0 / n**2) * cnt],
                  [                    (1.0 / n) * snt,                                 -(2.0 / n) * cnt,                  dt],
                  [                    (2.0 / n) * cnt,                       (4.0 / n) * snt - 3.0 * dt,                  dt],
                  [                                 dt,                                               dt,     (1.0 / n) * snt]
                ])
    return (Ad, Bd)

def getAB(n, dt):
    nt = n*dt
    snt = np.sin(nt)
    cnt = np.cos(nt)
    A = np.array([[    4.0 - 3.0 * cnt, 0.0,      0.0,         (1.0 / n) * snt,              (2.0 / n) * (1 - cnt),             0.0],
                 [     6.0 * (snt - nt), 1.0,      0.0, (2.0 / n) * (cnt - 1.0), (1.0 / n) * (4.0 * snt - 3.0 * nt),             0.0],
                 [                  0.0, 0.0,      cnt,                     0.0,                                0.0, (1.0 / n) * snt],
                 [        3.0 * n * snt, 0.0,      0.0,                     cnt,                          2.0 * snt,             0.0],
                 [6.0 * n * (cnt - 1.0), 0.0,      0.0,              -2.0 * snt,                    4.0 * cnt - 3.0,             0.0],
                 [                  0.0, 0.0, -n * snt,                     0.0,                                0.0,             cnt]
                ])

    B = A[:, 3:6]
    return (A, B)
