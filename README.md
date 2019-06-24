# fake-credit-card generation/validator

Quick and dirty implementation using Python. Feel free to reuse or port it into other lang for whatever the reason. I won't be responsible for how 

## Background
This is only generating a fake credit card number that statisfies the Luhn check algorithm which most of the card validation are based upon. So by knowing how the 'mod 10' is applied to validate the card number, we can then add appropriate checksum digit at the end of the number to making the random generation of number appear like a valid credit card number - reverse engineering.

Obviously, we also need to know some basics of card numbering system.
Example: a **Visa** card always starts with 4, **American Express** starts with 3 and **American Express** with 5. **Discover** on the other hand starts with 6011. But even if this initial numbering system are changed, it's not a big deal. The checksum will continue to work as long as we are going to use the Luhn algorithm for card validation.
<br>Wiki: https://en.wikipedia.org/wiki/Luhn_algorithm
<br>
"""

## Example
<pre>

$ ./card_num_generator.py 
Card type: discover,  6011227847324111
Card type: mastercard,  5563218655744379
Card type: americanexpress,  361649892117471
Card type: visa13,  4291416812973
Card type: visa16,  43545942222655110

</pre>

