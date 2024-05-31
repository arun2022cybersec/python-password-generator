import unittest
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_easy_complexity(self):
        pg_easy = PasswordGenerator(10, 'easy', False)
        password = pg_easy.generate()
        self.assertEqual(len(password), 10)
        self.assertTrue(all(c in "abcdefghijklmnopqrstuvwxyz" for c in password))

    def test_medium_complexity(self):
        pg_medium = PasswordGenerator(15, 'medium', False)
        password = pg_medium.generate()
        self.assertEqual(len(password), 15)
        self.assertTrue(all(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in password))

    def test_hard_complexity(self):
        pg_hard = PasswordGenerator(20, 'hard', True)
        password = pg_hard.generate()
        self.assertEqual(len(password), 20)
        self.assertTrue(all(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for c in password))

    def test_extreme_complexity(self):
        pg_extreme = PasswordGenerator(25, 'extreme', True)
        password = pg_extreme.generate()
        self.assertEqual(len(password), 25)
        self.assertTrue(all(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for c in password))

    def test_periodicity(self):
        pg_periodic = PasswordGenerator(16, 'medium', True)
        password = pg_periodic.generate()
        # Since it is periodic, it should have a repeated substring
        self.assertTrue(any(password[i:i+2] in password for i in range(len(password)-2)))

    def test_no_periodicity(self):
        pg_non_periodic = PasswordGenerator(16, 'medium', False)
        password = pg_non_periodic.generate()
        # Since it is non-periodic, it should not have any repeated substring
        self.assertFalse(any(password[i:i+2] in password[i+2:] for i in range(len(password)-2)))

if __name__ == '__main__':
    unittest.main()
