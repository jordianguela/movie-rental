<?php
namespace Kata;

class Movie
{
    const REGULAR = 0;
    const NEW_RELEASE = 1;
    const CHILDRENS = 2;
    private mixed $_priceCode;
    private mixed $_title;

    public function __construct($title, $priceCode)
    {
        $this->_title = $title;
        $this->_priceCode = $priceCode;
    }

    public function getPriceCode()
    {
        return $this->_priceCode;
    }

    public function setPriceCode(int $arg)
    {
        $this->_priceCode = $arg;
    }

    public function getTitle()
    {
        return $this->_title;
    }

}