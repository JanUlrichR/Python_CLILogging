import math
import logging

def calcSphere(radius):
    """Calculates Volume of a Sphere

    Calculates Volume of a Sphere in 3 Dimensions by using the formula
    V = 4/3 * pi * radius^3

    Args:
        radius (number): radius of the sphere

    Returns:
        float: volume of the sphere
    """

    logging.getLogger().info("Calcing volume of sphere with radius {0}".format(radius))

    if not(isinstance(radius, (int, float))):
        logging.getLogger().error("{0} is not a valid radius, return -666".format(radius))
        return -666

    if radius < 0 :
        logging.getLogger().warning("Radius {0} was negative, return -1".format(radius))
        return -1

    res = 4/3 * math.pi * math.pow(radius,3)

    logging.getLogger().info("Volume is {0}".format(res))

    return res