from math import hypot
from time import sleep
from typing import Optional


class Point:

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def rest(self):
        self.move(0, 0)

    def distance(self, other: "Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)


point: Optional[Point] = None


def get_point():
    global point
    if not point:
        point = Point()
        sleep(5)
    return point


po1 = get_point()
po1.move(4, 9)
print(po1.x,po1.y)

















# # <object>.<attribute>=<value>

# p1 = Point()
# p2 = Point()

# p1.rest()
# print(p1.x, p1.y)

# p2.move(3, 4)
# print(p2.x, p2.y)
# #distance
# print(p1.distance(p2))
# print(p2.distance(p1))
# print(p2.distance(p2))
# print(p1.distance(p1))
#################################
