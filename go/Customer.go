package movie_rental

import "fmt"

type Customer struct {
	_name    string
	_rentals []Rental
}

func (c *Customer) addRental(rental Rental) {
	c._rentals = append(c._rentals, rental)
}

func (c Customer) statement() string {
	totalAmount := 0.0
	frequentRenterPoints := 0
	result := "Rental Record for " + c.getName() + "\n"

	for _, each := range c._rentals {
		thisAmount := 0.0

		//determine amounts for each line
		switch each.getMovie().getPriceCode() {
		case REGULAR:
			thisAmount += 2
			if each.getDaysRented() > 2 {
				thisAmount += (each.getDaysRented() - 2) * 1.5
			}
			break
		case NEW_RELEASE:
			thisAmount += each.getDaysRented() * 3
			break
		case CHILDRENS:
			thisAmount += 1.5
			if each.getDaysRented() > 3 {
				thisAmount += (each.getDaysRented() - 3) * 1.5
			}
			break
		}

		// add frequent renter points
		frequentRenterPoints++
		// add bonus for a two day new release rental
		if (each.getMovie().getPriceCode() == NEW_RELEASE) && each.getDaysRented() > 1 {
			frequentRenterPoints++
		}

		// show figures for this rental
		result += fmt.Sprintf("\t"+each.getMovie().getTitle()+"\t%.1f\n", thisAmount)
		totalAmount += thisAmount
	}

	// add footer lines
	result += fmt.Sprintf("Amount owed is %.1f\n", totalAmount)
	result += fmt.Sprintf("You earned %d frequent renter points", frequentRenterPoints)

	return result

}

func (c Customer) getName() string {
	return c._name
}
