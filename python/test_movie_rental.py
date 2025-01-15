import unittest

from movie_rental import Customer, Rental, Movie, DefaultStatementPrinter, HtmlStatementPrinter, RegularMovie, ChildrenMovie, NewReleaseMovie


class MovieRental(unittest.TestCase):

    def test_default_statement_printter(self):
        customer = Customer("Bob")
        customer.add_rental(Rental(Movie("Jaws", RegularMovie()), 2))
        customer.add_rental(Rental(Movie("Golden Eye", RegularMovie()), 3))
        customer.add_rental(Rental(Movie("Short New", NewReleaseMovie()), 1))
        customer.add_rental(Rental(Movie("Long New", NewReleaseMovie()), 2))
        customer.add_rental(Rental(Movie("Bambi", ChildrenMovie()), 3))
        customer.add_rental(Rental(Movie("Toy Story", ChildrenMovie()), 4))

        expected = "Rental Record for Bob\n"
        expected += "\tJaws\t2.0\n"
        expected += "\tGolden Eye\t3.5\n"
        expected += "\tShort New\t3.0\n"
        expected += "\tLong New\t6.0\n"
        expected += "\tBambi\t1.5\n"
        expected += "\tToy Story\t3.0\n"
        expected += "Amount owed is 19.0\n"
        expected += "You earned 7 frequent renter points"

        default_statement_printer = DefaultStatementPrinter()
        self.assertEqual(expected, customer.print_statement(default_statement_printer))

    def test_html_statement_printter(self):
        customer = Customer("martin")
        customer.add_rental(Rental(Movie("Ran", RegularMovie()), 3))
        customer.add_rental(Rental(Movie("Trois Couleurs: Bleu", RegularMovie()), 2))

        expected = "<h1>Rental Record for <em>martin</em></h1>\n"
        expected += "<table>\n"
        expected += "\t<tr><td>Ran</td><td>3.5</td></tr>\n"
        expected += "\t<tr><td>Trois Couleurs: Bleu</td><td>2.0</td></tr>\n"
        expected += "</table>\n"
        expected += "<p>Amount owed is <em>5.5</em></p>\n"
        expected += "<p>You earned <em>2</em> frequent renter points</p>"

        default_statement_printer = HtmlStatementPrinter()
        self.assertEqual(expected, customer.print_statement(default_statement_printer))
