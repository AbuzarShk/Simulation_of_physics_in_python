from vpython import*

class ROLL():
  def __init__(self,R=1.5,O=1,L=20):
    disk_radius = R
    disk_omega = O
    disk_velocity = disk_radius*disk_omega
    track_length = L
# Thickness of drawn items.
    thickness = 0.05

# Create track.
    track = curve(color=color.white, 
              pos=[vector(-track_length/2,0,0),
                   vector(track_length/2,0,0)])

# Create disk. 
    disk = cylinder(texture="https://i.imgur.com/1nsaRK1.png", axis=vector(0,0,thickness), 
                        size=vector(thickness,2*disk_radius, 2*disk_radius),
                        pos=vector(-track_length/2,disk_radius,0),
                        omega=disk_omega, make_trail=False)

# Create point to trace a cycloid.
    marker_point = sphere( radius=thickness, color=color.red, make_trail = True,
                pos=disk.pos+vector(0,-disk_radius,0), retain=2000, theta=-pi/2,
                omega = -disk.omega)

# To create a second disk, copy and paste lines 17 through 25 in the space below.
# Be sure to give new names to everything in your second disk.

# Set animation parameters.
    dt = 0.01
    t = 0
    scene.autoscale = False
    total_distance = 0
# Animate!
    while (disk.pos.x < track_length/2):
      rate(200)

    # Update angles. Copy, paste, and modify this to apply to your second disk.
      marker_point.theta += marker_point.omega*dt

    # Move and rotate disk. Copy, paste, and modify this to apply to your second disk.
      disk.pos = disk.pos + disk_velocity*dt*vector(1,0,0)
      disk.rotate(angle=marker_point.omega*dt, axis=vector(0,0,1))

    # Move point. Copy, paste, and modify this to apply to your second disk.
      axis = disk_radius*vector(cos(marker_point.theta),sin(marker_point.theta),0) # Not sure why the length changes...
      point_distance = mag(disk.pos+axis - marker_point.pos)
      marker_point.pos = disk.pos+axis

      total_distance = total_distance + point_distance

    # Update time.
      t+=dt
    
    print("Disk traveled a distance of ",track_length)
    print("Red point traveled a distance of ",total_distance)