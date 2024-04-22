"""Recursive Turtle Scene - EX08."""

__author__ = "730662932"

from turtle import Turtle, done


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color('light green', 'light green')
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        a_turtle.forward(100)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_triangle(a_turtle: Turtle, x: float, y: float, amount: float) -> None:
    """Draw an equilateral triangle."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color('lavender', 'lavender')
    a_turtle.begin_fill()
    i: int = 0
    while i < 3:
        a_turtle.forward(amount)
        a_turtle.left(120)
        i = i + 1
    a_turtle.end_fill()


def draw_circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle."""
    a_turtle.penup()
    a_turtle.goto(x, y - radius)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.color('orange', 'orange')
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


def draw_recursive_triangles(a_turtle: Turtle, x: float, y: float, size: float, depth: int) -> None:
    """Draw a recursive pattern of triangles."""
    if depth == 0:
        return
    else:
        draw_triangle(a_turtle, x, y, size)
        for angle in [0, 120, 240]:
            new_x = x + size * 0.5 * 2 * (2 ** 0.5) * (3 ** 0.5) * (1 + 2 * (3 ** 0.5))
            new_y = y
            a_turtle.penup()
            a_turtle.goto(new_x, new_y)
            a_turtle.setheading(angle)
            a_turtle.pendown()
            a_turtle.color()
            draw_recursive_triangles(a_turtle, new_x, new_y, size / 2, depth - 1)


def recursive_Shapes(a_Turtle: Turtle, amount: int) -> None:
    """Using recursive."""
    if amount == 0:
        return
    else:
        a_Turtle.right(90)
        a_Turtle.forward(100)
        return recursive_Shapes(a_Turtle, amount - 1)


def main() -> None:
    """The entrypoint of my scene."""
    my_turtle = Turtle()
    
    # Draw components
    draw_square(my_turtle, 0, 0, 50)
    draw_square(my_turtle, 100, 0, 80)
    draw_triangle(my_turtle, 0, 0, 200)
    draw_circle(my_turtle, 0, 200, 70)
    my_turtle.goto(-100, 0)
    recursive_Shapes(my_turtle, 4)
    draw_triangle(my_turtle, -200, 0, 100)
    
    done()


if __name__ == "__main__":
    main()