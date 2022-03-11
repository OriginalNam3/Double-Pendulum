import numpy as np
global g
g = 9.81
global e

class DPendulum:
    def __init__(self, l1=1, m1=1, a1=np.radians(90), l2=1, m2=1, a2=np.radians(90)):
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
        self.y = [[a1, 0, a2, 0]]

    def RK4(self, y, dt):
        th1, th1d, th2, th2d = y
        k1 = self.derive(y)
        hdt = dt/2
        k2 = self.derive((th1 + hdt * k1[0], th1d + hdt * k1[1], th2 + hdt * k1[2], th2d + hdt * k1[3]))
        k3 = self.derive((th1 + hdt * k2[0], th1d + hdt * k2[1], th2 + hdt * k2[2], th2d + hdt * k2[3]))
        k4 = self.derive((th1 + dt * k3[0], th1d + dt * k3[1], th2 + dt * k3[2], th2d + dt * k3[3]))
        return [y[i] + dt * ((k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])/6) for i in range(4)]

    def generate_RK4(self, maxt, dt):
        for i in range(int(maxt/dt)):
            cy = self.y[i]
            print(cy)
            self.y.append(self.RK4(cy, dt))
        # self.y = odeint(self.derive, np.array([self.a1, 0, self.a2, 0]), np.arange(0, maxt + dt, dt))

    def euler(self, y, dt):
        th1, th1d, th2, th2d = y
        th1d, th1dd, th2d, th2dd = self.derive(y)
        return th1 + dt * th1d, th1d + dt * th1dd, th2 + dt * th2d, th2d + dt * th2dd

    def generate_euler(self, maxt, dt):
        for i in range(int(maxt/dt)):
            self.y.append(self.euler(self.y[i], dt))

    def plot(self):
        f = []
        for th1, th1d, th2, th2d in self.y:
            pos1 = (self.l1 * np.sin(th1), -self.l1 * np.cos(th1))
            pos2 = (pos1[0] + self.l2 * np.sin(th2), pos1[1] - self.l2 * np.cos(th2))
            f.append((pos1, pos2))
        return f

    def derive(self, y):  # Get derivatives of y (an array of [theta1, theta1dot, theta2, theta2dot]
        th1, th1d, th2, th2d = y
        c, s = np.cos(th1 - th2), np.sin(th1 - th2)

        th1dd = (self.m2 * g * np.sin(th2) * c - self.m2 * s * (self.l1 * (th1d**2) * c + self.l2 * (th2d ** 2)) - (self.m1 + self.m2) * g * np.sin(th1)) / (self.l1 * (self.m1 + self.m2 * (s ** 2)))
        th2dd = ((self.m1 + self.m2) * (self.l1 * (th1d ** 2) * s - g * np.sin(th2) + g * np.sin(th1) * c) + self.m2 * self.l2 * (th2d ** 2) * s * c)/(self.l2 * (self.m1 + self.m2 * (s ** 2)))

        return th1d, th1dd, th2d, th2dd

    def calc_e(self, y):
        th1, th1d, th2, th2d = y
        V = -((self.m1 + self.m2) * g * self.l1 * np.cos(self.a1)) - (self.m2 * g * self.l2 * np.cos(self.a2))
        T = 0.5 * self.m1 * (self.l1 ** 2) * (th1d ** 2) + 0.5 * self.m2 * ((self.l2 ** 2) * (th2d ** 2) + (self.l1 ** 2) * (th1d ** 2) + 2 * self.l1 * self.l2 * th1d * th2d * np.cos(th1 - th2))
        return V + T

class SPendulum:
    def __init__(self, l=1, m=1, a=np.radians(90)):
        self.l = l
        self.m = m
        self.a = a
        self.y = [(a, 0)]

    def derive(self, y, dt):
        th1, th1d = y  # Gets angle and omega
        alpha = (-g * np.sin(th1)) / self.l  # gets alpha
        return th1d + (alpha * dt)  # The Euler method is applied to return new velocity

    def euler_solve(self, maxt, dt):
        for i in range(int(maxt / dt)):
            th1, th1d = self.y[i]  # Get angle and omega from last frame
            nth1d = self.derive(self.y[i], dt)  # Gets new omega
            self.y.append((th1 + (th1d * dt), nth1d))  # Adds new frame

    def oscillator_sim(self, maxt, dt):
        for i in range(int(maxt / dt)):
            nth = self.a * np.cos(np.sqrt(g/self.l) * i * dt)
            nthd = - self.a * np.sqrt(g/self.l) * np.sin(np.sqrt(g/self.l) * i * dt)
            self.y.append((nth, nthd))

    def plot(self):
        f = []
        for th1, th1d in self.y:
            f.append((self.l * np.sin(th1), - self.l * np.cos(th1)))
        return f

    def calc_e(self, y):
        th1, th1d = y
        return self.m * g * (-np.cos(th1)) + 0.5 * self.m * ((self.l * th1d) ** 2)
