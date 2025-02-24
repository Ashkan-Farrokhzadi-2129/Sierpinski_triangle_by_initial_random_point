# Chaos Game Fractal in Turtle Graphics

This Python program generates a fractal pattern known as the **Sierpinski Triangle** using the Chaos Game algorithm. The program draws an equilateral triangle, selects random points inside it, and iteratively moves towards one of the triangle's vertices, creating a fractal pattern as the number of iterations increases.

## How it Works

The Chaos Game algorithm works as follows:
1. Start with an equilateral triangle and choose a random point inside the triangle.
2. For each iteration, randomly select one of the three vertices of the triangle.
3. Move halfway towards the selected vertex.
4. Repeat the process for a specified number of iterations.
5. The pattern formed will converge into the well-known **Sierpinski Triangle**.

## Requirements

- Python 3.x
- The `turtle` module (usually comes pre-installed with Python)

## Customization

- You can change the number of iterations by adjusting the variable `n` (currently set to 500).
- You can also modify the side length of the triangle by adjusting the `side_length` variable.
- The colors of the dots and the triangle can be customized by changing the relevant color values in the code.

## Example Output

The program will generate a fractal pattern within an equilateral triangle that resembles the **Sierpinski Triangle**. The pattern will become more defined as the number of iterations increases.
