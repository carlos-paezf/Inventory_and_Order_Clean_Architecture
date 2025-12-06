import unittest
from interfaces.repositories.inventory_repo import InventoryRepository
from demo.mocks.products import MOCKS_PRODUCTS

class TestInventoryRepository(unittest.TestCase):
    repository: InventoryRepository

    def tearDown(self):
        self.repository.dispose()
        self.repository = None

    def test_add_product(self):
        expected = MOCKS_PRODUCTS[0]

        self.assertNotIn(expected, self.repository.list_products(), "product to add is already in the list")

        self.repository.add_product(expected)
        actual = self.repository.get_product(expected.id)

        # Check attributes
        self.assertEqual(expected.id, actual.id, "incorrect product id")
        self.assertEqual(expected.name, actual.name, "incorrect product name")
        self.assertEqual(expected.price, actual.price, "incorrect product price")
        self.assertEqual(expected.category, actual.category, "incorrect product category")

        # Is created product in the list?
        self.assertIn(expected, self.repository.list_products(), "expected product is not in the list")

    def test_remove_product(self):
        expected = MOCKS_PRODUCTS[1]

        self.assertNotIn(expected, self.repository.list_products(), "product to remove is already in the list")

        self.repository.add_product(expected)

        self.assertIn(expected, self.repository.list_products(), "expected product is not in the list")

        isRemoved = self.repository.remove_product(expected.id)

        self.assertTrue(isRemoved, "failed to remove product")

        self.assertNotIn(expected, self.repository.list_products(), "removed product is still in the list")

        self.assertIsNone(self.repository.get_product(expected.id), "removed product is still indexable")
    def test_add_existing_product_id_raises_error(self):
        existing = MOCKS_PRODUCTS[2]
        self.repository.add_product(existing)

        expected = MOCKS_PRODUCTS[4]

        # Have the same ID to raise error
        expected.id = existing.id

        with self.assertRaises(ValueError):
            self.repository.add_product(expected)

        
