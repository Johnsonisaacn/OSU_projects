# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 01/18/2023
# Description: Classes that keep track of sales and inventory of a lemonade stand

class InvalidSalesItemError(Exception):
    """handles exceptions for sales of items that aren't
    included in the menu"""

    pass

class MenuItem():
    """this class creates menu item objects with names, cost, and price and can return these values
    """

    def __init__(self, name, wholesale_cost, selling_price):
        """initializes menu item objects with a name, cost, and selling price"""
        self._name = str(name)
        self._wholesale_cost = float(wholesale_cost)
        self._selling_price = float(selling_price)

    def get_name(self):
        """returns name of menu item object"""
        return self._name

    def get_wholesale_cost(self):
        """returns the wholesale cost of the menu item object"""
        return self._wholesale_cost

    def get_selling_price(self):
        """returns the price at which the item is sold"""
        return self._selling_price

class SalesForDay():
    """this class creates sales for day objects that keeps track of sales for a given day"""

    def __init__(self, day, sales_dict):
        """initializes number of days open and sales dictionary for a sales for day object"""
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """returns the day of operation"""
        return self._day

    def get_sales_dict(self):
        """returns the sales dictionary of the sales for day object with the menu items and number of each sold"""
        return self._sales_dict

class LemonadeStand():
    """this class creates lemonade stand objects with names, number of days open, sales for the day, and menu items"""

    def __init__(self, name):
        """initializes the lemonade stand object with a name passed as a parameter, an empty menu items dictionary, an
        empty menu dictionary, and initializes the date since open to 0"""
        self._name = name
        self._day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        """returns the name of the lemonade stand"""
        return self._name

    def add_menu_item(self, menu_item):
        """takes a MenuItem object as a parameter and adds it to the menu dictionary"""
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """Takes as a parameter a dictionary where the keys are names of items sold and the corresponding values are
        how many of the item were sold """
        counter = 0
        #couldn't find a more elegant way to loop over menu items and still
        #be able to raise exception
        for menu_item in sales_dict.keys():
            if menu_item in self._menu.keys():
                counter += 0
            else:
                counter += 1
        if counter > 0:
            raise InvalidSalesItemError
        else:
            self._sales_record.append(SalesForDay(self._day, sales_dict))
            self._day += 1

    def sales_of_menu_item_for_day(self, day, menu_item):
        """takes a day and menu item as parameters and returns the number of that menu item
        sold on a specific day"""
        for sale in self._sales_record:
            if sale.get_day() == day:
                if menu_item in sale.get_sales_dict():
                    return sale.get_sales_dict()[menu_item]
                else:
                    print("There were no sales of", menu_item,"on day", day)


    def total_sales_for_menu_item(self, menu_item):
        """takes a menu item as a parameter and returns the total number of that item sold
        since the opening of the stand"""

        total = 0
        for day in range(0,self._day):
            total += self.sales_of_menu_item_for_day(day, menu_item)
        return total

    def total_profit_for_menu_item(self, menu_item):
        """takes as a parameter the name of a menu item and returns the total profit on that item over
        the history of the stand"""
        if menu_item in self._menu:
            total_sales = self.total_sales_for_menu_item(menu_item)
            profit = total_sales * (menu_item.get_selling_price() - menu_item.get_wholesale_cost())
            return profit
        else:
            raise InvalidSalesItemError

    def total_profit_for_stand(self):
        """returns the total profit on all items sold over the history of the stand"""

        total = 0
        for menu_item in self._menu:
            total += self.total_profit_for_menu_item()
        return total

def main():
    """function to test code if this file is ran as a script.
    Creates LemonadeStand object. Creates MenuItem object(s) and adds them to the
    LemonadeStand's menu. Creates a dictionary of sales for the day that includes at
    least one item not on the menu. It tries calling enter_sales_for_today() and
    passing that sales dictionary as the argument. It also tests the InvalidSalesItem
    exception class"""

    test_stand1 = LemonadeStand("Double R")
    item1 = MenuItem("Coffee", .4, 2)
    item2 = MenuItem("Cherry Pie", .8, 3)
    test_stand1.add_menu_item(item1)
    test_stand1.add_menu_item(item2)
    test_sales1 = {"Coffee":25, "Cherry Pie":20, "Cookie":2}
    try:
        test_stand1.enter_sales_for_today(test_sales1)
    except(InvalidSalesItemError):
        print("At least one menu item not in menu for stand")



if __name__ == '__main__':
    main()





