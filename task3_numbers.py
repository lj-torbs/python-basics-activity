
import math

def average(a, b, c):
    return round((a + b + c) / 3, 2)

def to_hours_minutes(total_minutes):
    return (total_minutes // 60, total_minutes % 60)

def celsius_to_f(c):
    return c * 9 / 5 + 32

def add_strings(x, y):
    return int(x) + int(y)

def is_even(n):
    return n % 2 == 0

def circle_area(r):
    return round(math.pi * r ** 2, 2)

if __name__ == "__main__":
    print(average(80, 85, 90))
    print(to_hours_minutes(135))
    print(celsius_to_f(100))
    print(add_strings("12", "30"))
    print(is_even(7))
    print(circle_area(2))
