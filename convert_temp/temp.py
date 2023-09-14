#convert_temp.py

"""A python library to help you in temperature conversions"""

#FUNCTIONS

def to_centigrade(x):
    
    """Returns: x converted to centigrade"""
    return 5*(x-32)/9.0


def to_farenheit(x):
    """Returns: x converted to farenheit"""
    return 9*x/5.0 + 32

#CONSTANTS

FREEZING_C = 0.0 #Water freezing temp in celcius
FREEZING_F = 32.0 #water freezing point in farenheit