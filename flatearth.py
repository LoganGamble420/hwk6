import numpy as np

def grav_accel(p1, p2, m):
    """ p1 = point where the mass element is
        p2 = point you are interested in
        m  = mass
        returns a vector of the gravitational accleration"""
    G = 6.6743e-11
    r_diff=p2-p1
    r = np.sqrt(np.sum(p2-p1)**2)
    rhat=r_diff/r
    return (-1*G/r**2)*rhat*m

def point_in_sphere(x,y,z, radius=None):
    if (x**2 + y**2 + z**2) <= radius**2:
        return True
    else:
        return False

def point_in_cylinder(x,y,z,height,radius=None):
    if ((x**2 + y**2)**(1/2)) <= radius and z >=0 and z>=height:
        return True
    else:
        return False


if __name__ == "__main__":
    km = 1000                   #1 km = 1000 meters
    rho = 5514                  #kg/m^3, density of Earth
    r_earth = 6378*km           #radius of globe Earth
    r_flat = 20037*km           #radius of flat earth
    flat_h = 4750*km            #height of flat earth from side view
    h = 300.0*km                #relatively coarse step size
                                #set grid size same in x,y,z
    dx, dy, dz = h, h, h
    dV = dx*dy*dz
                                #x, y, z define boundaries of grid, here 7000 km
    x = np.arange(-6500*km, 6500*km, dx)
    y = x.copy()
    z = y.copy()
    fx= np.arange(-21000*km,21000*km,dx)
    fy = fx.copy()
    fz = np.arange(-5000*km,5000*km,dx)
                    #define points on the north pole, south pole, and equator for globe and flat earth
    point_northpole = np.array([0, 0,6378*km])
    point_equator   = np.array([6378*km,0,0])
    point_southpole = np.array([0,0,-6378*km])
    flat_northpole = np.array([0,0,4750*km])
    flat_equator = np.array([10085.5*km,0,0])
    flat_edge = np.array([20037*km,0,0])
                    # set all values to 0
    flat_vec_northpole=0
    flat_vec_equator=0
    flat_vec_edge=0
    grav_vec_northpole = 0
    grav_vec_equator = 0
    grav_vec_southpole = 0
    for idx, xx in enumerate(x):
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz,radius=6378*km):
                    m = rho*dV #mass in kg
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
                    grav_vec_equator += grav_accel(point, point_equator,m)
                    grav_vec_southpole += grav_accel(point,point_southpole, m)

    for idx, xx in enumerate(fx):
        for yy in fy:
            for zz in fz:
                if point_in_cylinder(xx,yy,zz,flat_h, radius=20037*km):
                    m = rho*dV
                    point = np.array([xx,yy,zz])
                    flat_vec_northpole += grav_accel(point, flat_northpole, m,)
                    flat_vec_equator += grav_accel(point, flat_equator, m,)
                    flat_vec_edge += grav_accel(point, flat_edge, m,)


print("The gravity vector at the north pole of a globe earth is...", grav_vec_northpole)
print("The gravity vector at the equator of a globe earth is...", grav_vec_equator)
print("The gravity vector at the south pole of a globe earth is...", grav_vec_southpole)
print("The gravity vector at the north pole of a flat earth is...", flat_vec_northpole)
print("The gravity vector at the equator of a flat earth is...", flat_vec_equator)
print("The gravity vector at the edge of a flat earth is...", flat_vec_edge)
