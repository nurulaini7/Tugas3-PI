"""
Nama : Nurul Aini
NIM : 221402005

Soal 2 = Write a class that calculates and stores the height and weight of a person in metric. The file should be named lab.py.  
"""

class BmiCalculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def get_bmi(self):
        return self.weight / (self.height**2)

    def is_equal(self, other):
        return self.weight == other.weight and self.height == other.height


bmi1 = BmiCalculator(70, 1.75)
bmi2 = BmiCalculator(65, 1.7)
bmi3 = BmiCalculator(70, 1.75)
print(bmi1.is_equal(bmi2))
print(bmi1.is_equal(bmi3))
