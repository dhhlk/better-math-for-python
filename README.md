🧮 maths--cleaned-python-module

A pure-Python math utility library built without the math module, using only decimal.Decimal for clarity, precision, and learning.

This project is designed to be:

📚 Educational

🧼 Clean & readable

🎯 Deterministic & precise

🧠 Math-from-scratch inspired

✨ Features

No math module — everything is implemented manually

Uses Decimal for controlled precision

Well-organized, beginner-friendly functions

Ideal for:

learning math logic

school projects

custom calculators

understanding how math libraries work internally

📦 Installation

Clone the repository:

git clone https://github.com/dhhlk/better-maths-for-python.git


Then import directly (no install needed):

from maths_cleaned import *

🔢 Precision Control
The module uses Python’s decimal module:

from decimal import getcontext
getcontext().prec = 28


You can change precision anytime before calculations.

🧠 Available Functions

🔹 Constants

PI

E

🔹 Basic Number Functions

fact(n) – factorial

fibonacci(n) – Fibonacci series

digital_root(n)

is_harshad(n)

triangular(n)

collatz_steps(n)

🔹 Roots & Powers

sqrt(x)

cbrt(x)

power(x, n)

🔹 Logarithms

ln(x) – natural log (Decimal-based)

log(x, base)

🔹 Trigonometry (manual series-based)

sin(x)

cos(x)

tan(x)

🔹 Geometry

circumference(radius)

area_circle(radius)

area_square(side)

area_rectangle(length, breadth)

area_triangle(base, height)

perimeter_square(side)

perimeter_rectangle(length, breadth)

distance_2d(x1, y1, x2, y2)

cube_volume(side)

cube_surface_area(side)

pythagoras(a, b)

🔹 Finance & Percentages

percentage(part, total)

simple_interest(principal, rate, time)

compound_interest(principal, rate, time)

🔹 Statistics

average(values)

weighted_average(values, weights)

🔹 Number Theory

is_prime(n)

gcd(a, b)

lcm(a, b)

🔹 Utility / Game Math

clamp(x, low, high)

smoothstep(x)

logistic(x, r=3.9)

🧪 Example Usage
from maths_cleaned import PI, sin, fibonacci, area_circle

print(sin(PI / 2))
print(fibonacci(10))
print(area_circle(5))

🎯 Why this project?

Python’s math module is powerful — but opaque.

This library is about:

understanding the logic

seeing the formulas

learning how math works under the hood

Perfect for students, hobbyists, and curious programmers.

📜 License

MIT License — free to use, modify, and learn from.

🚀 Future Ideas

Unit tests

More number theory

Matrix math (Decimal-based)

Calculus utilities (limits, derivatives)

pip packaging
