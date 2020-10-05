"""Returns a string with the classifiication of the triangle"""
def classify_triangle(a, b, c):
    """Returns a string with the classifiication of the triangle"""
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return "Invalid input"
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"
    if a >= b + c or b >= a + c or c >= a + b:
        return "Not a triangle"
    triangle_type = ""
    if a == b and a == c:
        triangle_type += "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type += "Isosceles"
    else:
        triangle_type += "Scalene"
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        triangle_type = "Right " + triangle_type
    return triangle_type
