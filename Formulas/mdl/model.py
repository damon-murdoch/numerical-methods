import matplotlib.pyplot as plt
import math

import numpy


def unconstrained_growth(len, pop, rate, ct, st):
    dp = []
    dt = []
    for i in range(st, len, 1):
        growth = rate * pop
        pop += (growth * ct)
        t = i * ct
        dp.append(pop)
        dt.append(t)
    return dt, dp


def constrained_growth(len, pop, rate, C, ct, st):
    dp = []
    dt = []
    dt.append(st)
    dp.append(pop)
    for i in range(st + 1, len, 1):
        growth = dp[i - 1] * rate * ((C - dp[i - 1]) / C)
        pop += growth
        t = i * ct
        dp.append(pop)
        dt.append(t)
    return dt, dp


def aspirin_single_dose(half_life=3.2, plasma_vol=3000, init_aspirin_in_plasma=2 * 325 * 1000, sim_hours=8,
                        delta_x=5 / 60):
    num_iterations = int(8 * 60 / 5)
    print(num_iterations)
    elim_const = -math.log(0.5) / half_life
    aspirin_in_plasma = list()
    plasma_conc_lst = list()
    time = list()
    aspirin_in_plasma.append(init_aspirin_in_plasma)
    plasma_conc_lst.append(aspirin_in_plasma[-1] / plasma_vol)
    time.append(0)
    for i in range(1, num_iterations):
        time.append(i * delta_x)
        elim = (elim_const * aspirin_in_plasma[-1]) * delta_x
        aspirin_in_plasma.append(aspirin_in_plasma[-1] - elim)
        plasma_conc = aspirin_in_plasma[-1] / plasma_vol
        plasma_conc_lst.append(plasma_conc)
    return aspirin_in_plasma, plasma_conc_lst, time


def drug_dosage_repeated(mec=10, mtc=20, halfLife=22, volume=3000, dosage=100 * 1000, absorpFract=0.12, interval=8,
                         simHrs=168, deltaX=2 / 60):
    def xtoi(x):
        return x / deltaX + 1

    def itox(i):
        return (i - 1) * deltaX

    elimconst = -math.log(0.5) / halfLife
    drugInSystem = [absorpFract * dosage]
    time = [0]

    numiterations = int(simHrs / deltaX)

    conc = [drugInSystem[-1] / volume]

    for i in range(1, numiterations):
        time.append(i * deltaX)
        if itox(i) % interval == 0:
            ingested = absorpFract * dosage
        else:
            ingested = 0
        eliminated = (elimconst * drugInSystem[-1] * deltaX)
        drugInSystem.append(drugInSystem[-1] + ingested - eliminated)
        conc.append(drugInSystem[-1] / volume)
    return drugInSystem, conc, time


def competition_model(Ps=110, Pj=150, DCs=0.03, DCj=0.06, BCs=0.03, BCj=0.03, sim_mnth=36, delta_x=1):
    p_s = [Ps]
    p_j = [Pj]
    time = [0]

    num_iterations = int(sim_mnth / delta_x)

    for i in range(1, num_iterations):
        time.append(i * delta_x)
        p_s.append(p_s[-1] * (1 + BCs) * (1 - DCs * (p_j[-1] / p_s[-1])))
        p_j.append(p_j[-1] * (1 + BCj) * (1 - DCj * (p_s[-1] / p_j[-1])))

    return p_s, p_j, time


def predator_prey(alpha=1, beta=1.2, gamma=4, delta=1, T=15.0, dt=0.01, x0=10, y0=2, t0=0):
    def euler_step(u, f, dt):
        return u + dt * f(u)

    def f(u):
        x = u[0]
        y = u[1]
        return numpy.array([x * (alpha - beta * y), -y * (gamma - delta * x)])

    N = int(T / dt) + 1  # number of time steps

    u_euler = numpy.empty((N, 2))

    u_euler[0] = numpy.array([x0, y0])

    for n in range(N - 1):
        u_euler[n + 1] = euler_step(u_euler[n], f, dt)

    time = numpy.linspace(0.0, T, N)
    x_euler = u_euler[:, 0]
    y_euler = u_euler[:, 1]

    plt.plot(time, x_euler, label='prey ')
    plt.plot(time, y_euler, label='predator ')
    plt.legend(loc='upper right')
    plt.xlabel("time")
    plt.ylabel("number of each species")
    plt.title("predator prey model")
    plt.show()

    plt.plot(x_euler, y_euler, '-->', markevery=5, label='phase plot')
    plt.legend(loc='upper right')
    # labels
    plt.xlabel("number of prey")
    plt.ylabel("number of predators")
    # title
    plt.title("predator prey model")
    plt.show()


