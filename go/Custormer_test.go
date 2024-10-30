package movie_rental

import (
	"fmt"
	"testing"
)

func TestCustomer(t *testing.T) {
	customer := Customer{"Bob", []Rental{}}
	customer.addRental(Rental{Movie{"Jaws", REGULAR}, 2})
	customer.addRental(Rental{Movie{"Golden Eye", REGULAR}, 3})
	customer.addRental(Rental{Movie{"Short New", NEW_RELEASE}, 1})
	customer.addRental(Rental{Movie{"Long New", NEW_RELEASE}, 2})
	customer.addRental(Rental{Movie{"Bambi", CHILDRENS}, 3})
	customer.addRental(Rental{Movie{"Toy Story", CHILDRENS}, 4})
	expected := "" +
		"Rental Record for Bob\n" +
		"\tJaws\t2.0\n" +
		"\tGolden Eye\t3.5\n" +
		"\tShort New\t3.0\n" +
		"\tLong New\t6.0\n" +
		"\tBambi\t1.5\n" +
		"\tToy Story\t3.0\n" +
		"Amount owed is 19.0\n" +
		"You earned 7 frequent renter points"
	if expected != customer.statement() {
		t.Fatal(fmt.Sprintf("Expected:\n%s\nActual:\n%s\n", expected, customer.statement()))
	}
}
