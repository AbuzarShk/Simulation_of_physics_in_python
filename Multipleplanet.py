from vpython import *


class Multileplanet():
        def __init__(self,P1 = 1, P2 = 2, P3 = 10):
                self.P1 = P1
                self.P2 = P2
                self.P3 = P3
                
                def gforce(p1,p2):
                        G = 1 
                        r_vec = p1.pos-p2.pos
                        r_mag = mag(r_vec)
                        r_hat = r_vec/r_mag
                        force_mag = G*p1.mass*p2.mass/r_mag**2
                        force_vec = -force_mag*r_hat
                        return force_vec
    
                star = sphere( pos=vector(0,0,0), radius=0.2, color=color.yellow,mass = 1000, momentum=vector(0,0,0), make_trail=True)
               
                planet1 = sphere( pos=vector(1,0,0), radius=0.05, color=color.blue,mass = P1, momentum=vector(0,30,0), make_trail=True )

                planet2 = sphere( pos=vector(0,3,0), radius=0.075, color=color.red,mass = P2, momentum=vector(-35,0,0), make_trail=True )
                  
                planet3 = sphere( pos=vector(0,-4,0), radius=0.1, color=color.green,mass = P3, momentum=vector(160,0,0), make_trail=True )
               
                dt = 0.0001
                t = 0
                while (t <= 0.1):
                        rate(1000)
                        star.force = gforce(star,planet1)+gforce(star,planet2)+gforce(star,planet3)
                        planet1.force = gforce(planet1,star)+gforce(planet1,planet2)+gforce(planet1,planet3)
                        planet2.force = gforce(planet2,star)+gforce(planet2,planet1)+gforce(planet2,planet3)
                        planet3.force = gforce(planet3,star)+gforce(planet3,planet1)+gforce(planet3,planet2)

    
                        star.momentum = star.momentum + star.force*dt
                        planet1.momentum = planet1.momentum + planet1.force*dt
                        planet2.momentum = planet2.momentum + planet2.force*dt
                        planet3.momentum = planet3.momentum + planet3.force*dt

   
                        star.pos = star.pos + star.momentum/star.mass*dt
                        planet1.pos = planet1.pos + planet1.momentum/planet1.mass*dt
                        planet2.pos = planet2.pos + planet2.momentum/planet2.mass*dt
                        planet3.pos = planet3.pos + planet3.momentum/planet3.mass*dt
    
                        t = t + dt
