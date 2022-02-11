import math as m
global g
g = 9.81
global e

class Mass:
    def __init__(self, m, x, y, a, anchor, d):
        self.d = d
        self.m = m
        self.pos = [x, y]
        self.anchor = anchor
        self.a = a
        self.o = 0

    def get_v(self):
        v = [self.o * self.d * m.sin(self.a), self.o * self.d * m.cos(self.a)]
        return m.sqrt(v[0] **2 + v[1] **2)

    def get_a(self):
        if (self.pos[1]-self.anchor.pos[1]) == 0:
            return m.pi / 2
        return m.atan((self.pos[0] - self.anchor.pos[0]) / (self.pos[1] - self.anchor.pos[1]))

    def update_pos(self, dt, fx=0, fy=0):
        fx += -self.anchor.resolve_v()[0]
        fy += -self.anchor.resolve_v()[1]
        torque = (self.d * m.sin(self.a)) * (fy + self.m * g) + (self.d * m.cos(self.a) * fx)
        alpha = torque / (self.m * (self.d**2))  # angular acceleration
        self.a += self.o * dt  # New angle
        self.o += (alpha * dt/ 2)  # New angular velocity
        self.pos = [self.anchor.pos[0] + self.d * m.sin(self.a), self.anchor.pos[1] + self.d * m.cos(self.a)]

    def get_f(self):
        return self.m * self.d * (self.o ** 2)

    def resolve_f(self):
        return self.get_f() * m.sin(self.a), min(-self.get_f() * m.cos(self.a) + self.m * g, 0)

    def resolve_v(self):
        v = self.o * self.d
        return v * m.cos(self.a), v * m.sin(self.a)


class DPendulum:
    def __init__(self, l1=0.5, m1=1, a1=m.radians(90), l2=1, m2=1, a2=m.radians(180)):
        # self.l1 = l1
        # self.m1 = m1
        # self.a1 = a1
        # self.l2 = l2
        # self.m2 = m2
        # self.a2 = a2
        self.mass1 = Mass(m1, m.sin(a1) * l1, m.cos(a1) * l1, a1, Mass(0, 0, 0, 0, None, 0), l1)
        self.mass2 = Mass(m2, self.mass1.pos[0] + (m.sin(a2) * l2), self.mass1.pos[1] + (m.cos(a2) * l2), a2, self.mass1,
                     l2)
        e = (m1 * (self.mass1.pos[1] + l1) + m2 * (self.mass2.pos[1] + l2)) * g

    def set_angle(self, a1, a2):
        self.a1 = m.radians(a1)
        self.a2 = m.radians(a2)

    def update(self, dt):
        fx, fy = self.mass2.resolve_f()
        self.mass1.update_pos(dt, fx, fy)
        fx, fy = self.mass2.resolve_f()
        self.mass2.update_pos(dt)
        self.show()

    def show(self):
        print(self.mass1.pos, self.mass1.get_a(), self.mass1.get_v())
        print(self.mass2.pos, self.mass2.get_a(), self.mass2.get_v())
        print('\n\n')

    # def get_pos(self):
    #     return self.mass1.pos, self.mass2.pos
