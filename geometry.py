from geom2d.point import *

l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l3 = l1
l4 = list(l1)
l4[0] = Point(0, 0)

print(l1 == l2)
print(l1 == l3)
print(l1 == l4)
print(l1 == l4)
l = [1, 5, 3, 7, 2, 8]
l5 = [1, 5, 3, 7, 2, 8]

# print(sorted(l))

print(l.sort())

ll1 = [Point(3, 1), Point(0, 0), Point(1, 2)]


#
# ll2 = sorted(ll1)
# print("ok")
# print(ll1)
# print(ll2)


# def x(p):
#     return p.x
#
#
# def y(p):
#     return p.y
# ll2 = sorted(ll1, key=y)
# ll3 = sorted(ll1, key=x)
ll2 = sorted(ll1, key=lambda p: p.x)
ll3 = sorted(ll1, key=lambda p: p.distance(Point(0, 0)))
print(ll1)
print(ll2)
# print(ll3)
