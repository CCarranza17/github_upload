fv = 1000
cost = 800
remaining = 12
hurdle = .2

def pvcalc(x,y,z):
    pv = x / (1 +(y / 12)) ** z
    return pv

print("The PV is", pvcalc(1000,12,.2))


def pvcalc2(fv,remaining,hurdle):
    pv2 = fv / (1 +(remaining / 12)) ** hurdle
    return pv2

print("PV 2 is ",pvcalc2(1000,12,.2))

