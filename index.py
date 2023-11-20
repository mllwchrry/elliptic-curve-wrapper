import fastecdsa.curve as curve
from fastecdsa.point import Point
import secrets

class ECPoint:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

curve = curve.secp256k1

def BasePointGGet():
    BasePoint = curve.G
    return ECPoint(BasePoint.x, BasePoint.y)

def ECPointGen(x, y):
    newPoint = ECPoint(x, y)
    if IsOnCurveCheck(newPoint):
        return newPoint

def IsOnCurveCheck(p):
    return curve.is_point_on_curve((p.X, p.Y))

def AddECPoints(a, b):
    pa = Point(a.X, a.Y, curve)
    pb = Point(b.X, b.Y, curve)
    result = pa + pb
    return ECPoint(result.x, result.y)

def DoubleECPoints(a):
    p = Point(a.X, a.Y, curve)
    doubled_p = 2 * p
    return ECPoint(doubled_p.x, doubled_p.y)

def ScalarMult(k, a):
    p = Point(a.X, a.Y, curve)
    mul = k * p
    return ECPoint(mul.x, mul.y)

def ECPointToString(p):
    return f"({hex(p.X)}, {hex(p.Y)})"

def StringToECPoint(s):
    x, y = s.strip('()').split(',')
    return ECPoint(int(x, 16), int(y, 16))

def PrintECPoint(point):
    print(f"X: {hex(point.X)}")
    print(f"Y: {hex(point.Y)}")

# k*(d*G) = d*(k*G)

G = BasePointGGet()
k = secrets.randbits(256)

d = secrets.randbits(256)

H1 = ScalarMult(d, G)
H2 = ScalarMult(k, H1)

H3 = ScalarMult(k, G)
H4 = ScalarMult(d, H3)


print(PrintECPoint(H2))
print(PrintECPoint(H4))
