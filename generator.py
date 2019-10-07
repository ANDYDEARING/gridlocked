from random import randint

def next_number(total_so_far, numbers_remaining, set_length):
    """
    Generates the next elemental effect number on a random mech. This assumes the
    average value across all stats is 3 out of 5 and returns an integer between 1 and
    5 inclusive that won't make the mean of 3 impossible
    """
    if numbers_remaining > (set_length/2):
        return randint(1,5)
    target_number = (3 * set_length) - total_so_far
    if target_number < 1:
        print("You messed up")
        return
    else:
        min_value = max(target_number-(5*(numbers_remaining-1)) ,1)
        max_value = min(target_number-(1*(numbers_remaining-1)) ,5)
        return randint(min_value,max_value)

def make_random_mech_stats(number_of_mechs, number_of_attributes=4):
    """
    Accepts an integer for the desired number of random mech stats and
    returns a list that size of tuples (of default length 4). The tuples contain
    a value of 1 to 5 inclusive
    """
    mech_array = []

    return mech_array[]


