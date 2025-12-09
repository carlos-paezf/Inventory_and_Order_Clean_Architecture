import unittest
from copy import deepcopy
from demo.mocks.products import MOCKS_PRODUCTS
from demo.mocks.orders import MOCKS_ORDERS
from domain.entities.order import OrderItem, Order

class TestOrderEntity(unittest.TestCase):
    def test_add_item(self):
        # deepcopy to not modify order from the mock list
        order: Order = deepcopy(MOCKS_ORDERS[0])
        mock_item: OrderItem = OrderItem(product = MOCKS_PRODUCTS[2], quantity = 2)

        expected: list[OrderItem] = order.items + [mock_item]

        order.add_item(mock_item.product, mock_item.quantity)

        actual = order.items

        self.assertEqual(expected, actual, "order item has not been added")

    def test_remove_item(self):
        order: Order = deepcopy(MOCKS_ORDERS[1])
        mock_item: OrderItem = OrderItem(product = MOCKS_PRODUCTS[3], quantity = 2)

        def all_except_with_product_id(item): return item.product.id != mock_item.product.id

        expected: list[OrderItem] = list(filter(all_except_with_product_id, order.items))

        order.remove_item(mock_item.product.id)

        actual = order.items

        self.assertEqual(expected, actual, "order item has not been removed")

    def test_calculate_total(self):
        order: Order = MOCKS_ORDERS[2]

        expected: float = sum(item.get_subtotal() for item in order.items)

        actual: float = order.calculate_total()

        self.assertEqual(expected, actual, "incorrect calculated total of order")

    def test_item_subtotal(self):
        product = MOCKS_PRODUCTS[4]
        quantity = 4

        item: OrderItem = OrderItem(product = product, quantity = quantity)

        expected = product.get_final_price() * quantity
        actual = item.get_subtotal()

        self.assertEqual(expected, actual, "incorrect order item subtotal")
