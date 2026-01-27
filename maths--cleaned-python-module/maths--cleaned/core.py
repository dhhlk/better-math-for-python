from decimal import Decimal, getcontext

# ───────────── Configuration & Constants ─────────────

getcontext().prec = 50

PI = Decimal("3.1415926535897932384626433832795028841971")
E  = Decimal("2.7182818284590452353602874713527")
ZERO = Decimal("0")
ONE  = Decimal("1")


# ───────────── Basic Number Functions ─────────────

def fact(n):
    n = int(n)
    if n < 0:
        raise ValueError("Factorial not defined for negatives")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return Decimal(result)


def fibonacci(n):
    n = int(n)
    a, b = ZERO, ONE
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def digital_root(n):
    n = abs(int(n))
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


def is_harshad(n):
    n = int(n)
    return n % sum(int(d) for d in str(n)) == 0


def triangular(n):
    n = Decimal(n)
    return n * (n + 1) / 2


def collatz_steps(n):
    n = int(n)
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


# ───────────── Roots & Powers ─────────────

def sqrt(x):
    x = Decimal(x)
    if x < 0:
        raise ValueError("Square root of negative")
    guess = x / 2
    for _ in range(30):
        guess = (guess + x / guess) / 2
    return guess


def cbrt(x):
    x = Decimal(x)
    guess = x / 3
    for _ in range(30):
        guess = (2 * guess + x / (guess * guess)) / 3
    return guess


def power(base, exp):
    base = Decimal(base)
    exp = int(exp)
    result = ONE
    for _ in range(abs(exp)):
        result *= base
    return result if exp >= 0 else ONE / result


# ───────────── Logarithms ─────────────

def ln(x):
    x = Decimal(x)
    if x <= 0:
        raise ValueError("ln undefined for non-positive")

    y = (x - ONE) / (x + ONE)
    term = y
    result = ZERO
    n = 1

    while abs(term) > Decimal("1e-40"):
        result += term / n
        term *= y * y
        n += 2

    return 2 * result


def log(x, base=10):
    return ln(x) / ln(base)


# ───────────── Trigonometry (Series Based) ─────────────

def sin(x):
    x = Decimal(x)
    term = x
    result = x
    n = 1
    while abs(term) > Decimal("1e-40"):
        term *= -x * x / ((2*n)*(2*n+1))
        result += term
        n += 1
    return result


def cos(x):
    x = Decimal(x)
    term = ONE
    result = ONE
    n = 1
    while abs(term) > Decimal("1e-40"):
        term *= -x * x / ((2*n-1)*(2*n))
        result += term
        n += 1
    return result


def tan(x):
    return sin(x) / cos(x)


# ───────────── Geometry ─────────────

def circumference(radius):
    r = Decimal(radius)
    return 2 * PI * r


def area_circle(radius):
    r = Decimal(radius)
    return PI * r * r


def area_square(side):
    s = Decimal(side)
    return s * s


def area_rectangle(length, breadth):
    l = Decimal(length)
    b = Decimal(breadth)
    return l * b


def area_triangle(base, height):
    return Decimal("0.5") * Decimal(base) * Decimal(height)


def perimeter_square(side):
    s = Decimal(side)
    return 4 * s


def perimeter_rectangle(length, breadth):
    l = Decimal(length)
    b = Decimal(breadth)
    return 2 * (l + b)


def distance_2d(x1, y1, x2, y2):
    dx = Decimal(x2) - Decimal(x1)
    dy = Decimal(y2) - Decimal(y1)
    return sqrt(dx*dx + dy*dy)


def cube_volume(side):
    s = Decimal(side)
    return s ** 3


def cube_surface_area(side):
    s = Decimal(side)
    return 6 * s * s


def pythagoras(a, b):
    a = Decimal(a)
    b = Decimal(b)
    return sqrt(a*a + b*b)


# ───────────── Finance & Percentages ─────────────

def percentage(part, total):
    return (Decimal(part) / Decimal(total)) * 100


def simple_interest(principal, rate, time):
    return (Decimal(principal) * Decimal(rate) * Decimal(time)) / 100


def compound_interest(principal, rate, time):
    p = Decimal(principal)
    r = Decimal(rate) / 100
    t = Decimal(time)
    return p * (ONE + r) ** t - p


# ───────────── Statistics ─────────────

def average(values):
    values = [Decimal(v) for v in values]
    return sum(values) / Decimal(len(values))


def weighted_average(values, weights):
    values = [Decimal(v) for v in values]
    weights = [Decimal(w) for w in weights]
    return sum(v*w for v, w in zip(values, weights)) / sum(weights)


# ───────────── Number Theory ─────────────

def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    a, b = int(a), int(b)
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# ───────────── Utility / Game Math ─────────────

def clamp(x, low, high):
    x = Decimal(x)
    return max(Decimal(low), min(x, Decimal(high)))


def smoothstep(x):
    x = Decimal(x)
    return x*x*(3 - 2*x)


def logistic(x, r="3.9"):
    x = Decimal(x)
    r = Decimal(r)
    return r * x * (ONE - x)

