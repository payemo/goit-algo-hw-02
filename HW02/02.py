import math
import turtle

class LineSegment:
    """Represents liniar segment."""

    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos

    def draw(self):
        """Drawing the segment."""
        turtle.penup()
        turtle.goto(self.start_pos)
        turtle.pendown()
        turtle.goto(self.end_pos)

class KochCurve:
    """Class for building Koch's curve."""

    def __init__(self, level):
        self.level = level

    def _generate(self, segment: LineSegment, level):
        """Recursive method for generating Koch's curve."""
        if level == 0:
            segment.draw()
        else:
            x1, y1 = segment.start_pos
            x5, y5 = segment.end_pos

            # Calculate itermediate points.
            delta_x = (x5 - x1) / 3
            delta_y = (y5 - y1) / 3

            x2 = x1 + delta_x
            y2 = y1 + delta_y

            x3 = (0.5 * (x1 + x5) - math.sqrt(3) * (y1 - y5) / 6)
            y3 = (0.5 * (y1 + y5) - math.sqrt(3) * (x5 - x1) / 6)

            x4 = x1 + 2 * delta_x
            y4 = y1 + 2 * delta_y

            # Creating new segments
            seg1 = LineSegment((x1, y1), (x2, y2))
            seg2 = LineSegment((x2, y2), (x3, y3))
            seg3 = LineSegment((x3, y3), (x4, y4))
            seg4 = LineSegment((x4, y4), (x5, y5))

            self._generate(seg1, level - 1)
            self._generate(seg2, level - 1)
            self._generate(seg3, level - 1)
            self._generate(seg4, level - 1)

    def draw_snowflake(self):
        size = 300
        height = size * math.sqrt(3) / 2

        p1 = (-size / 2, -height / 3)
        p2 = (size / 2, -height / 3)
        p3 = (0, 2 * height / 3)

        segments = [
            LineSegment(p1, p2),
            LineSegment(p2, p3),
            LineSegment(p3, p1)
        ]

        for seg in segments:
            self._generate(seg, self.level)

def main():
    try:
        level = int(input("Enter recursion level (0 or > 0): "))
        if level < 0:
            raise ValueError
    except ValueError:
        print("Enter valid number.")
        return

    turtle.speed(0)
    turtle.hideturtle()
    turtle.setup(width=800, height=600)
    turtle.title("Kohn's snowflake")
    turtle.bgcolor("white")
    turtle.color("blue")

    # Set up initial position
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    koch_curve = KochCurve(level)
    koch_curve.draw_snowflake()

    turtle.done()

if __name__ == '__main__':
    main()