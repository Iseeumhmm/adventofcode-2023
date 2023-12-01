
import re

str_digits = dict(one='1', two='2', three='3', four='4', five='5', six='6',  seven='7', eight='8', nine='9')
pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"

def get_input():
         with open('./input.txt') as f: return [line.strip() for line in f.readlines()]
       
def get_digits(line):
       digits = list(map(lambda x: x if x.isdigit() else str_digits[x], re.findall(pattern, line)))
       return int(digits[0] + digits[-1])

def get_calibration(lines):
       total = 0
       for line in lines:
              total += get_digits(line)
       return total

'''
Day 1: Trebuchet?!
'''

print(get_calibration(get_input()))