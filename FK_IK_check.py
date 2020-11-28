# Checking FK and IK to make sure the code is right

from math import cos, sin, atan2, sqrt, acos, pi

# Forward Kinematics

def FKin(q1, q2, q3):
    """q1 limit = -1.13 to 1.57, q2 limit =  -2.64 to 2.55, q3 limit = -1.78 to 1.78"""

    l1 = 0.155
    l2 = 0.135
    l3 = 0.218
    
    phi = q1 + q2 + q3
    print(phi)

    if phi > pi:
        phi = phi- (2*pi)
    elif phi < -pi:
        phi = (2*pi) + phi

    x = (l1*cos(q1)) + (l2*cos(q1+q2)) + (l3*cos(phi))
    y = (l1*sin(q1)) + (l2*sin(q1+q2)) + (l3*sin(phi))


    print("FK result for {}, {}, {} is {}, {}, {}".format(q1, q2, q3, x, y, phi))

    return [x, y, phi]


def IKin(x, y, phi):
    """calculate IK"""

    l1 = 0.155
    l2 = 0.135
    l3 = 0.218

    big_X = x - (l3*cos(phi))
    big_Y = y - (l3*sin(phi))

    denom1 = sqrt(big_X**2 + big_Y**2)
    gamma = atan2((-big_Y/denom1), (-big_X/denom1))

    denom2 = 2*l1*(sqrt(big_X**2 + big_Y**2))

    # if phi < 0:
    #     q1 = gamma + acos(-(big_X**2 + big_Y**2 + l1**2 - l2**2)/denom2)
    # else:
    #     q1 = gamma - acos(-(big_X**2 + big_Y**2 + l1**2 - l2**2)/denom2)

    q1_A = gamma + acos(-(big_X**2 + big_Y**2 + l1**2 - l2**2)/denom2)
    q1_B = gamma - acos(-(big_X**2 + big_Y**2 + l1**2 - l2**2)/denom2)

    if q1_A < q1_B:
        q1 = q1_A
    else:
        q1 = q1_B

    q2 = atan2(((big_Y - (l1*sin(q1)))/l2), ((big_X - (l1*cos(q1)))/l2)) - q1
    q3 = phi - q1 - q2

    if q1 > pi:
        q1 = q1 - (2*pi)
    elif q1 < -pi:
        q1 = (2*pi) + q1

    if q2 > pi:
        q2 = q2 - (2*pi)
    elif q2 < -pi:
        q2 = (2*pi) + q2

    if q3 > pi:
        q3 = q3 - (2*pi)
    elif q3 < -pi:
        q3 = (2*pi) + q3

    print("IK result for {}, {}, {}, is {}, {}, {}".format(x, y, phi, q1, q2, q3))

    return [q1, q2, q3]


#test

# q11 = -1.0
# q12 = -0.6
# q13 = -0.75
# q1 limit = -1.13 to 1.57, q2 limit =  -2.64 to 2.55, q3 limit = -1.78 to 1.78


[x2, y2, phi2] = FKin(-1.0,-0.6,-1.25) #box
IKin(x2, y2, phi2)

[x1, y1, phi1] = FKin(-0.7, -1.3, -0.75) #trolley
IKin(x1, y1, phi1)

