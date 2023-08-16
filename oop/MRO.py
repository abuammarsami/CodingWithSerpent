# MRO- Method Resolution Order
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())


class S:
    @staticmethod
    def ddo_it(z):
        z[0] = 0


m = [1, 2, 3, 4, 5]

ms = ""

for i in m:
    ms = ms + str(i) + " "

print(ms)

"""
parent class object could be cast to child class object
"""
