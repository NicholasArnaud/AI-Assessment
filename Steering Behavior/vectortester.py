'''main file'''
from mathlib import Vector

def testvector(vector1, vector2):
    '''tests vector class'''
    vector3 = vector1 + vector2
    vector3 = vector1 - vector2
    vector1.mag()
    vector1.normal()
    vector2.normal()
    vectortest = vector1 * 2
    vector1.print_info()
    vectortest.print_info()

if __name__ == "__main__":
    vectora = Vector([2, 2])
    vectorb = Vector([1, 1])
    testvector(vectora, vectorb)
