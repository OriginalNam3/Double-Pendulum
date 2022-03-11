# Double-Pendulum
Physics Investigation

I used Object Oriented Programming.

The classes are: 
DPendulum(l_1, m_1, theta_1, l_2, m_2, theta_2), SPendulum(l, m, theta)
Functions include: 

DPendulum: 

state = [theta1, theta1dot, theta2, theta2dot]

Functions:
derive(state): returns derivative of state
RK4(state, dt): returns next state using the Runge-Kutta fourth order method
euler(state, dt): returns next state using the Euler method
generate_RK4(maxt, dt): Generate all frames over a time period with time step of dt using RK4(dt)
generate_euler(maxt, dt): Generate all frames over a time period with time step of dt using euler(dt)
plot(): returns list of cartisian coordinates translated from all frames generated
calc_e(state): returns total energy in a particular state

SPendulum: 

state = [theta, thetadot]

Functions:
derive(state): returns derivative of state
euler_solve(maxt, dt): Generate all frames over a time period with time step of dt using the Euler method
oscillator_sim(maxt, dt): Generate all frames over a time period with time step of dt using the model of a harmonic oscillator
plot(): returns list of cartesian coordinates translated from all frames generated
calc_e(state): returns total energy in the state
