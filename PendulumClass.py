import math as m
global g
g = 9.81

class Anchor():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Mass:
    def __init__(self, m, x, y, anchor, d, vx=0, vy=0):
        self.d = d
        self.m = m
        self.pos = [x, y]
        self.anchor = anchor
        self.v = [vx, vy]

    def update_pos(self, fx, fy, dt):
        a = m.atan(self.anchor.x / self.anchor.y)
        ft = (self.m * g + fy) * m.sin(a) - fx * m.cos(a)
        ft *= self.d
        alpha = ft / (self.m * (self.d **2))
        vr = m.sqrt(self.v[0] **2 + self.v[1] **2) + alpha * dt
        na = a * (1 - vr * dt / a * self.d)
        self.pos = [self.d * m.sin(na), self.d * m.cos(na)]
        self.v = [vr * m.sin(na), vr * m.cos(na)]

class Pendulum:
    def __init__(self, l1=1, m1=1, a1=m.radians(90), l2=1, m2=1, a2=m.radians(90)):
        self.l1 = l1
        self.m1 = m1
        self.a1 = a1
        self.l2 = l2
        self.m2 = m2
        self.a2 = a2
        mass1 = Mass(self.m1, m.cos(self.a1) * self.l1, m.sin(self.a1) * self.l1, Anchor(0, 0), self.l1)
        mass2 = Mass(self.m2, mass1.pos[0] + m.cos(self.a2) * self.l2, mass1.pos[1] + m.sin(self.a2) * self.l2, mass1,
                     self.l2)

    def set_angle(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def update(self, t):

