# Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temper-
# ature is in. Your program should convert the temperature to the other unit.


temperature = float(input("enter your temperature: "))
Unit = input("the unit(Celsius/fahrenheit: ")
if Unit.upper() == "Celsius":
    new_temperature = (9/5) * temperature + 32
    print(f"{new_temperature} F ")

elif Unit.lower() == "fah":
    new_temperature = (5/9) * (temperature - 32)
    print(new_temperature)

else:
    print("invalid unit")
