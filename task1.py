"""
Nama : Nurul Aini
Nim : 221402005 

soal 1 : Write a program that reads in integer numbers from a text file named indata.txt in the same directory as the executing program.  
Print the sum of the numbers with comma separators and two digits.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'indata.txt')

with open(file_path, 'r') as file:
    data = [int(line) for line in file.readlines()]

sum_data = sum(data)
print(f'{sum_data:.2f}')