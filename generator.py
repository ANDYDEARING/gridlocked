from random import randint

def next_number(total_so_far, numbers_remaining, set_length):
    """
    Generates the next elemental effect number on a random mech. This assumes the
    average value across all stats is 3 out of 5
    """
    target_number = (3 * set_length) - total_so_far
    if target_number < 1:
        print("You messed up")
        return
    else:
        min_value = max(target_number-(5*(numbers_remaining-1)) ,1)
        max_value = min(target_number-(1*(numbers_remaining-1)) ,5)
        return randint(min_value,max_value)




