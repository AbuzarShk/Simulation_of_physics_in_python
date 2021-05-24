from vpython import *

class Projectile():
    def __init__(self,S = 3.2,A = 75,M = 1.0):
        projectile = sphere(pos = vector(-5,0,0),radius = 0.1,color = color.red,make_trail = True)

        projectile.speed = S # Initial speed.
        projectile.angle = A*3.141459/180 # Initial angle, from the +x-axis.

        projectile.velocity = vector(projectile.speed*cos(projectile.angle),
                             projectile.speed*sin(projectile.angle),
                             0)

        projectile.mass = M
        grav_field = 1.0

        dt = 0.01
        time = 0

        while (projectile.pos.y >=0):
            rate(100)

    # Calculate the force.
            grav_force = vector(0,-projectile.mass*grav_field,0)

            force = grav_force
    
    # Update velocity.
            projectile.velocity = projectile.velocity + force/projectile.mass * dt

    # Update position.
            projectile.pos = projectile.pos + projectile.velocity * dt

    # Update time.
            time = time + dt

