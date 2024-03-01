# this is just a simple example of how to use the library

from fancy_calcy.advanced import ScientificFunctions


sf = ScientificFunctions()

print(sf.factorial(5))

print(sf.power(2, 3))

print(sf.logarithm(10, 100))

print(sf.sine(45))

print(sf.cosine(60))

print(sf.tangent(30))

print(sf.add_complex(2+3j, 4+5j))

print(sf.subtract_complex(4+5j, 2+3j))
