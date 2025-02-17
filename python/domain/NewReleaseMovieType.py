from domain.MovieType import MovieType


class NewReleaseMovieType(MovieType):
    def calculate_rental_price(self, days_rented: int) -> float:
        return days_rented * 3.0

    def calculate_frequent_renter_points(self, days_rented: int) -> int:
        return 2 if days_rented > 1 else 1
