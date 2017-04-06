# fake-credit-card generation/validator

"""<br>
Quick and dirty implementation using pure Python and mathematics.
Feel free to reuse or port it into other lang for whatever the reason.

This is ONLY for generating a fake credit card number that statisfies the Luhn
check algorithm which most of the card validation are based upon.
In other words, it's studying how the 'mod 10' employed in the Luhn works and then,
adding appropriate checksum digit at the end to  making the random generation of number
appear like a valid credit card number.<br>
"""

<h4>Example</h4>
<pre>

$ ./card_num_generator.py 
Card type: discover,  6011227847324111
Card type: mastercard,  5563218655744379
Card type: americanexpress,  361649892117471
Card type: visa13,  4291416812973
Card type: visa16,  43545942222655110

</pre>

