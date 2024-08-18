from geom2d.point import *

l = []

for i in range(-5, 6):
    l.append(Point(i, i*i))

# for el in l:
#     print(el)
#
# for elm in l:
#     elm.y = -elm.y
#     print(elm)

l2 = []
for elme in l:
    l2.append(Point(elme.x, -elme.x))


print(l)
print(l2)

# List comrehention

l = [Point(i, i*i) for i in range(-5, 6)]

l2 = [Point(el.x, -el.x) for el in l]

print(l)
print(l2)

