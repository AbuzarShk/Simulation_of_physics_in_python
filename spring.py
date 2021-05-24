from vpython import *

class Spring():
    def __init__(self,KS=10.0,LO=1.0,MA=1.0,G=0.1):
        nrg = gcurve(color=color.red)

        topball = sphere(pos=vector(0,0,0),
               radius=0.1,
               color=color.blue)

        middleball  = sphere(#pos=vector(.71,-.71,0),
                pos=vector(0.5,-0.833,0),
               radius=0.1, 
               color=color.red)

        spring = helix(pos=topball.pos,
               axis=middleball.pos-topball.pos,
               radius=0.1, 
               color=color.white,
               thickness=0.05)
        middlevel = vector(0,0,0)

        bottomball  = sphere(pos=vector(2*.71,-2*.71,0),
               radius=0.1, 
               color=color.green)

        spring2 = helix(pos=middleball.pos,
               axis=bottomball.pos-middleball.pos,
               radius=0.1, 
               color=color.white,
               thickness=0.05)
        bottomvel = vector(0,0,0)

        ks = KS # Spring stiffness.
        L0 = LO # Spring's natural length.
        mass = MA # Mass of each ball.
        grav = G # Gravitational field.

        dt = 0.001 # Time step.
        t = 0 # Initialize.

        while( t<= 5):
            rate(10000)

            L = middleball.pos-topball.pos
            Lhat = L/mag(L) # Calculate spring direction.
            s = mag(L) - L0 # Amount the spring has been stretched or compressed by.
            F_spring = -ks*s*Lhat # Calculate spring force.

            L2 = bottomball.pos-middleball.pos
            Lhat2 = L2/mag(L2) # Calculate spring direction.
            s2 = mag(L2) - L0 # Amount the spring has been stretched or compressed by.
            F_spring2 = -ks*s2*Lhat2 # Calculate spring force.

            F_grav   = -mass*grav*vector(0,1,0) #Calculate the gravitational force (weight).

            energy = 0.5*mass*mag(middlevel)**2 + 0.5*mass*mag(bottomvel)**2 + 0.5*ks*s**2 + 0.5*ks*s2**2 + mass*grav*middleball.pos.y + mass*grav*bottomball.pos.y

#    nrg.plot(pos=(t,energy))
#    nrg.plot(pos=(atan(spring2.axis.x/spring2.axis.y),atan(spring.axis.x/spring.axis.y)))
            nrg.plot(pos=(mag(spring.axis),atan(spring.axis.x/spring.axis.y)))

            force = F_spring + F_grav - F_spring2 # Total force on middleball.
            force2 = F_spring2 + F_grav # Total force on bottomball.

            middlevel = middlevel + force/mass*dt # Update velocity.
            middleball.pos = middleball.pos + middlevel*dt   # Update position.
            bottomvel = bottomvel + force2/mass*dt # Update velocity.
            bottomball.pos = bottomball.pos + bottomvel*dt   # Update position.
            spring.axis = middleball.pos-topball.pos    # Update spring axis.
            spring2.axis = bottomball.pos-middleball.pos
            spring2.pos = middleball.pos

            t = t + dt
