import math


class Shape:
    def __init__(self, center: list, line: float):
        self.center_x = center[0]
        self.center_y = center[1]

    def get_center(self):
        return [self.center_x, self.center_y]

    def move(self, x, y):
        self.center_x = x
        self.center_y = y

    def get_area(self):
        pass

    def get_distance(self, shape_first, shape_second):
        lenght = math.sqrt(
            ((shape_first.center_x - shape_second.center_x) ** 2) + (
                        (shape_first.center_y - shape_second.center_y) ** 2)
        )
        return lenght if lenght > 0 else lenght * -1


class Circle(Shape):
    def __init__(self, center, line):
        super().__init__(center, line)
        self.radius = line

    def get_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, center, line):
        super().__init__(center, line)
        self.side = line

    def get_vertex(self):
        lx = self.center_x - self.side / 2
        rx = self.center_x + self.side / 2
        by = self.center_y - self.side / 2
        ty = self.center_y + self.side / 2
        return [
            [lx, ty],
            [rx, ty],
            [rx, by],
            [lx, by],
        ]

    def get_area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, center, line):
        super().__init__(center, line)
        self.side = line

    def get_vertex(self):
        h = (math.sqrt(3) / 2) * self.side
        lx = self.center_x - h / 2
        rx = self.center_x + h / 2
        by = self.center_y - h / 2
        ty = self.center_y + h / 2
        top_coord = [self.center_x, ty]
        left_coord = [lx, by]
        right_coord = [rx, by]
        return [
            top_coord,
            left_coord,
            right_coord
        ]

    def get_area(self):
        return ((self.side ** 2) * math.sqrt(3)) / 4
