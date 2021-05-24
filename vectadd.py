from vpython import*
#GlowScript 2.7 VPython



class VECTADD():
    def __init__(self,VAX =4,VAY= 1,VBX= 2,VBY= 4):
        


        


        def vec_add(v1,v2,color):
            sleep(1)
            total_x = v1.xcomp + v2.xcomp
            total_y = v1.ycomp + v2.ycomp
            start = v1.start
            v2.start = v1.end
            v2.pos = vector(v2.start[0],v2.start[1],0)
            end = (v1.start[0]+total_x,v1.start[1]+total_y)
            added = make_vector("start-end",start,end,color)
            return added

        


        def make_grid():
            scene.background = color.white
            thickness = 0.02
            dx = 1
            xmax = 6
            x = -xmax
            while (x <= xmax):
                y = -xmax
                gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
                while (y <= xmax):
                    gridline.append(vector(x,y,-thickness))
                    y = y + dx
                x = x + dx
            y = -xmax
            while (y <= xmax):
                x = -xmax
                gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
                while (x <= xmax):
                    gridline.append(vector(x,y,-thickness))
                    x = x + dx
                y = y + dx
            return




        def x_y(xcomp,ycomp,color):
            sleep(1)
            vec = make_vector("x-y",xcomp,ycomp,color)
            return vec

        def start_end(start,end,color):
            sleep(1)
            vec = make_vector("start-end",start,end,color)
            return vec

        def make_vector(instruction,in1,in2,color):
            if (instruction=="mag-degrees"):
                mag = in1
                angle = in2
                xcomp = mag*cos(angle*pi/180)
                ycomp = mag*sin(angle*pi/180)
                start = vector(0,0,0)
                end = vector(xcomp+start.x,ycomp+start.y,0)
            elif (instruction=="x-y"):
                xcomp = in1
                ycomp = in2
    # Calculate magnitude and angle. 
                mag = (xcomp**2+ycomp**2)**0.5
                angle = atan(ycomp/xcomp)*180/pi
    # Set start and end points.
                start = vector(0,0,0)
                end = vector(xcomp+start.x,ycomp+start.y,0)
            elif (instruction=="start-end"):
    # Read inputs as start and end points.
                start = vector(in1[0],in1[1],0)
                end = vector(in2[0],in2[1],0)
    # Calculate x- and y-components. 
                xcomp = end.x-start.x
                ycomp = end.y-start.y
    # Calculate magnitude and angle. 
                mag = (xcomp**2+ycomp**2)**0.5
                angle = atan(ycomp/xcomp)*180/pi
            else:
    # Someone must have called this function without proper instructions. Display error message.
                print("error in make_vector! instructions not supplied")
                return

            vec = arrow(pos=start,axis=vector(xcomp,ycomp,0),color=color,shaftwidth=0.1)
  # Vector is drawn. Attach attributes to vector.
            vec.xcomp = xcomp
            vec.ycomp = ycomp
            vec.mag = mag
            vec.degrees = angle
            vec.radians = angle*pi/180
            vec.start = (start.x,start.y)
            vec.end = (end.x,end.y)
  
            return vec

        make_grid()
        red_vector = x_y(VAX, VAY,color.red)
        blue_vector = x_y(VBX,VBY,color.blue)
        black_vector = vec_add(red_vector,blue_vector,color.black)
        print("black x-comp = ",black_vector.xcomp)
        print("red x-comp +blue x-comp =")
        print(red_vector.xcomp + blue_vector.xcomp)
        print("black y-comp = ",black_vector.ycomp)
        print("red x-comp + blue x-comp = ")
        print(red_vector.ycomp + blue_vector.ycomp)
