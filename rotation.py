from vpython import*

class Rotation():
    def __init__(self,Radius , X , Y , Z , O ):
        atoms = []
        omega_graph = gcurve(color=color.red)

        # Set radius and mass.
        R = Radius
        M = 1

        # Make a ring.
        z = 0
        theta = 0
        ds = 0.1 # Fixed distance between atoms.
        while (theta < 2*pi):
            atoms.append( simple_sphere(
                pos=vector(R*cos(theta),R*sin(theta),z),
                color=color.red, radius=0.05) )
            theta = theta + ds/R

        # Draw rotation axis.
        rot_axis = cylinder(pos=vector(0,0,0),
                            axis=vector(X,Y,Z),size=vector(2,0.05,0.05))
        rot_axis.pos -= rot_axis.size.x*hat(rot_axis.axis)/2

        # Set a marker.
        atoms[0].color = color.white
        # Merge atoms into one object.
        shape = compound(atoms)

        # Begin rotation.
        dt = 0.01
        t = 0
        shape.omega = O*hat(rot_axis.axis)
        shape.alpha = 1.0*hat(rot_axis.axis)
        while(t <= 10):
            rate(50)
            # Update angular velocity.
            shape.omega = shape.omega + shape.alpha*dt
            shape.rotate(angle=mag(shape.omega)*dt,axis=shape.omega.hat)
            # Here is where you can graph magnitude of omega vs. t!

            t = t + dt