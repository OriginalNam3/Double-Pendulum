import numpy as np
from scipy.integrate import odeint
global g
g = 9.81
global e


class DPendulum:
    def __init__(self, l1=1, m1=1, a1=np.radians(135), l2=1, m2=1, a2=np.radians(135)):
        self.l1 = l1
        self.m1 = m1
        self.a1 = a1
        self.l2 = l2
        self.m2 = m2
        self.a2 = a2
        self.pos1 = [l1 * np.sin(a1), -l1 * np.cos(a1)]
        self.v1 = [0, 0]
        self.pos2 = [self.pos1[0] + l2 * np.sin(a2), self.pos1[1] - l2 * np.cos(a2)]
        self.v2 = [0, 0]
        self.y = []

    def plot_isoda(self, maxt, dt):
        self.y = odeint(self.derive, np.array([self.a1, 0, self.a2, 0]), np.arange(0, maxt + dt, dt))
        f = []
        for th1, th1d, th2, th2d in self.y:
            pos1 = (self.l1 * np.sin(th1), -self.l1 * np.cos(th1))
            pos2 = (pos1[0] + self.l2 * np.sin(th2), pos1[1] - self.l2 * np.cos(th2))
            f.append((pos1, pos2))
        return f

    def derive(self, y, t): # Get derivatives of y (an array of [theta1, theta1dot, theta2, theta2dot]
        th1, z1, th2, z2 = y
        th1d, th2d = z1, z2
        c, s = np.cos(th1 - th2), np.sin(th1 - th2)

        z1d = (self.m2 * g * np.sin(th2) * c - self.m2 * s * (self.l1 * (z1**2) * c + self.l2 * (z2 ** 2)) - (self.m1 + self.m2) * g * np.sin(th1)) / (self.l1 * (self.m1 + self.m2 * (s ** 2)))
        z2d = ((self.m1 + self.m2) * (self.l1 * (z1 ** 2) * s - g * np.sin(th2) + g * np.sin(th1) * c) + self.m2 * self.l2 * (z2 ** 2) * s * c)/(self.l2 * (self.m1 + self.m2 * (s ** 2)))

        return th1d, z1d, th2d, z2d

    def calc_e(self, y):
        th1, th1d, th2, th2d = y
        V = -(self.m1 + self.m2) * g * self.l1 * np.cos(self.a1) - self.m2 * g * self.l2 * np.cos(self.a2)
        T = 0.5 * self.m1 * (self.l1 ** 2) * (th1d ** 2) + 0.5 * self.m2 * ((self.l2 ** 2) * (th2d ** 2) + (self.l1 ** 2) * (th1d ** 2) + 2 * self.l1 * self.l2 * th1d * th2d * np.cos(th1 - th2))
        return V + T
    # def show(self):
    #     print(self.mass1.pos, self.mass1.get_a(), self.mass1.get_v())
    #     print(self.mass2.pos, self.mass2.get_a(), self.mass2.get_v())
    #     print('\n\n')

    # def get_pos(self):
    #     return self.mass1.pos, self.mass2.pos

# class Mass:
#     def __init__(self, m, x, y, a, anchor, d):
#         self.d = d
#         self.m = m
#         self.pos = [x, y]
#         self.anchor = anchor
#         self.a = a
#         self.o = 0
#
#     def get_v(self):
#         v = [self.o * self.d * m.sin(self.a), self.o * self.d * m.cos(self.a)]
#         return m.sqrt(v[0] **2 + v[1] **2)
#
#     def get_a(self):
#         if (self.pos[1]-self.anchor.pos[1]) == 0:
#             return m.pi / 2
#         return m.atan((self.pos[0] - self.anchor.pos[0]) / (self.pos[1] - self.anchor.pos[1]))
#
#     # def update_pos_verlet(self, ):
#
#     def update_pos(self, dt, fx=0, fy=0):
#         fx += -self.anchor.resolve_v()[0]
#         fy += -self.anchor.resolve_v()[1]
#         torque = (self.d * m.sin(self.a)) * (fy + self.m * g) + (self.d * m.cos(self.a) * fx)
#         alpha = torque / (self.m * (self.d**2))  # angular acceleration
#         self.a += self.o * dt  # New angle
#         self.o += (alpha * dt/ 2)  # New angular velocity
#         self.pos = [self.anchor.pos[0] + self.d * m.sin(self.a), self.anchor.pos[1] + self.d * m.cos(self.a)]
#
#     def get_f(self):
#         return self.m * self.d * (self.o ** 2)
#
#     def resolve_f(self):
#         return self.get_f() * m.sin(self.a), min(-self.get_f() * m.cos(self.a) + self.m * g, 0)
#
#     def resolve_v(self):
#         v = self.o * self.d
#         return v * m.cos(self.a), v * m.sin(self.a)