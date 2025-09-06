from .tuple import Tuple

def FixedLengthArray(Type, Length: int):
    return Tuple(*([Type] * Length))
