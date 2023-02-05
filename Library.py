# Author: Isaac Johnson
# GitHub username: Johnsonisaacn
# Date: 01/24/2023
# Description: This library simulator uses classes to organize the patrons
# and items belonging to a library

class LibraryItem:
    """Object that represents an item that a patron may check out from
    a library. This parent class has 3 child classes: Book, Album, and
    Movie"""

    def __init__(self, library_item_id, title):
        """initializes data members"""

        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        int(self._date_checked_out)

    def get_location(self):
        """returns the location of a library item"""

        return self._location

    def set_location(self, location):
        """sets the location of a library item"""

        self._location = location

    def get_requested_by(self):
        """returns the name of the patron requesting the item"""

        return self._requested_by

    def get_checked_out_by(self):
        """returns the name of the patrom who has the item checked out"""

        return self._checked_out_by

    def set_requested_by(self, patron):
        """returns the name of the patron requesting the item"""

        self._requested_by = patron

    def set_checked_out_by(self, patron):
        """returns the name of the patrom who has the item checked out"""

        self._checked_out_by = patron

    def get_title(self):
        """returns the title of the item"""

        return self._title

    def get_library_item_id(self):
        """returns the item ID of the item"""

        return self._library_item_id

    def set_date_checked_out(self, date):
        """sets date for when a library item is checked out"""

        self._date_checked_out = date

    def get_date_checked_out(self):
        """sets date for when a library item is checked out"""

        return self._date_checked_out

class Book(LibraryItem):
    """creates a book object, which is a child class of the LibraryItem class"""

    def __init__(self, library_item_id, title, author):
        """initializes the data members using the LibraryItem method and an
        assignment for author"""

        self._author = author
        super().__init__(library_item_id, title)
    def get_author(self):
        """returns the author of the book"""

        return self._author

    def get_check_out_length(self):
        """returns the length in days for which a book may be checked out"""

        return 21

class Album(LibraryItem):
    """creates an album object that inherits from its parent class LibraryItem"""

    def __init__(self, library_item_id, title, artist):
        """initializes the data members using the LibraryItem method and an
        assignment for author"""

        self._artist = artist
        super().__init__(library_item_id, title)


    def get_artist(self):
        """returns the author of the book"""

        return self._artist

    def get_check_out_length(self):
        """returns the length in days for which a book may be checked out"""

        return 14

class Movie(LibraryItem):
    """creates a movie object that inherits from parent class LibraryItem"""

    def __init__(self, library_item_id, title, director):
        """initializes the data members using the LibraryItem method and an
        assignment for author"""

        self._director = director
        super().__init__(library_item_id, title)


    def get_director(self):
        """returns the author of the book"""

        return self._director

    def get_check_out_length(self):
        """returns the length in days for which a book may be checked out"""

        return 7

class Patron:
    """creates a patron object that can check out LibraryItem objects"""

    def __init__(self, patron_id, name):
        """initializes data members for Patron object"""

        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        float(self._fine_amount)

    def get_fine_amount(self):
        """returns the amount that the patron owes the library in fines"""

        return self._fine_amount

    def get_name(self):
        """returns the patron name"""

        return self._name

    def get_checked_out_items(self):
        """returns list of LibraryItem objects that the patron object has
        checked out currently"""

        return self._checked_out_items

    def get_patron_id(self):
        """returns the patron ID"""

        return self._patron_id

    def add_library_item(self, library_item):
        """adds a LibraryItem object to the list of checked out items
        for the patron"""

        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """removes the specified LibraryItem object from the list of
        items checked out by the patron"""

        self._checked_out_items.remove(library_item)

    def amend_fine(self, amount):
        """changes the fine amount that the patron owes the library"""

        self._fine_amount -= amount

