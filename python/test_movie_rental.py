import unittest

from movie_rental import Customer, Rental, Movie


class MovieRental(unittest.TestCase):

    def test_print_default_statement(self):
        customer = Customer("Bob")
        customer.add_rental(Rental(Movie("Jaws", Movie.REGULAR), 2))
        customer.add_rental(Rental(Movie("Golden Eye", Movie.REGULAR), 3))
        customer.add_rental(Rental(Movie("Short New", Movie.NEW_RELEASE), 1))
        customer.add_rental(Rental(Movie("Long New", Movie.NEW_RELEASE), 2))
        customer.add_rental(Rental(Movie("Bambi", Movie.CHILDREN), 3))
        customer.add_rental(Rental(Movie("Toy Story", Movie.CHILDREN), 4))

        expected = "Rental Record for Bob\n"
        expected += "\tJaws\t2.0\n"
        expected += "\tGolden Eye\t3.5\n"
        expected += "\tShort New\t3.0\n"
        expected += "\tLong New\t6.0\n"
        expected += "\tBambi\t1.5\n"
        expected += "\tToy Story\t3.0\n"
        expected += "Amount owed is 19.0\n"
        expected += "You earned 7 frequent renter points"

        assert expected == customer.statement()
