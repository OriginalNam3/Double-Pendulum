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
        self.p2 = DPendulum(l1, m1, a1, l2, m2, a2)
        self.sp = SPendulum(l1, m1, a1)
        self.root = tk.Tk()
        self.display = tk.Canvas(self.root, width=w, height=h)
        self.display.pack()
        self.fi = 0
        self.f = []
        self.f2 = []
        self.fs = []

    def update(self, pos1, pos2):
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

    def dp_generate_frames(self, maxt):
        self.p.generate_RK4(maxt, self.dt)
        self.f = self.p.plot()

    def run(self, fps):
        self.start(100)
        self.root.mainloop()

    def start(self, fps, t=0):
        pos1, pos2 = self.f[int(t/self.dt)]
        # print(pos1, pos2)
        # print(self.p.calc_e(self.p.y[self.fi]))
        # print(pos1, pos2)
        # print(self.p.calc_e(self.p.y[int(t / dt)]))
        self.display.delete('all')
        self.update(pos1, pos2)
        if int((t + 1/fps) / self.dt) < len(self.fs) - 1:
            self.root.after(int(1000/fps), self.start, fps, t + (1/fps))

    def two_generate_frames(self, maxt):
        self.p2.generate_euler(maxt, self.dt)
        self.f2 = self.p2.plot()

    def tworun(self, fps):
        self.twostart(fps)
        self.root.mainloop()

    def twostart(self, fps, t=0):
        pos1, pos2 = self.f[int(t/self.dt)]
        pos3, pos4 = self.f2[int(t/self.dt)]
        self.display.delete('all')
        self.update(pos1, pos2)
        self.update(pos3, pos4)
        if int((t + 1/fps) / self.dt) < len(self.fs) - 1:
            self.root.after(int(1000 / fps), self.twostart, fps, t + 1 / fps)

    def sp_generate_frames(self, maxt):
        self.sp.oscillator_sim(maxt, self.dt)
        self.fs = self.sp.plot()

    def singlerun(self, fps):
        self.singlestart(fps)
        self.root.mainloop()

    def singlestart(self, fps, t=0):
        pos1 = self.fs[int(t/self.dt)]
        print(pos1)
        self.display.delete('all')
        self.update(pos1, pos1)
        if int((t + 1/fps) / self.dt) < len(self.fs) - 1:
            print(int(1000/fps), t + (1/fps))
            self.root.after(int(1000 / fps), self.singlestart, fps, t + (1/fps))
