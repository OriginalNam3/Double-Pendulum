from GUIClass import GUI
import numpy as np
import csv

f = open('/Users/mingchauchan/Documents/Tonbridge/Physics/InvestigationDoublePendulum/EnergyTimeNormal.csv', 'w')
writer = csv.writer(f)
# worksheet.write('A1', 'Energy/ J')
# worksheet.write('B1', 'Time/ ms')
sim = GUI(0.0001, 1, 1, np.radians(135), 1, 1, np.radians(135))
sim.p.generate_lsoda(300, sim.dt)
i = 0
n = len(sim.p.y)
while i < n:
    energy = sim.p.calc_e(sim.p.y[i])
    writer.writerow((energy, i * sim.dt * 1000))
    i += 100
sim.run(100)
