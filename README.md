# Elliptic Curve Arithmetic Wrapper

Here is a wrapper for elliptic curve arithmetic functions
from the Python library fastecdsa (https://github.com/AntonKueltz/fastecdsa).

It was implemented as the practical task for the Distributed Lab Cryptography course.

## Available functions

- **SetCurve(c)**: sets the curve c to be further used
- **BasePointGGet()**: gets the base point G of the selected curve
- **ECPointGen(x, y)**: generates a point with coordinates x and y on the curve
- **IsOnCurveCheck(p)**: checks whether the point p is on the curve
- **AddECPoints(a, b)**: adds points a and b
- **DoubleECPoint(a)**: doubles point a
- **ScalarMult(a, k)**: multiplies point a by the scalar k
- **ArePointsEqual(a, b)**: checks whether points a and b are equal
- **PrintECPoint(point)**: prints point a in a user-friendly way
- **SerializePoint(point, compressed = False)**: serializes a point
- **DeserializePoint(bytes)**: deserializes a point


## Available curves over Prime Fields

The library supports the following curves that can be set
with a wrapper function, e.g.

```python
SetCurve(curve.secp256k1)
```
<img width="654" alt="Screenshot 2023-11-21 at 21 51 57" src="https://github.com/mllwchrry/elliptic-curve-wrapper/assets/72436706/b3d58f9a-b73b-4b46-9c49-3665c409daeb">


NOTE: Please get acquainted with http://safecurves.cr.yp.to/ before choosing a curve.

## Serialization and Deserialization

Serialization and deserialization of the points on the elliptic curve were implemented 
according to the SEC1 standard for both compressed and uncompressed formats.

_**The format used for representing elliptic curve points in TLS is based on the compressed format described in SEC1.**_

```python
serialized_point = SerializePoint(point, True)
deserialized_point = DeserializePoint(serialized_point)
```

## Project Setup

### Install dependencies
```sh
pip install fastecdsa
```

Note that you need to have a C compiler. 
You also need to have GMP on your system as the 
underlying C code in this package (fastecdsa) includes the gmp.h 
header (and links against gmp via the -lgmp flag). You can install all dependencies as follows:

**apt**
```sh
sudo apt-get install python3-dev libgmp3-dev
```

**yum**
```sh
sudo yum install python-devel gmp-devel
```

**brew**
```sh
brew install gmp
```



### Run tests


```sh
python3 -m unittest test.py   
```

### Test results
<img width="695" alt="Screenshot 2023-11-21 at 21 52 17" src="https://github.com/mllwchrry/elliptic-curve-wrapper/assets/72436706/69ce1807-97dd-4549-a144-e71340b095e4">

