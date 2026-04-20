def equilateral(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a == b == c:
        return True
    else:
        return False


def isosceles(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if (a == b and a + b>= c) or (b == c and b + c >= a) or (a == c and a + c>= b) or (a == b == c):
        return True
    else:
        return False


def scalene(sides):
    a, b, c = sides
    if (a == 0 or b == 0 or c == 0) or (a + b < c or a + c < b or b + c < a):
        return False
    if (a != b and a != c and b != c):
        return True
    else:
        return False
