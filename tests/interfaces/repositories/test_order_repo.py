import unittest
from interfaces.repositories.order_repo import OrderRepository
from demo.mocks.orders import MOCKS_ORDERS

class NotTested:
    class TestOrderRepository(unittest.TestCase):
        repository: OrderRepository

        def tearDown(self):
            self.repository = None

        def test_save_order(self):
            expected = MOCKS_ORDERS[0]

            self.assertNotIn(expected, self.repository.list_all(), "order to add is already in the list")

            self.repository.save(expected)
            actual = self.repository.get(expected.id)

            # Check attributes
            self.assertEqual(expected.id, actual.id, "incorrect order id")
            self.assertEqual(expected.items, actual.items, "incorrect order items")

            # Is created order in the list?
            self.assertIn(expected, self.repository.list_all(), "expected product is not in the list")

        def test_delete_order(self):
            expected = MOCKS_ORDERS[1]

            self.assertNotIn(expected, self.repository.list_all(), "order to delete is already in the list")

            self.repository.save(expected)

            self.assertIn(expected, self.repository.list_all(), "expected order is not in the list")

            isRemoved = self.repository.delete(expected.id)

            self.assertTrue(isRemoved, "failed to remove order")

            self.assertNotIn(expected, self.repository.list_all(), "deleted order is still in the list")

            self.assertIsNone(self.repository.get(expected.id), "removed order is still indexable")
