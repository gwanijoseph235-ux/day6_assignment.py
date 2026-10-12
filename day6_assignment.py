# BMI Calculator.
def calculate_bmi(weight_kg: float, height_m: float) -> float:
     return weight_kg / (height_m * height_m)


# Rectangle Area Calculator.
def calculate_rectangle_area(lenght: float, width: float): 
       return (lenght * width)
   

# Celcius to Fahrenheit converter.
def celcius_to_fahrenheit(celcius: float):
      return (celcius * 9 / 5) + 32

# Functions calls and Results

# BMI function test.
bmi = calculate_bmi(90, 1.75)
print(f"BMI: {bmi:.2f}")

# Rectangle Area Function test.
area = calculate_rectangle_area(20, 5)
print(F"Rectangle Area: {area}")

#Celcius to Fahrenheit Function test.
fahrenheit = celcius_to_fahrenheit(60)
print(f"Temperature in Fahrenheit: {fahrenheit}°F")