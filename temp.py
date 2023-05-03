
unit = input("Is this Tempreture in Celcuis or Farenheit (C/F): ")
temp = float(input("Enter the tempreture: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The tempreture in Farenheit is: {temp}F")
elif unit == "F":
    temp = round((temp - 32) + 5 / 9, 1)
    print(f"The tempreture in celcuis is: {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")