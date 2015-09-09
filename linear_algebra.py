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
    v_add = [vector_1[x] + vector_2[x] for x in range(len(vector_1))]
    return v_add



def vector_sub(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        raise ShapeException
    v_add = [vector_1[x] - vector_2[x] for x in range(len(vector_1))]
    return v_add

# def vector_sum(vector):
#     pass
#
# def dot(vector):
#     pass
#
# def vector_multiply(vector):
#     pass
#
# def vector_mean(vector):
#     pass
#
# def shape(vector):
#     pass
