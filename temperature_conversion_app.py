print("Welcome to the Temperature Conversion App")
#Taking user input
temp_f=float(input("\nWhat is the given temperature in degrees Fahrenheit: "))
#Converting fahrenheit into celsius and kelvin
temp_c=(temp_f - 32) * 5/9
temp_k=(temp_f - 32) * 5/9 + 273.15
#Rounding upto 4 decimal places
temp_f=round(temp_f, 4)
temp_c=round(temp_c,4)
temp_k=round(temp_k,4)
#printing the output
print("Degrees Fahrenheit:\t"+str(temp_f))
print("Degrees Celsius:\t"+str(temp_c))
print("Degrees Kelvin:\t\t"+str(temp_k))
