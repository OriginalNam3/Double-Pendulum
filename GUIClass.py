import tkinter as tk
from PendulumClass import *

class GUI:
    def __init__(self, w=1000, h=700):
        self.w = w
        self.h = h
        self.r = 20
        self.sf = w//6
        self.dt = 0.005
        self.p = DPendulum()
        self.root = tk.Tk()
        self.display = tk.Canvas(self.root, width=w, height=h)
        self.display.pack()
        self.root.after(int(self.dt * 10), self.run)
        self.root.mainloop()

    def update(self):
        self.display.delete('all')
        self.display.create_line(self.p.mass1.anchor.pos[0] * self.sf + self.w // 2,
                                 -self.p.mass1.anchor.pos[1] * self.sf + self.h // 2,
                                 self.p.mass1.pos[0] * self.sf + self.w // 2,
                                 -self.p.mass1.pos[1] * self.sf + self.h // 2,
                                 width=self.r // 2, fill='black')
        self.display.create_line(self.p.mass2.anchor.pos[0] * self.sf + self.w // 2,
                                 -self.p.mass2.anchor.pos[1] * self.sf + self.h // 2,
                                 self.p.mass2.pos[0] * self.sf + self.w // 2,
                                 -self.p.mass2.pos[1] * self.sf + self.h // 2,
                                 width=self.r // 2, fill='black')
        self.display.create_oval(self.p.mass1.pos[0] * self.sf + self.w // 2 - self.r,
                                 -self.p.mass1.pos[1] * self.sf + self.h // 2 - self.r,
                                 self.p.mass1.pos[0] * self.sf + self.w // 2 + self.r,
                                 -self.p.mass1.pos[1] * self.sf + self.h // 2 + self.r,
                                 fill='red')
        self.display.create_oval(self.p.mass2.pos[0] * self.sf + self.w // 2 - self.r,
                                 -self.p.mass2.pos[1] * self.sf + self.h // 2 - self.r,
                                 self.p.mass2.pos[0] * self.sf + self.w // 2 + self.r,
                                 -self.p.mass2.pos[1] * self.sf + self.h // 2 + self.r,
                                 fill='red')

    def run(self):
        self.p.update(self.dt)
        self.update()
        self.root.update()
        self.root.after(1, self.run)