class Library:
    """creates a Library object that contains LibraryItem objects and is
    used by patrons"""

    def __init__(self):
        self._holdings = []
        self._members = []
        int(self._current_date)

    def get_current_date(self):
        """returns the current date"""

        return self._current_date

    def add_library_item(self, library_item):
        """adds LibraryItem objects to the list of holdings"""

        self._holdings.append(library_item)

    def add_patron(self, patron):
        """adds a patron object to the list of members"""

        self._members.append(patron)

    def lookup_library_item_from_id(self, library_item_id):
        """returns a library item given the library item ID
        if that library item object is in the holdings list"""
        counter = 0
        #running out of time to submit and needed a quick way to return
        #None in case of not finding item while looping
        for item in self._holdings:
            if item.get_library_item_id() == library_item_id:
                counter += 1
                return item
        if counter == 0:
            return None

    def lookup_patron_from_id(self, patron_id):
        """returns a patron object given the patron ID
        if that patron is in the members list"""
        counter = 0
        #running out of time to submit and needed a quick way to return
        #None in case of not finding item while looping
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                counter += 1
                return patron
        if counter == 0:
            return None

    def check_out_library_item(self, patron_id, library_item_id):
        """Checks out a library item object to a patron object"""
        patron = self.lookup_patron_from_id(patron_id)
        library_item = self.lookup_library_item_from_id(library_item_id)

        if patron in self._members:
            if library_item in self._holdings:
                if library_item.get_checked_out_by() == None:
                    if library_item.get_requested_by() == None or patron:
                        library_item.set_checked_out_by(patron)
                        library_item.set_date_checked_out(self._current_date)
                        library_item.set_location("CHECKED_OUT")
                        patron.add_library_item(library_item)
                        if library_item.get_requested_by() == patron:
                            library_item.set_requested_by(None)
                        return "check out successful"
                    else:
                        return "item on hold by other patron"
                else:
                    return "item already checked out"

            else:
                return "item not found"
        else:
            return "patron not found"

    def return_library_item(self, library_item_id):
        """returns a library item object from the patron"""

        library_item = self.lookup_library_item_from_id(library_item_id)
        if library_item in self._holdings:
            if library_item.get_location() == "CHECKED_OUT":
                library_item.get_checked_out_by().remove_library_item(library_item)
                if library_item.get_requested_by() != None:
                    library_item.set_location("ON_HOLD_SHELF")
                library_item.set_checked_out_by(None)
                return "return successful"
            else:
                return "item already in library"
        else:
            return "item not found"

    def request_library_item(self, patron_id, library_item_id):
        """places a library item object on hold"""

        patron = self.lookup_patron_from_id(patron_id)
        library_item = self.lookup_library_item_from_id(library_item_id)
        if patron in self._members:
            if library_item in self._holdings:
                if library_item.get_requested_by() == None:
                    library_item.set_requested_by(patron)
                    if library_item.get_location() == "ON_SHELF":
                        library_item.set_location("ON_HOLD_SHELF")
                    return "request successful"
                else:
                    return "item already on hold"
            else:
                return "item not found"
        else:
            return "patron not found"

    def pay_fine(self, patron_id, fine_amount):
        """pays a fine for having library items checked out past
        their due date"""

        patron = self.lookup_patron_from_id(patron_id)
        if patron in self._members:
            patron.amend_fine(fine_amount)
        else:
            return "patron not found"

    def increment_current_date(self):
        """increments the current date for the library object"""

        self._current_date += 1
        for patron in self._members:
            for item in patron.get_checked_out_items():
                if item.get_date_checked_out() > item.get_check_out_length():
                    patron.amend_fine(-0.1)


b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")
print(b1.get_author())
print(a1.get_artist())
print(m1.get_director())

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")

libr = Library()
libr.add_library_item(b1)
libr.add_library_item(a1)
libr.add_patron(p1)
libr.add_patron(p2)

libr.check_out_library_item("bcd", "456")
for _ in range(7):
    libr.increment_current_date()  # 7 days pass
libr.check_out_library_item("abc", "567")
loc = a1.get_location()
libr.request_library_item("abc", "456")
for _ in range(57):
    libr.increment_current_date()  # 57 days pass
p2_fine = p2.get_fine_amount()
libr.pay_fine("bcd", p2_fine)

print(p1.get_fine_amount())
print(libr.get_current_date())
print(a1.get_date_checked_out())
print(a1.get_check_out_length())
print(a1.get_checked_out_by().get_name())