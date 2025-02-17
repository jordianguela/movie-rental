from domain.MovieType import MovieType


class RegularMovieType(MovieType):
    def calculate_rental_price(self, days_rented: int) -> float:
        rental_price = 2.0
        if days_rented > 2:
            rental_price += (days_rented - 2) * 1.5
        return rental_price

    def calculate_frequent_renter_points(self, days_rented: int) -> int:
        return 1
