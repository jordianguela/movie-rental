from domain.MovieType import MovieType


class Movie:
    def __init__(self, title: str, movie_type: MovieType):
        self.title = title
        self.movie_type = movie_type

    def calculate_rental_price(self, days_rented: int) -> float:
        return self.movie_type.calculate_rental_price(days_rented)

    def calculate_frequent_renter_points(self, days_rented):
        return self.movie_type.calculate_frequent_renter_points(days_rented)
