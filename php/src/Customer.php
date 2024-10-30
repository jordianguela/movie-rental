<?php
namespace Kata;

class Customer
{
    private array $_rentals;
    private mixed $_name;

    public function __construct($string)
    {
        $this->_name = $string;
    }

    public function addRental($param)
    {
        $this->_rentals[] = $param;
    }

    public function statement()
    {
        $totalAmount = 0;
        $frequentRenterPoints = 0;
        $result = "Rental Record for " . $this->getName() . "\n";

        foreach ($this->_rentals as $each) {
            $thisAmount = 0;

            //determine amounts for each line
            switch ($each->getMovie()->getPriceCode()) {
                case Movie::REGULAR:
                    $thisAmount += 2;
                    if ($each->getDaysRented() > 2)
                        $thisAmount += ($each->getDaysRented() - 2) * 1.5;
                    break;
                case Movie::NEW_RELEASE:
                    $thisAmount += $each->getDaysRented() * 3;
                    break;
                case Movie::CHILDRENS:
                    $thisAmount += 1.5;
                    if ($each->getDaysRented() > 3)
                        $thisAmount += ($each->getDaysRented() - 3) * 1.5;
                    break;
            }

            // add frequent renter points
            $frequentRenterPoints++;
            // add bonus for a two day new release rental
            if (($each->getMovie()->getPriceCode() == Movie::NEW_RELEASE) && $each->getDaysRented() > 1)
                $frequentRenterPoints++;

            // show figures for this rental
            $result .= sprintf("\t%s\t%1.1f\n", $each->getMovie()->getTitle(), $thisAmount);
            $totalAmount += $thisAmount;
        }

        // add footer lines
        $result .= sprintf("Amount owed is %1.1f\n", $totalAmount);
        $result .= "You earned " . $frequentRenterPoints . " frequent renter points";

        return $result;

    }

    private function getName()
    {
        return $this->_name;
    }
}