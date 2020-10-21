#!/usr/bin/env python3.9

# BMI : weight / (height squared)
# Imperial BMI : 703 * (weight / (height squared))

def gather_info():
    height = float(input("What is you height? (inches or meters): "))
    weight = float(input("What is you weight? (pounds or kilograms): "))
    system = input("What is the measurement system? (metric or imperial): ")
    return (height, weight, system)

def calculate_bmi(height, weight, system='metric'):
    if system == 'metric':
        bmi = weight / (height ** 2)
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(height, system='imperial', weight=weight)
        print(f"bmi is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(height, system='metric', weight=weight)
        print(f"bmi is {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")
