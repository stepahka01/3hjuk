class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5, 6)
point3 = Point3D(7, 8, 9)

print("Point 1:", point1)
print("Point 2:", point2)
print("Point 3:", point3)

point1.z = 10

print("\nAfter modifying Point3D class:")
print("Point 1:", point1)
print("Point 2:", point2)
print("Point 3:", point3)

point2.x = 100

print("\nAfter modifying Point3D instance (point2):")
print("Point 1:", point1)
print("Point 2:", point2)
print("Point 3:", point3)


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length


side_length = 5
square = Square(side_length)
area = square.calculate_area()
perimeter = square.calculate_perimeter()

print(f"Square area: {area}")
print(f"Square perimeter: {perimeter}")

import math


class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.hypotenuse = math.sqrt(a ** 2 + b ** 2)

    def calculate_area(self):
        area = 0.5 * self.a * self.b
        return area

    def calculate_perimeter(self):
        perimeter = self.a + self.b + self.hypotenuse
        return perimeter


triangle = Triangle(3, 5)
area = triangle.calculate_area()
perimeter = triangle.calculate_perimeter()

print(f"Triangle area: {area}")
print(f"Triangle perimeter: {perimeter}")

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def perimeter(self):
        side_ab = self.point_a.distance_to(self.point_b)
        side_bc = self.point_b.distance_to(self.point_c)
        side_ca = self.point_c.distance_to(self.point_a)
        return side_ab + side_bc + side_ca


point_a = Point(2, 4)
point_b = Point(6, 9)
point_c = Point(6, 0)

triangle = Triangle(point_a, point_b, point_c)
perimeter = triangle.perimeter()

print("Triangle ABC perimeter:", perimeter)

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def perimeter(self):
        side_ab = self.point_a.distance_to(self.point_b)
        side_bc = self.point_b.distance_to(self.point_c)
        side_ca = self.point_c.distance_to(self.point_a)
        return side_ab + side_bc + side_ca


point_a = Point(2, 4)
point_b = Point(6, 9)
point_c = Point(6, 0)

triangle = Triangle(point_a, point_b, point_c)
perimeter = triangle.perimeter()

print("Triangle ABC perimeter:", perimeter)


class CPerson:
    def __init__(self, first_name, last_name, middle_name, birth_day, birth_month, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.gender = gender

    def update_info(self, first_name, last_name, middle_name, birth_day, birth_month, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.gender = gender

    def get_info(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}, Birth Date: {self.birth_day}.{self.birth_month}.{self.birth_year}, Gender: {self.gender}"

    def __del__(self):
        print(f"Object {self.get_info()} deleted")


person1 = CPerson("Иван", "Иванов", "Иванович", 15, 7, 1990, "Мужской")
person2 = CPerson("Мария", "Петрова", "Сергеевна", 25, 4, 1985, "Женский")

person1.update_info("Петр", "Сидоров", "Петрович", 10, 12, 1988, "Мужской")
print(person1.get_info())

person2.update_info("Анна", "Смирнова", "Алексеевна", 5, 9, 1992, "Женский")
print(person2.get_info())


class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receive_call(self, caller_name):
        print(f"Call from {caller_name}")

    def get_number(self):
        return self.number


phone1 = Phone("+1234567890", "Poko", 160)
phone2 = Phone("+9876543210", "Samsung", 175)
phone3 = Phone("+1112233444", "Google", 150)

print(f"Phone 1: Number - {phone1.number}, Model - {phone1.model}, Weight - {phone1.weight}")
print(f"Phone 2: Number - {phone2.number}, Model - {phone2.model}, Weight - {phone2.weight}")
print(f"Phone 3: Number - {phone3.number}, Model - {phone3.model}, Weight - {phone3.weight}")

phone1.receive_call("John")
phone2.receive_call("Alice")
phone3.receive_call("Bob")

print(f"Phone 1 number: {phone1.get_number()}")
print(f"Phone 2 number: {phone2.get_number()}")
print(f"Phone 3 number: {phone3.get_number()}")


class Reader:
    def __init__(self, full_name, ticket_number, faculty, birth_date, phone):
        self.full_name = full_name
        self.ticket_number = ticket_number
        self.faculty = faculty
        self.birth_date = birth_date
        self.phone = phone

    def takeBook(self, book_count):
        print(f"{self.full_name} took {book_count} books")

    def returnBook(self, book_count):
        print(f"{self.full_name} returned {book_count} books")


reader1 = Reader("Петров В. В.", "12345", "Информатика", "01.01.1990", "123-456-7890")
reader1.takeBook(3)
reader1.returnBook(2)