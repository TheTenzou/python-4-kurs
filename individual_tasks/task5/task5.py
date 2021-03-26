class Shape:
    name = "shape"
    corners = list()

    def isIntersect(self, shape):
        this_sides = self.__get_all_sides__()
        shape_sides = shape.__get_all_sides__()
        for this_side in this_sides:
            for shape_side in shape_sides:
                if self.__line_intersect__(this_side, shape_side):
                    return True
        return False

    def compare(self, shape):
        return self.name == shape.name and self.corners == shape.corners
    
    def __get_all_sides__(self):
        sides = list()
        for i in range(len(self.corners)-1):                
            sides.append((self.corners[i], self.corners[i+1]))            
        sides.append((self.corners[len(self.corners)-1], self.corners[0]))
        return sides

    def __line_intersect__(self, side1, side2):            
        (s1_x1, s1_y1), (s1_x2, s1_y2) = side1
        (s2_x1, s2_y1), (s2_x2, s2_y2) = side2

        i1 = [min(s1_x1, s1_x2), max(s1_x1, s1_x2)]
        i2 = [min(s2_x1, s2_x2), max(s2_x1, s2_x2)]

        ia = [max(min(s1_x1, s1_x2), min(s2_x1, s2_x2)),
              min(max(s1_x1, s1_x2), max(s2_x1, s2_x2))]

        if (max(s1_x1, s1_x2) < min(s2_x1, s2_x2)):
            return False

        xa=float()
        if (s1_x1 - s1_x2) == 0.0:
            a2 = (s2_y1 - s2_y2)/(s2_x1 - s2_x2)
            b2 = s2_y1 - a2*s2_x1
            if a2 == 0.0:
                xa = b2
            else:
                xa = b2/a2  
        elif (s2_x1 - s2_x2) == 0.0:
            a1 = (s1_y1 - s1_y2)/(s1_x1 - s1_x2)
            b1 = s1_y1 - a1*s1_x1
            if a1 == 0.0:
                xa = b1
            else:
                xa = b1/a1  
        else:
            a1 = (s1_y1 - s1_y2)/(s1_x1 - s1_x2)
            a2 = (s2_y1 - s2_y2)/(s2_x1 - s2_x2)

            b1 = s1_y1 - a1*s1_x1
            b2 = s2_y1 - a2*s2_x1

            if (a1 == a2):
                return False
            
            xa = (b2 - b1)/(a1 - a2)

        if ((xa < max(min(s1_x1, s1_x2), min(s2_x1, s2_x2))) or
            (xa > min(max(s1_x1, s1_x2), max(s2_x1, s2_x2)))):
            return False
        else:
            return True


class Rectangle(Shape):
    name = "Ractangle"

    def __init__(self, name, top_left, bottom_right):
        self.name = name
        self.corners = list()
        self.corners.append(top_left)
        self.corners.append((bottom_right[0], top_left[1]))
        self.corners.append(bottom_right)
        self.corners.append((top_left[0], bottom_right[1]))
            
            
class  Square(Shape):
    name = "Square"

    def __init__(self, name, top_left, side):
        self.name = name
        self.corners = list()
        self.corners.append(top_left)
        self.corners.append((top_left[0]+side, top_left[1]))
        self.corners.append((top_left[0]+side, top_left[1]+side))
        self.corners.append((top_left[0], top_left[1]+side))

def main():
    rec1 = Rectangle("rec1", top_left=(1, 2), bottom_right=(3, 4))
    sq1 = Square("sq", top_left=(2, 2), side=2)
    sq2 = Square("sq2", top_left=(100, 100), side=1)
    sq3 = Square("sq2", top_left=(100, 100), side=1)

    print(rec1.isIntersect(sq1))
    print(sq1.isIntersect(sq2))

    print(sq2.compare(sq3))

main()