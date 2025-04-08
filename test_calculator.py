import unittest
from main import calculate_bmr, calculate_tdee

class TestBMRCaculator(unittest.TestCase):

    def test_calculate_bmr_male_basic(self):
        # Перевіряємо базове обчислення BMR для чоловіка.
        # Вхідні дані: вага 80 кг, зріст 180 см, вік 35 років, стать 1.
        # Очікуваний результат: 10 * 80 + 6.25 * 180 - 5 * 35 + 5 = 1755 ккал.
        result = calculate_bmr(80, 180, 35, 1)
        expected = 10 * 80 + 6.25 * 180 - 5 * 35 + 5
        self.assertEqual(result, expected)

    def test_calculate_bmr_female_basic(self):
        # Перевіряємо базове обчислення BMR для жінки.
        # Вхідні дані: вага 55 кг, зріст 160 см, вік 28 років, стать 2.
        # Очікуваний результат: 10 * 55 + 6.25 * 160 - 5 * 28 - 161 = 1249 ккал.
        result = calculate_bmr(55, 160, 28, 2)
        expected = 10 * 55 + 6.25 * 160 - 5 * 28 - 161
        self.assertEqual(result, expected)

    def test_calculate_bmr_invalid_gender(self):
        # Перевіряємо, чи викликається помилка ValueError при некоректній статі.
        # Вхідні дані: вага 70 кг, зріст 175 см, вік 30 років, стать 3.
        # Очікуваний результат: виняток ValueError з повідомленням.
        with self.assertRaises(ValueError) as context:
            calculate_bmr(70, 175, 30, 3)
        self.assertEqual(str(context.exception), "Стать має бути 1 (чоловік) або 2 (жінка)")

    def test_calculate_tdee_sedentary(self):
        # Перевіряємо обчислення TDEE для сидячого способу життя.
        # Вхідні дані: BMR = 1500, рівень активності 1.
        # Очікуваний результат: 1500 * 1.2 = 1800 ккал.
        result = calculate_tdee(1500, 1)
        self.assertEqual(result, 1500 * 1.2)

    def test_calculate_tdee_very_active(self):
        # Перевіряємо обчислення TDEE для дуже активного рівня.
        # Вхідні дані: BMR = 2000, рівень активності 5.
        # Очікуваний результат: 2000 * 1.9 = 3800 ккал.
        result = calculate_tdee(2000, 5)
        self.assertEqual(result, 2000 * 1.9)

    def test_calculate_tdee_invalid_activity_level(self):
        # Перевіряємо, чи викликається помилка ValueError при некоректному рівні активності.
        # Вхідні дані: BMR = 1600, рівень активності 6.
        # Очікуваний результат: виняток ValueError з повідомленням.
        with self.assertRaises(ValueError) as context:
            calculate_tdee(1600, 6)
        self.assertEqual(str(context.exception), "Некоректний рівень активності")

    def test_calculate_bmr_negative_weight(self):
        # Перевіряємо, чи викликається помилка ValueError при від’ємній вазі.
        # Вхідні дані: вага -10 кг, зріст 170 см, вік 25 років, стать 1.
        # Очікуваний результат: виняток ValueError з повідомленням.
        with self.assertRaises(ValueError) as context:
            calculate_bmr(-10, 170, 25, 1)
        self.assertEqual(str(context.exception), "Вага має бути більшою за 0")

    def test_calculate_bmr_zero_height(self):
        # Перевіряємо, чи викликається помилка ValueError при нульовому зрості.
        # Вхідні дані: вага 60 кг, зріст 0 см, вік 30 років, стать 2.
        # Очікуваний результат: виняток ValueError з повідомленням.
        with self.assertRaises(ValueError) as context:
            calculate_bmr(60, 0, 30, 2)
        self.assertEqual(str(context.exception), "Зріст має бути більшим за 0")

    def test_calculate_bmr_negative_age(self):
        # Перевіряємо, чи викликається помилка ValueError при від’ємному віці.
        # Вхідні дані: вага 70 кг, зріст 175 см, вік -5 років, стать 1.
        # Очікуваний результат: виняток ValueError з повідомленням.
        with self.assertRaises(ValueError) as context:
            calculate_bmr(70, 175, -5, 1)
        self.assertEqual(str(context.exception), "Вік має бути більшим за 0")

    def test_calculate_bmr_elderly_female(self):
        # Перевіряємо обчислення BMR для літньої жінки.
        # Вхідні дані: вага 50 кг, зріст 150 см, вік 70 років, стать 2.
        # Очікуваний результат: 10 * 50 + 6.25 * 150 - 5 * 70 - 161 = 926.5 ккал.
        result = calculate_bmr(50, 150, 70, 2)
        expected = 10 * 50 + 6.25 * 150 - 5 * 70 - 161
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()