def ball_falling(mass=0.5, adtg=-9.81, radius=0.05, p=400, v=0, T=60, dt=0.001):
    weight = mass * adtg
    projected_area = 3.14159 * radius

    num_iterations = int(T / dt)

    velocity = [v]
    position = [p]
    time = [0]

    for i in range(1, num_iterations):
        time.append(i * dt)
        air_friction = -0.65 * projected_area * velocity[-1] * abs(velocity[-1])
        total_force = weight + air_friction
        acceleration = total_force / mass
        delta_velocity = acceleration
        delta_position = velocity[-1]
        speed = abs(velocity[-1])
        velocity.append(velocity[-1] + delta_velocity * dt)
        position.append(position[-1] + delta_position * dt)
        if position[-1] < 0: break

    return velocity, position, time


def sky_dive(mass=80, height=2500, height_open=700, DT=0.001, T=200):
    velocity = 0
    num_iterations = int(T / DT)
    adtg = -9.81
    weight = mass * adtg
    projected_area = 28
    air_friction = -0.65 * projected_area * velocity * abs(velocity)
    total_force = weight + air_friction
    acceleration = total_force / mass
    change_in_velocity = acceleration
    change_in_height = velocity
    s_lst = [0]
    t_lst = [0]
    h_lst = [height]

    # print(len(s_lst),len(t_lst),len(h_lst))

    for i in range(1, num_iterations):
        velocity = velocity + change_in_velocity * DT
        speed = abs(velocity)
        height = height + change_in_height * DT
        if height < 0:
            break
        s_lst.append(speed)
        h_lst.append(height)
        t_lst.append(i * DT)
        if (height > height_open):
            projected_area = 0.4
        else:
            projected_area = 28

        air_friction = -0.65 * projected_area * velocity * abs(velocity)
        total_force = weight + air_friction
        acceleration = total_force / mass
        change_in_height = velocity
        change_in_velocity = acceleration

        # print(len(s_lst), len(t_lst), len(h_lst))

    return s_lst, h_lst, t_lst


def sky_dive(mass=80, height=3048, height_open=700, DT=0.001, T=200):
    sea_level_density = 1225  # g/m^3

    air_density = (1225 / 100) * 73.8

    adpercent = ((100 - 73.8) / (0 - 3048))

    print(adpercent)

    velocity = 0
    num_iterations = int(T / DT)
    adtg = -9.81
    weight = mass * adtg
    projected_area = 28
    air_friction = -0.65 * projected_area * velocity * abs(velocity) * air_density
    total_force = weight + air_friction
    acceleration = total_force / mass
    change_in_velocity = acceleration
    change_in_height = velocity
    s_lst = [0]
    t_lst = [0]
    h_lst = [height]

    for i in range(1, num_iterations):
        velocity = velocity + change_in_velocity * DT
        speed = abs(velocity)
        height = height + change_in_height * DT
        if height < 0:
            break
        s_lst.append(speed)
        h_lst.append(height)
        t_lst.append(i * DT)
        if (height > height_open):
            projected_area = 0.4
        else:
            projected_area = 28

        air_density -= adpercent
        air_friction = -0.65 * projected_area * velocity * abs(velocity) * air_density
        total_force = weight + air_friction
        acceleration = total_force / mass
        change_in_height = velocity
        change_in_velocity = acceleration

    return s_lst, h_lst, t_lst


def spring_model(spring_const=10, weight=0.2, init_displacement=0.3, unweighted_length=1.2, T=60, dt=0.5):
    num_iterations = int(T / dt)

    adtg = 9.81

    mass = weight / -adtg

    weight_displacement = -weight / spring_const

    length = unweighted_length + weight_displacement + init_displacement

    restoring_spring_force = -spring_const * (length - unweighted_length)

    total_force = restoring_spring_force + weight

    acceleration = mass * total_force

    v_t = [0.0]
    v_v = [0.0]
    v_l = [length]

    for i in range(1, num_iterations):
        change_in_velocity = v_t[-1] - acceleration
        length = v_l[-1] - change_in_velocity
        restoring_spring_force = -spring_const * (length - unweighted_length)
        v_l.append(length)
        v_v.append(change_in_velocity)
        v_t.append(i * dt)

    return v_v, v_l, v_t


def rocket_model(c, v):
    pass
    # T = c(dm/dt)


if __name__ == "__main__":
    # predator_prey()
    b = spring_model()
    plt.plot(b[2], b[1])
    plt.show()
    plt.plot(b[2], b[0])
    plt.show()
    pass
