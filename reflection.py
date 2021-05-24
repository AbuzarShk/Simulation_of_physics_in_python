from vpython import*


class Reflection():
    def __init__(self):


        mirror = box(pos=vector(0,-2,0),size=vector(7,0.1,7),color=vector(0.75,0.75,0.75))
        #get_sides(mirror)

        red_light = sphere(pos=vector(-1.9,4,0),radius=0.1,color=color.red,vel=vector(1,-2,0),make_trail=True,trail_type="points")

        green_light = sphere(pos=vector(1.9,4,0),radius=0.1,color=color.green,vel=vector(-1,-2,0),make_trail=True,trail_type="points")

        time = 0
        dt = 0.1
        while(time<4):
            rate(10)
            red_light.pos += red_light.vel*dt
            green_light.pos += green_light.vel*dt
            if (red_light.pos.y<mirror.pos.y):
                red_light.vel.y *= -1
            if (green_light.pos.y<mirror.pos.y):
                green_light.vel.y *= -1
            time += dt


        def get_sides(s):
            s.front = s.pos.z+s.size.z/2
            s.back = s.pos.z-s.size.z/2
            s.right = s.pos.x+s.size.x/2
            s.left = s.pos.x-s.size.x/2
            s.top = s.pos.y+s.size.y/2
            s.bottom = s.pos.y-s.size.y/2
            return