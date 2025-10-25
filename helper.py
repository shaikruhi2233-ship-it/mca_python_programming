# module example
def calcCircumference(radius:float)->float:
    """
    calculate the circumference based on the radius
    """
    return 2*(22/7)*radius
def calcAreaOfcircle(radius=None,diameter=None):
    """
    return area of circle based on radius or diameter
    """
    pi=22/7
    if radius is not None:
        return pi*radius**2
    elif diameter is not None:
        return pi*(diameter/2)**2
