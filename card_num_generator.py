#!/usr/bin/env python

# author: garbu

from random import randint

def generate_card(type):
    """
    Prefill some values based on the card type
    """
    card_types = ["americanexpress","visa13", "visa16","mastercard","discover"]
    
    def prefill(t):
        # typical number of digits in credit card
        def_length = 16
        
        """
        Prefill with initial numbers and return it including the total number of digits
        remaining to fill
        """
        if t == card_types[0]:
            # american express starts with 3 and is 15 digits long
            # override the def lengths
            return [3, randint(4,7)], 13
            
        elif t == card_types[1] or t == card_types[2]:
            # visa starts with 4
            if t.endswith("16"):
                return [4], def_length - 1
            else:
                return [4], 12
            
        elif t == card_types[3]:
            # master card start with 5 and is 16 digits long
            return [5, randint(1,5)], def_length - 2
            
        elif t == card_types[4]:
            # discover card starts with 6011 and is 16 digits long
            return [6, 0, 1, 1], def_length - 4
            
        else:
            # this section probably not even needed here
            return [], def_length
    
    def finalize(nums):
        """
        Make the current generated list pass the Luhn check by checking and adding
        the last digit appropriately bia calculating the check sum
        """
        check_sum = 0
        
        #is_even = True if (len(nums) + 1 % 2) == 0 else False
        
        """
        Reason for this check offset is to figure out whther the final list is going
        to be even or odd which will affect calculating the check_sum.
        This is mainly also to avoid reversing the list back and forth which is specified
        on the Luhn algorithm.
        """
        check_offset = (len(nums) + 1) % 2
        
        for i, n in enumerate(nums):
            if (i + check_offset) % 2 == 0:
                n_ = n*2
                check_sum += n_ -9 if n_ > 9 else n_
            else:
                check_sum += n
        return nums + [10 - (check_sum % 10) ]
    
    # main body
    t = type.lower()
    if t not in card_types:
        print "Unknown type: '%s'" % type
        print "Please pick one of these supported types: %s" % card_types
        return
    
    initial, rem = prefill(t)
    so_far = initial + [randint(1,9) for x in xrange(rem - 1)]
    print "Card type: %s, " % t,
    print "".join(map(str,finalize(so_far)))



# run - check
generate_card("discover")
generate_card("mastercard")
generate_card("americanexpress")

generate_card("visa13")
generate_card("visa16")


