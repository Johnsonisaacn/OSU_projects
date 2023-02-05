# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 01/18/2023
# Description: Test cases for classes that keep track of sales and inventory of a lemonade stand

import unittest
from LemonadeStand import InvalidSalesItemError, MenuItem, LemonadeStand, SalesForDay

class TestStands(unittest.TestCase):
    """this class contains unit tests for classes in the Lemonade Stand file"""

    def test_1(self):
        """tests get_name, get_wholesale_cost, and get_selling_price in class MenuItem"""

        item_1 = MenuItem("Cherry Pie", .8, 3.25)
        self.assertEqual(item_1.get_name(), "Cherry Pie")
        self.assertAlmostEqual(item_1.get_wholesale_cost(), .8)
        self.assertAlmostEqual(item_1.get_selling_price(), 3.25)

    def test_2(self):
        """tests class SalesForDay"""

        day_1_sales = {"Cherry Pie":100, "Coffee":200}
        day_1_sales_object = SalesForDay(1, day_1_sales)
        self.assertEqual(day_1_sales_object.get_day(), 1)
        self.assertEqual(day_1_sales_object.get_sales_dict()["Cherry Pie"],100)

    def test_3(self):
        """tests get_name function in class LemonadeStand"""

        stand_1 = LemonadeStand("Double R")
        self.assertEqual(stand_1.get_name(), "Double R")

    def test_4(self):
        """tests total_sales_for_menu_item in class LemonadeStand"""

        stand_1 = LemonadeStand("Double R")
        item_1 = MenuItem("Cherry Pie", .8, 3.25)
        item_2 = MenuItem("Coffee", .4, 2)
        day_0_sales = {"Cherry Pie": 100, "Coffee": 200}
        stand_1.add_menu_item(item_1)
        stand_1.add_menu_item(item_2)
        stand_1.enter_sales_for_today(day_0_sales)
        self.assertEqual(stand_1.total_sales_for_menu_item(item_1), 100)

    def test_5(self):
        """tests total_profit_for_stand in class LemonadeStand"""





