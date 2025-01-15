# Movie rental kata
Completed on the 15th of January 2025.

Done by [Jordi Anguela](https://www.linkedin.com/in/jordianguela/) from [Codium](https://www.codium.team/).

Starting point [Github repository](https://github.com/SoftwareCraftersMurcia/movie-rental).

# Problem
Add a new formatter to print a history of customer rentals.

[Extended version](https://github.com/SoftwareCraftersMurcia/movie-rental/blob/main/README.md)

# Solution
1. Remove void getter methods without business logic.
2. Split the business logic that calculates the Statement data and the logic that only prints the data.
3. Define a Print interface with DefaultStatementPrinter implementation and inject it
4. Implement the HtmlStatementPrinter (goal of the kata) 
5. Use composition to extract price and frequent_renter_points calculations
6. Create a first-class collection Rentals
