
from vpython import *


class Rocket():
    def __init__(self, RM=100.0, FM=10.0, V=100):

        rocket_parts = []
        height = 0.5
        rocket_parts.append(cylinder(pos=vector(0, 0, 0), color=color.red, size=vector(
            height, 0.1, 0.1), axis=vector(0, 1, 0), make_trail=True))

        rocket_parts.append(cone(pos=rocket_parts[0].pos+rocket_parts[0].size.x*rocket_parts[0].axis*2, color=color.red,
                                 size=vector(
            rocket_parts[0].size.y, rocket_parts[0].size.y, rocket_parts[0].size.y),
            axis=vector(0, 1, 0)))
        rocket_parts.append(triangle(v0=vertex(pos=rocket_parts[0].pos+0.5*rocket_parts[0].size.y*vector(1, 0, 0), color=color.red),
                                     v1=vertex(
            pos=rocket_parts[0].pos+1.5*rocket_parts[0].size.y*vector(1, 0, 0), color=color.red),
            v2=vertex(pos=rocket_parts[0].pos+0.5*rocket_parts[0].size.y*vector(1, 2, 0), color=color.red)))
        rocket_parts.append(triangle(v0=vertex(pos=rocket_parts[0].pos+0.5*rocket_parts[0].size.y*vector(-1, 0, 0), color=color.red),
                                     v1=vertex(
            pos=rocket_parts[0].pos+1.5*rocket_parts[0].size.y*vector(-1, 0, 0), color=color.red),
            v2=vertex(pos=rocket_parts[0].pos+0.5*rocket_parts[0].size.y*vector(-1, 2, 0), color=color.red)))
        rocket_parts.append(triangle(v0=vertex(pos=rocket_parts[0].pos+0.5*rocket_parts[0].size.y*vector(0, 0, 1), color=color.red),
                                     v1=vertex(
            pos=rocket_parts[0].pos+1.5*rocket_parts[0].size.y*vector(0, 0, 1), color=color.red),
            v2=vertex(pos=rocket_parts[0].pos+0.5*rocket_parts[0].size.y*vector(0, 2, 1), color=color.red)))
        rocket_parts.append(triangle(v0=vertex(pos=rocket_parts[0].pos+0.5*rocket_parts[0].size.y*vector(0, 0, -1), color=color.red),
                                     v1=vertex(
            pos=rocket_parts[0].pos+1.5*rocket_parts[0].size.y*vector(0, 0, -1), color=color.red),
            v2=vertex(pos=rocket_parts[0].pos+0.5*rocket_parts[0].size.y*vector(0, 2, -1), color=color.red)))

        rocket = compound(rocket_parts, pos=vector(0, 0, 0))
        rocket.velocity = vector(0, 0, 0)
        rocket.mass = RM
        rocket.fuel_mass = FM
        attach_trail(rocket)

        initial_mass = rocket.mass + rocket.fuel_mass
        initial_fuel_mass = rocket.fuel_mass

        graph(fast=True)
        r_pos = gcurve(color=color.red)

        exhaust_velocity = vector(0, -V, 0)
        mdot = 1.0  # Rate of mass loss per time.
        dt = 0.001
        t = 0
        scene.camera.follow(rocket)

        earth = []
        earth.pos = vector(0, -height*100, 0)
        earth.mass = 1000

        ground = box(pos=vector(0, -height/2-0.05, 0),
                     color=vector(0.8, 0.8, 0.8), size=vector(2, 0.01, 2))
        grav = -1*earth.mass/earth.pos.y**2

        while (rocket.fuel_mass > 0):
            rate(10000)
            dm = mdot*dt  # Amount of mass lost in time dt.
            if (rocket.pos.y > 0):
                force = (rocket.mass+rocket.fuel_mass)*vector(0, grav, 0)
                
            else:
                     force = vector(0, 0, 0)
            rocket.velocity = rocket.velocity + dm/(rocket.mass+rocket.fuel_mass)*(-exhaust_velocity) + force/(rocket.mass+rocket.fuel_mass)*dt
            rocket.pos = rocket.pos + rocket.velocity*dt
            rocket.fuel_mass = rocket.fuel_mass - dm
            rocket.opacity = rocket.fuel_mass/initial_fuel_mass
            t = t + dt
            r_pos.plot(pos=(t,rocket.pos.y))


        print((1-rocket.velocity.y/(mag(exhaust_velocity)*log(initial_mass/rocket.mass)))
              * 100, "% decrease in speed due to external forces")
