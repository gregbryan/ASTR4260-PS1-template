import math

def kappa0(p, z):
    return math.acos((p**2 + z**2 - 1)/(2*p*z))

def kappa1(p, z):
    return math.acos((1 - p**2 + z**2)/(2*z))

def lambd(p, z):
    if 1 + p < z:
        return 0
    if z <= 1 - p:
        return p**2
    if z <= p - 1:
        return 1
    arg = (4*z**2 - (1 + z**2 - p**2)**2)/4
    if arg >= 0:
        return (kappa0(p, z)*p**2 + kappa1(p, z) - math.sqrt(arg))/math.pi
    else:
        return 0

def FluxRatio(p, z):
    """
    Compute the ratio of obscured/unobscured flux for a planet transit.
    
    Arguments:
       p - ratio of planet radius to stellar radius
       z - distance between star and planet divided by stellar radius
    Returns: 
       FluxRatio - ratio of obscured to unobscured stellar flux

    """
    return 1 - lambd(p, abs(z))
