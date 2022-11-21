class Person:
  def __init__(self, name=None, age=None):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Name:{self.name} Age:({self.age})"

p1 = Person(age=36)

print(p1.name)
print(p1)