from vpython import *


class Pendulum():
    def __init__(self, M=1.0, l=0.25, d=0.1):

        def thetaDoubleDot(theta, thetaDot, g, l):
            thetaDoubleDot = -g / l * sin(theta)
            return thetaDoubleDot

        # Set initial conditions and constants.
        theta = 0.5
        thetaDot = 0.0
        mass = M
        l = l
        g = 9.8

        # Create pendulum bob.
        x = l*sin(theta)
        y = -l*cos(theta)

        bob = sphere(pos=vector(x, y, 0), radius=0.05 *
                     l, color=color.red, make_trail=True)

    #    Create pendulum arm.
        arm = cylinder(pos=vector(0, 0, 0), axis=bob.pos,
                       color=color.white, size=vector(l, 0.02*l, 0.02*l))

    # Animate.
        # Time step. Smaller is more accurate but more computationally intensive.
        dt = 0.01
        time = 0.0
        while (time <= 5):  # Set maximum time for animation.
            rate(1.0 / dt)  # Set animation rate.

            # Calculate thetaDoubleDot.
            tdd = thetaDoubleDot(theta, thetaDot, g, l)

            thetaDot += tdd*dt  # Update thetaDot.
            thetaDot -= 0.01
            theta += thetaDot*dt  # Update theta.

    # Update graphics.
            x = l*sin(theta)
            y = -l*cos(theta)
            bob.pos = vector(x, y, 0)
            arm.axis = bob.pos

            time += dt  # Update time.
