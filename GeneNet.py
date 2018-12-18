import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import itertools as itl

class GeneNet:
    def __init__(self, N=20, Nin=5, Nout=5, M=5, dt=0.01, scale=40):
        self.N    = N
        self.Nin  = Nin
        self.Nout = Nout
        self.M    = M

        self.dt     = dt
        self.scale  = scale
        self.step   = int(scale/dt)

        self.time = np.arange(0, self.scale, self.dt)

        #係数決定
        W = np.random.randn(self.N*self.N).reshape([self.N, self.N])

        self.W = W
