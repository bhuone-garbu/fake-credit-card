# fake-credit-card generation/validator

"""<br>
Quick and dirty implementation using pure Python and mathematics.
Feel free to reuse or port it into other lang for whatever the reason.

This is ONLY for generating a fake credit card number that statisfies the Luhn
check algorithm which most of the card validation are based upon.
In other words, it's studying how the 'mod 10' employed in the Luhn works and then,
adding appropriate checksum digit at the end to  making the random generation of number
appear like a valid credit card number.

If only life was so easy as generating numbers like these. :)<br>
"""

<h4>Example</h4>
<pre>
./card_num_generator.py 
Card type: discover,  6011178514751914
Card type: mastercard,  5333466425476884
Card type: americanexpress,  363393755294212
Enter 13 or 16 for the digits required (visa): 13
Card type: visa,  4224473725572
Enter 13 or 16 for the digits required (visa): 16
Card type: visa,  4619287581787635

</pre>

