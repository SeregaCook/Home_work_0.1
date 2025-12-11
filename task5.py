class Rectangle:
    """Прямоугольник с шириной и высотой."""
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def info(self) -> str:
        return (f"Прямоугольник: width={self.width}, height={self.height}, "
                f"area={self.area()}, perimeter={self.perimeter()}")
