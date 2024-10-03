import unittest
from calc_temp import fahrenheit_to_kelvin,kelvin_to_celsius

class TestCalcTemp(unittest.TestCase):

    def test_fahrenheit_to_kelvin(self):
        # prueba encargada de probar la conversión de 30F a Kelvin
        temp1 = 30
        temp2 = fahrenheit_to_kelvin(temp1)
        self.assertAlmostEqual(temp2, 272.04, places=2)

    def test_kelvin_to_celsius_negative(self):
        # prueba encargada de probar la conversión de -12 K a Celsius
        with self.assertRaises(ValueError) as context:
            kelvin_to_celsius(-12)
        self.assertEqual(str(context.exception), "El valor en Kelvin no puede ser negativo.")

if __name__ == '__main__':
    unittest.main()