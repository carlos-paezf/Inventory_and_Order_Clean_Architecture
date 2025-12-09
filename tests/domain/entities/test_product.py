import unittest
from domain.entities.product import BookProduct, AccessoryProduct
from demo.mocks.products import MOCKS_PRODUCTS

class TestProductEntity(unittest.TestCase):
    def test_book_final_price(self):
        product: BookProduct = MOCKS_PRODUCTS[0]

        expected = product.price * 0.9
        actual = product.get_final_price()

        self.assertEqual(expected, actual, "incorrect book final price")

    def test_accessory_final_price(self):
        product: AccessoryProduct = MOCKS_PRODUCTS[1]

        expected = product.price
        actual = product.get_final_price()

        self.assertEqual(expected, actual, "incorrect product final price")
