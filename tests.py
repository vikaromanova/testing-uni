import unittest
from task import Methods

# в unittest тест-кейс должен быть реализован в виде класса,
# наследованного от unittest.TestCase
class TestMethods(unittest.TestCase):
  # подготовка для прогона теста, вызывается перед каждым тестом
  def setUp(self):
    self.methods = Methods()
  # проверки работы функции degree класса Methods
  def test1_degree(self):
    res = self.methods.degree(4, [1, 5, 25, 125])
    self.assertEqual(res, 4)
  def test2_degree(self):
    res = self.methods.degree(2, [1, 5])
    self.assertEqual(res, 2)
  # проверки работы функции isPrime класса Methods
  def test1_is_prime(self):
    self.assertTrue(self.methods.is_prime(7))
  def test2_is_prime(self):
    self.assertFalse(self.methods.is_prime(8))
  def test3_is_prime(self):
    self.assertTrue(self.methods.is_prime(13))


if __name__ == "__main__":
  # запуск тестов
  unittest.main()
