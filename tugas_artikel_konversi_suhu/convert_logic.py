def celcius(input_suhu):
        fahrenheit = (input_suhu * 9/5) + 32
        kelvin = input_suhu + 273.15
        return {
                fahrenheit : fahrenheit,
                kelvin : kelvin
        }