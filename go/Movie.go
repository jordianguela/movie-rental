package movie_rental

type Movie struct {
	_title     string
	_priceCode uint
}

func (m Movie) getPriceCode() uint {
	return m._priceCode
}

func (m Movie) getTitle() string {
	return m._title
}

const REGULAR = 0
const NEW_RELEASE = 1
const CHILDRENS = 2
