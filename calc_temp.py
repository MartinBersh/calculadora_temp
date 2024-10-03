def celsius_to_fahrenheit(c):
    #Función encargada de convertir Celclius a Fahreinheit
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    #Función encargada de convertir Celicius a Kelvin
    return c + 273.15

def fahrenheit_to_celsius(f):
    #Función encargada de convertir Fahreinheit a Celcius
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    #Función encargada de convertir Fahreinheit a Kelvin
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    #función encargada de convertir Kelvin a Celcius
    if k < 0:
        raise ValueError("El valor en Kelvin no puede ser negativo.")
    return k - 273.15

def kelvin_to_fahrenheit(k):
    #función encargada de convertir Kelvin a Fahreinheit
    if k < 0:
        raise ValueError("El valor en Kelvin no puede ser negativo.")
    return (k - 273.15) * 9/5 + 32
