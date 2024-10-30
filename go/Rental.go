package movie_rental

type Rental struct {
	_movie      Movie
	_daysRented float64
}

func (r Rental) getMovie() Movie {
	return r._movie
}

func (r Rental) getDaysRented() float64 {
	return r._daysRented
}
