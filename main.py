# Welcoming Statement
print("Welcome to the Area and Volume of Shapes Calculator! Version 1.0\n")
# Input statement
shape = float(input(
    "Which shapes' area or volume would you like to calculate? (in cm.)\n\nArea of Square(1) or Volume of Cube("
    "10)\nArea of Circle(2) or Volume of Sphere(20)\nArea of Rectangle(3) or Volume of Rectangular Prism(30)\nArea of "
    "Triangle(4) or Volume of Triangular Prism(40)\nArea of Trapezoid(5) or Volume of Trapezoidal Prism(50)\n\n"))


# Square Area Function
def squarea():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    squarearea = base * height
    print "Area =", squarearea, "cm.^2"


# Square Volume Function
def squvol():
    base = float(input("Enter base: "))
    squvol = base ** 3
    print "Volume =", squvol, "cm.^3"


# Circle Area Function
def circarea():
    radius = float(input("Enter radius: "))
    circlearea = 3.141592654 * (radius ** 2)
    print "Area =", circlearea, "cm.^2"


# Circle Volume Function
def circvol():
    radius = float(input("Enter radius: "))
    circvol = (4 / 3) * 3.141592654 * (radius ** 3)
    print "Volume =", circvol, "cm.^3"


# Rectangle Area Function
def rectarea():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    rectarea = base * height
    print "Area =", rectarea, "cm.^2"


# Rectangle Volume Function
def rectvol():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    depth = float(input("Enter depth: "))
    rectvol = base * height * depth
    print "Volume =", rectvol, "cm.^3"


# Triangle Area Function
def triarea():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    triarea = ((base * height) / 2)
    print "Area =", triarea, "cm.^2"


# Triangle Volume Function
def trivol():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    length = float(input("Enter height: "))
    trivol = ((base * height * length) / 2)
    print "Volume =", trivol, "cm.^3"


# Trapezoid Area Function
def traparea():
    base1 = float(input("Enter base #1: "))
    base2 = float(input("Enter base #2: "))
    height = float(input("Enter height: "))
    traparea = (((base1 + base2) * height) / 2)
    print "Area =", traparea, "cm.^2"


# Trapezoid Volume Function
def trapvol():
    base1 = float(input("Enter base #1: "))
    base2 = float(input("Enter base #2: "))
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))
    trapvol = ((((base1 + base2) * height) / 2) * length)
    print "Volume =", trapvol, "cm.^3"


# Area of a Square
if int(shape) == 1:
    squarea()

# Volume of a Square
if int(shape) == 10:
    squvol()

# Area of a Circle
if int(shape) == 2:
    circarea()

# Volume of a Circle
if int(shape) == 20:
    circvol()

# Area of a Rectangle
if int(shape) == 3:
    rectarea()

# Volume of a Rectangle
if int(shape) == 30:
    rectvol()

# Area of a Triangle
if int(shape) == 4:
    triarea()

# Volume of a Triangle
if int(shape) == 40:
    trivol()

# Area of a Trapezoid
if int(shape) == 5:
    traparea()

# Volume of a Trapezoid
if int(shape) == 50:
    trapvol()