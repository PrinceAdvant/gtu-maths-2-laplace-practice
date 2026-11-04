import unittest

import sympy as sp

from laplace_ivp_check import PRACTICE, check, solve_ivp_laplace


class TestPractice(unittest.TestCase):
    def test_all_practice_ivps(self):
        for label, a, b, f, y0, y1, expected in PRACTICE:
            with self.subTest(label):
                _, y = solve_ivp_laplace(a, b, f, y0, y1)
                self.assertEqual(sp.simplify(y - expected), 0)
                self.assertTrue(check(a, b, f, y0, y1, expected))

    def test_wrong_answer_is_rejected(self):
        t = sp.Symbol("t", positive=True)
        self.assertFalse(check(0, 4, 0, 1, 2, sp.cos(2 * t)))


if __name__ == "__main__":
    unittest.main()
