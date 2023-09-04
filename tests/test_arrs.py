import unittest
from utils import arrs

class TestArrs(unittest.TestCase):

    def test_get_existing_index(self):
        # Проверяем, что функция возвращает элемент по указанному существующему индексу
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)

    def test_get_default_value(self):
        # Проверяем, что функция возвращает значение по умолчанию, если индекс не существует
        self.assertEqual(arrs.get([], 0, "test"), "test")

        # Проверяем, что функция возвращает значение по умолчанию, если индекс меньше нуля
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")

        # Проверяем, что функция возвращает значение по умолчанию, если индекс больше длины списка
        self.assertEqual(arrs.get([1, 2, 3], 3, "test"), "test")

    def test_slice_with_indices(self):
        # Проверяем, что функция возвращает подсписок с указанными индексами
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])

    def test_slice_without_end_index(self):
        # Проверяем, что функция работает правильно, если не указан конечный индекс
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])

    def test_slice_with_end_index(self):
        # Проверяем, что функция работает правильно, если указан конечный индекс
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, 4), [2, 3, 4])

    def test_slice_empty_list(self):
        # Проверяем, что функция возвращает пустой список, если исходный список пуст
        self.assertEqual(arrs.my_slice([], 0, 2), [])

    def test_get_empty_list(self):
        # Проверяем, что функция возвращает значение по умолчанию, если список пустой
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_get_negative_index(self):
        # Проверяем, что функция возвращает значение по умолчанию, если индекс меньше -len(array)
        self.assertEqual(arrs.get([1, 2, 3], -4, "test"), "test")

    def test_slice_negative_start_index(self):
        # Проверяем, что функция работает правильно, если указан отрицательный стартовый индекс
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3), [3, 4, 5])

    def test_slice_negative_end_index(self):
        # Проверяем, что функция работает правильно, если указан отрицательный конечный индекс
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 0, -2), [1, 2, 3])

    def test_get_index_beyond_length(self):
        # Проверяем, что функция возвращает значение по умолчанию, если индекс больше длины списка
        self.assertEqual(arrs.get([1, 2, 3], 5, "test"), "test")

    def test_get_negative_index_beyond_length(self):
        # Проверяем, что функция возвращает значение по умолчанию, если индекс меньше -len(array)
        self.assertEqual(arrs.get([1, 2, 3], -4, "test"), "test")



