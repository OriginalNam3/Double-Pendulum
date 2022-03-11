from GUIClass import GUI
import numpy as np
import csv

# f = open('/Users/mingchauchan/Documents/Tonbridge/Physics/InvestigationDoublePendulum/Energy-TimeDoublePendulum.csv', 'w')
# writer = csv.writer(f)
sim = GUI(0.0001, 1, 1, np.radians(135), 1, 1, np.radians(135))
sim.dp_generate_frames(60)
sim.run(100)
# i = 0
# n = len(sim.p.y)
# while i < n:
#     print(i)
#     energy = sim.p.calc_e(sim.p.y[i])
#     writer.writerow((i * sim.dt * 1000, energy, sim.p.y[i][0], sim.p.y[i][1], sim.p.y[i][2], sim.p.y[i][3]))
#     i += 100
