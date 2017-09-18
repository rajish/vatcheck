# vatcheck

Checks a VAT number validity with the
[VIES](http://ec.europa.eu/taxation_customs/vies/) service

## Requirements

To run this script the [zeep](http://docs.python-zeep.org/en/master/)
module has to be installed:

    pip install zeep

## Running

Provide a proper VAT number as a parameter of the script.

    python vatcheck.py PL12345678

A proper VAT number consists of two-letter country code followed by
the country-specific VAT number matching the following reqular expression:

    [0-9A-Za-z\+\*\.]{2,12}