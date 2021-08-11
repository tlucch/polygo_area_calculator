class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def set_width(self, width):
    self.width = width
  
  def get_area(self):
    return self.width*self.height
  
  def get_perimeter(self):
    return 2*self.width + 2*self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big fo picture"
    else:
      total_lines = self.height
      while total_lines > 0:
        picture = ("*" * self.width + "\n") * self.height
      return picture
  
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, side):
    self.height = side
    self.width = side

  def set_side(self, side):
    self.height = side
    self.width = side
  
  def __str__(self):
    return f"Square(side={self.height})"

rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
