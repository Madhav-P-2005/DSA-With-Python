# Q6) Write a Program to convert Temperature from Celsius to Fahrenheit ?   --> My logic 
Celsius_Temperature = float(input("Enter your Temperature in Celsius :- "))

Fahrenheit_Temperature =  9 * (Celsius_Temperature/5) + 32

print(f"Converted Celsius {Celsius_Temperature}ᴼC to Fahrenheit Temperature :-  {Fahrenheit_Temperature}ᴼF")


'''

Output :- 

Enter your Temperature in Celsius :- 23
Converted Celsius 23.0ᴼC to Fahrenheit Temperature :-  73.4ᴼF

'''



# Q6) Write a Program to convert Temperature from Fahrenheit to Celsius  ?   --> My logic 
Fahrenheit_Temperature = float(input("Enter your Temperature in Fahrenheit :- "))

Celsius_Temperature =  (Fahrenheit_Temperature - 32)  * (5/9)

print(f"Converted Fahrenheit {Fahrenheit_Temperature}ᴼF to Celsius Temperature :-  {Celsius_Temperature}ᴼC")


'''

Output :- 

Enter your Temperature in Fahrenheit :- 73.4
Converted Fahrenheit 73.4ᴼF to Celsius Temperature :-  23.000000000000004ᴼC

'''



# Q6) Write a Program to convert Temperature from Celsius to Fahrenheit Using Functions  ?   --> My logic 

def Calculate_Fahrenheit(Celsius_Temperature):
   Fahrenheit_Temperature =  9 * (Celsius_Temperature/5) + 32
   return Fahrenheit_Temperature



Celsius_Temperature = float(input("Enter your Temperature in Celsius :- "))
print(f"Converted Celsius {Celsius_Temperature}ᴼC to Fahrenheit Temperature :-  {Calculate_Fahrenheit(Celsius_Temperature)}ᴼF")


'''

Output :- 

Enter your Temperature in Celsius :- 0
Converted Celsius 0.0ᴼC to Fahrenheit Temperature :-  32.0ᴼF

'''


# Q6) Write a Program to convert Temperature from Fahrenheit to Celsius Using Functions ?   --> My logic 

def Calculate_Celsius(Fahrenheit_Temperature):
   Celsius_Temperature  = (Fahrenheit_Temperature - 32) * (5/9)
   return Celsius_Temperature


Fahrenheit_Temperature = float(input("Enter your Temperature in Fahrenheit :- "))
print(f"Converted Fahrenheit {Fahrenheit_Temperature}ᴼF to Celsius Temperature :-  {Calculate_Celsius(Fahrenheit_Temperature)}ᴼC")


'''

Output :- 

Enter your Temperature in Fahrenheit :- 73.4 
Converted Fahrenheit 73.4ᴼF to Celsius Temperature :-  23.000000000000004ᴼC

'''