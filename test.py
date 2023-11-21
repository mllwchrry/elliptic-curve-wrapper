from index import *
import unittest
import fastecdsa.curve as curve
from fastecdsa.point import Point
from fastecdsa.encoding import sec1
import secrets

class TestECPointFunctions(unittest.TestCase):

    # setting a curve for testing
    def setUp(self):
        self.curve = curve.secp256k1
        SetCurve(curve.secp256k1)

    # should get the correct base point G for the selected EC
    def test_BasePointGGet(self):
        base_point = BasePointGGet()
        self.assertTrue(base_point.X == self.curve.G.x and base_point.Y == self.curve.G.y)

    # should generate a correct point on the selected EC
    # x and y are appropriate for secp256k1 curve (change for others)
    def test_ECPointGen(self):
        x = 0xc6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5
        y = 0x1ae168fea63dc339a3c58419466ceaeef7f632653266d0e1236431a950cfe52a
        point = ECPointGen(x, y)
        self.assertTrue(IsOnCurveCheck(point))
        self.assertEqual(point.X, x)
        self.assertEqual(point.Y, y)

    # should correctly add 2 points
    # x and y are appropriate for secp256k1 curve (change for others)
    def test_AddECPoints(self):
        ax = 0xc6047f9441ed7d6d3045406e95c07cd85c778e4b8cef3ca7abac09b95c709ee5
        ay = 0x1ae168fea63dc339a3c58419466ceaeef7f632653266d0e1236431a950cfe52a
        point_a = ECPointGen(ax, ay)
        point_b = BasePointGGet()
        result_point = AddECPoints(point_a, point_b)
        self.assertTrue(IsOnCurveCheck(result_point))
        lib_result = Point(ax, ay, self.curve) + self.curve.G
        self.assertTrue(result_point.X == lib_result.x and result_point.Y == lib_result.y)

    # should correctly double a point
    def test_DoubleECPoint(self):
        point = BasePointGGet()
        doubled_point = DoubleECPoint(point)
        lib_result = self.curve.G * 2
        self.assertTrue(IsOnCurveCheck(doubled_point))
        self.assertTrue(doubled_point.X == lib_result.x and doubled_point.Y == lib_result.y)

    # should correctly multiply a point by scalar
    def test_ScalarMult(self):
        point = BasePointGGet()
        result_point = ScalarMult(point, 18)
        lib_result = self.curve.G * 18
        self.assertTrue(IsOnCurveCheck(result_point))
        self.assertTrue(result_point.X == lib_result.x and result_point.Y == lib_result.y)

    # should correctly calculate the Diffie-Hellman secret using selected EC
    # k*(d*G) = d*(k*G)
    def test_ArePointsEqual(self):
        G = BasePointGGet()
        k = secrets.randbits(256)
        d = secrets.randbits(256)

        H1 = ScalarMult(G, d)
        H2 = ScalarMult(H1, k)

        H3 = ScalarMult(G, k)
        H4 = ScalarMult(H3, d)

        self.assertTrue(ArePointsEqual(H2, H4))

    # should correctly serialize and deserialize a point based on the SEC1 standard
    def test_SerializeDeserialize(self):
        point = BasePointGGet()
        serialized_point = SerializePoint(point)
        deserialized_point = DeserializePoint(serialized_point)
        self.assertTrue(ArePointsEqual(point, deserialized_point))

    # should correctly serialize and deserialize a point based on the SEC1 standard in a compressed format
    def test_SerializeDeserializeCompressed(self):
        point = BasePointGGet()
        serialized_point = SerializePoint(point, True)
        deserialized_point = DeserializePoint(serialized_point)
        self.assertTrue(ArePointsEqual(point, deserialized_point))