import tkinter as tk
from PendulumClass import *

class GUI:
    def __init__(self, dt=0.0001, l1=1, m1=1, a1=np.radians(90), l2=1, m2=1, a2=np.radians(90), w=1000, h=700):
        self.w = w
        self.h = h
        self.r = 20
        self.sf = w//6
        self.dt = dt
        self.p = DPendulum(l1, m1, a1, l2, m2, a2)
        self.root = tk.Tk()
        self.display = tk.Canvas(self.root, width=w, height=h)
        self.display.pack()
        self.fi = 0
        self.f = []

    def update(self, pos1, pos2):
        self.display.delete('all')
        self.display.create_line(self.w // 2,
                                 self.h // 2,
                                 pos1[0] * self.sf + self.w // 2,
                                 -pos1[1] * self.sf + self.h // 2,
                                 width=self.r // 2, fill='cyan')
        self.display.create_line(pos1[0] * self.sf + self.w // 2,
                                 -pos1[1] * self.sf + self.h // 2,
                                 pos2[0] * self.sf + self.w // 2,
                                 -pos2[1] * self.sf + self.h // 2,
                                 width=self.r // 2, fill='pink')
        self.display.create_oval(pos1[0] * self.sf + self.w // 2 - self.r,
                                 -pos1[1] * self.sf + self.h // 2 - self.r,
                                 pos1[0] * self.sf + self.w // 2 + self.r,
                                 -pos1[1] * self.sf + self.h // 2 + self.r,
                                 fill='blue')
        self.display.create_oval(pos2[0] * self.sf + self.w // 2 - self.r,
                                 -pos2[1] * self.sf + self.h // 2 - self.r,
                                 pos2[0] * self.sf + self.w // 2 + self.r,
                                 -pos2[1] * self.sf + self.h // 2 + self.r,
                                 fill='red')

    def run(self, fps):
        self.f = self.p.plot()
        self.start(fps)
        self.root.mainloop()

    def start(self, fps, t=0):
        pos1, pos2 = self.f[self.fi]
        self.fi += int((1/fps)/self.dt)
        # print(self.p.calc_e(self.p.y[self.fi]))
        # print(pos1, pos2)
        # print(self.p.calc_e(self.p.y[int(t / dt)]))
        self.update(pos1, pos2)
        if int(t/self.dt) < len(self.f)-1:
            self.root.after(int(1000/fps), self.start, fps, t + 1/fps)
