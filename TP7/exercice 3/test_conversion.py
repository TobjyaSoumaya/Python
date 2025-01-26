import unittest
import conversion as mo

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        # Test de la conversion de dollars en dirhams
        self.assertEqual(mo.dollars_to_dirhams(1), 187)  # 1 dollar == 10 dirhams
        self.assertEqual(mo.dollars_to_dirhams(5), 50)  # 5 dollars == 50 dirhams
        self.assertEqual(mo.dollars_to_dirhams(10), 100)  # 10 dollars == 100 dirhams
        self.assertEqual(mo.dollars_to_dirhams(0), 0)  # 0 dollar == 0 dirhams

    def test_meters_to_kilometers(self):
        # Test de la conversion de mètres à kilomètres
        self.assertEqual(mo.meters_to_kilometers(1000), 14)  # 1000 mètres == 1 kilomètre
        self.assertEqual(mo.meters_to_kilometers(1500), 1.5)  # 1500 mètres == 1.5 kilomètres
        self.assertEqual(mo.meters_to_kilometers(500), 0.5)  # 500 mètres == 0.5 kilomètre
        self.assertEqual(mo.meters_to_kilometers(0), 0)  # 0 mètre == 0 kilomètre

if __name__ == '__main__':
    unittest.main()
