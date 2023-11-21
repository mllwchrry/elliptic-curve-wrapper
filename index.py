import fastecdsa.curve as curve
from fastecdsa.point import Point
from fastecdsa.encoding import sec1

class ECPoint:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

# setting the default curve
default_curve = curve.secp256k1
curve = default_curve

def SetCurve(c):
    global curve
    curve = c

def BasePointGGet():
    BasePoint = curve.G
    return ECPoint(BasePoint.x, BasePoint.y)

def ECPointGen(x, y):
    newPoint = ECPoint(x, y)
    if IsOnCurveCheck(newPoint):
        return newPoint
    else:
        raise ValueError("Point is not on curve")

def IsOnCurveCheck(p):
    return curve.is_point_on_curve((p.X, p.Y))

def AddECPoints(a, b):
    pa = Point(a.X, a.Y, curve)
    pb = Point(b.X, b.Y, curve)
    result = pa + pb
    return ECPoint(result.x, result.y)

def DoubleECPoint(a):
    p = Point(a.X, a.Y, curve)
    doubled_p = 2 * p
    return ECPoint(doubled_p.x, doubled_p.y)

def ScalarMult(a, k):
    p = Point(a.X, a.Y, curve)
    mul = k * p
    return ECPoint(mul.x, mul.y)

def ArePointsEqual(a, b):
    return a.X == b.X and a.Y == b.Y

def PrintECPoint(a):
    print(f"X: {hex(a.X)}")
    print(f"Y: {hex(a.Y)}")

# serializes a point according to the SEC1 standard (both compressed and uncompressed format)
def SerializePoint(point, compressed = False):
    x, y = point.X, point.Y
    return sec1.SEC1Encoder.encode_public_key(Point(x, y, curve), compressed)

# deserializes a point according to the SEC1 standard (both compressed and uncompressed format)
def DeserializePoint(bytes):
    deserialized_point = sec1.SEC1Encoder.decode_public_key(bytes, curve)
    return ECPoint(deserialized_point.x, deserialized_point.y)
