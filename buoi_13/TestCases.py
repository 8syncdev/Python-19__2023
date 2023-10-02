'''
    Unitest và Pytest
'''

from unittest import TestCase

# TestCase: chấm cho 1 trường hợp
# Chấm cho nhiều trường hợp: Tên_TestCases


a = 1
b = 1
import unittest

class ExpresionTestCases(TestCase):
    # tất cả hàm trong class sẽ khởi chạy
    def is_equal(self):
        self.assertEqual(a, b)

    def is_not_equal(self):
        self.assertNotEqual(a, b)


unittest.main()