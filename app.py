import unittest

def add(a,b):
  return a + b 
def subtract(a,b):
  return a - b

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(20,50),70)
  def test_subtract(self):
    self.assertEqual(subtract(30,10),20)
  
if __name__ == "__main__":
  print("Student Calculator Application")
  print("Addition:", add(20,20))
  print("Subtraction:", subtract(20,10))
  
  
  unittest.main(argv=['first-arg-is-ignored'],exit = False) 
