import math

class ShapeException(Exception):
    pass


def shape(vector):
    v_shape = len(vector)
    return (v_shape,)

def vector_add(vector_1, vector_2):
    """
    [a b]  + [c d]  = [a+c b+d]

    Matrix + Matrix = Matrix
    """
    if len(vector_1) != len(vector_2):
        raise ShapeException

    v_sum = [sum(x) for x in zip(vector_1, vector_2)]
    return v_sum



def vector_sub(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        raise ShapeException
    v_sub = [vector_1[x] - vector_2[x] for x in range(len(vector_1))]
    return v_sub

def vector_sum(*args):
     """vector_sum can take any number of vectors and add them together."""


     v_sum = [sum(x) for x in zip(*args)]
     return v_sum


def dot(vector_1, vector_2):
    """
    dot([a b], [c d])   = a * c + b * d

    dot(Vector, Vector) = Scalar
    """
    if len(vector_1) != len(vector_2):
        raise ShapeException

    v_dot = sum([x * y for x, y in zip(vector_1, vector_2)])
    return v_dot

def vector_multiply(vector_1, y):
    """
    [a b]  *  Z     = [a*Z b*Z]

    Vector * Scalar = Vector
    """

    v_mult = [x*y for x in vector_1]
    return v_mult

def vector_mean(*args):
     """
     mean([a b], [c d]) = [mean(a, c) mean(b, d)]

     mean(Vector)       = Vector
     """
     v_mean = [(sum(x)/len(args)) for x in zip(*args)]
     return v_mean


def magnitude(vector_1):
     """
     magnitude([a b])  = sqrt(a^2 + b^2)

     magnitude(Vector) = Scalar
     """
     v_mag = sum([x**2 for x in vector_1])
     return math.sqrt(v_mag)
