"""
Your fuel is running out and the nearest pump is 50 miles away!
You know that on average, your car runs on about 25 miles per gallon.
There are 2 gallons left.
Write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not.
MATHEMATICSFUNDAMENTALS
"""
#
def zero_fuel(distance_to_pump, mpg, fuel_left):
    # distance_to_pump = 50     # mpg = 25     # fuel_left = 2
    if (mpg * fuel_left) >= distance_to_pump:
        return True
    return False

#works:
def zero_fuel(distance_to_pump, mpg, fuel_left):
    # distance_to_pump = 50     # mpg = 25     # fuel_left = 2
    return mpg * fuel_left >= distance_to_pump
