class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero") 

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be grater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width Deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height Deleted")

rectangle = Rectangle(3, 4)

rectangle.width = 6
rectangle.height = 8

# del rectangle.width
# del rectangle.height

print(rectangle._width)
print(rectangle._height)