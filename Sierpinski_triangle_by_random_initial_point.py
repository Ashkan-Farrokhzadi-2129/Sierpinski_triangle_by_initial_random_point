import turtle
import random
import math

# Ask the user for the number of iterations (n)
# n = int(input("Enter the number of iterations: "))
n = 500

# Function to draw an equilateral triangle
def draw_triangle(vertices):
    pen.penup()
    pen.goto(vertices[0][0], vertices[0][1])
    pen.pendown()
    for vertex in vertices:
        pen.goto(vertex[0], vertex[1])
    pen.goto(vertices[0][0], vertices[0][1])

# Function to calculate the midpoint between two points
def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Create a screen/window
screen = turtle.Screen()
screen.title("Fractal Process Inside Triangle")

# Create a turtle object to draw
pen = turtle.Turtle()

# Set the turtle speed to the fastest (instant movement)
pen.speed(0)

# Side length for the equilateral triangle
side_length = 400

# Calculate the height of the equilateral triangle
height = (math.sqrt(3) / 2) * side_length

# Define the vertices of the triangle centered at (0, 0)
A = (-side_length / 2, -height / 3)  # Bottom-left vertex
B = (side_length / 2, -height / 3)   # Bottom-right vertex
C = (0, 2 * height / 3)              # Top vertex

# Draw the equilateral triangle
draw_triangle([A, B, C])

# Function to choose a random point inside the triangle
def random_point_in_triangle(A, B, C):
    r1 = random.random()
    r2 = random.random()

    if r1 + r2 > 1:
        r1 = 1 - r1
        r2 = 1 - r2

    x = r1 * A[0] + r2 * B[0] + (1 - r1 - r2) * C[0]
    y = r1 * A[1] + r2 * B[1] + (1 - r1 - r2) * C[1]

    return (x, y)

# Choose a random point inside the triangle
random_point = random_point_in_triangle(A, B, C)

# Draw the random point (using a much smaller dot)
pen.penup()
pen.goto(random_point[0], random_point[1])
pen.pendown()
pen.dot(3, "blue")  # Smaller blue dot

# Set a start point (the random point) and begin iterations
current_point = random_point

# Repeat the process n times
for _ in range(n):
    # Randomly select one of the three vertices (A, B, or C)
    random_vertex = random.choice([A, B, C])

    # Find the midpoint of the current point and the random vertex
    new_point = midpoint(current_point, random_vertex)

    # Draw the midpoint as a smaller red dot
    pen.penup()
    pen.goto(new_point[0], new_point[1])
    pen.pendown()
    pen.dot(3, "red")  # Smaller red dot

    # Update current_point to the new midpoint
    current_point = new_point

# Hide the turtle cursor
pen.hideturtle()

# Keep the window open
turtle.done()
