from random import randint

#actual multiplier values for the 5 stat positions
STAT_MULTIPLIER_SET = (0.5, 0.75, 1, 1.5, 2)

#Heavy extra damage at the cost of speed, Light faster at the cost of damage,
#Ruinous applies a status effect, Piercing decreases element defense at the cost
#damage
SPECIAL_SET = (Heavy, Light, Ruinous, Piercing)
ELEMENT_SET = (Energy, Acid, Metal, Quantum)
WEAPON_SET = (Blaster, Cannon, Blade, Bomb)


def next_number(total_so_far, numbers_remaining, set_length):
    """
    Generates the next elemental effect number on a random fighter. This assumes the
    average value across all stats is 3 out of 5 and returns an integer between 1 and
    5 inclusive that won't make the mean of 3 impossible
    """
    # if the set number is less than halfway through the set, any value 1-5 is allowed
    if numbers_remaining > (set_length/2):
        return randint(1,5)
    # if not, set minimum and maximum to make sure the mean is 3 at the end
    target_number = (3 * set_length) - total_so_far
    min_value = max(target_number-(5*(numbers_remaining-1)) ,1)
    max_value = min(target_number-(1*(numbers_remaining-1)) ,5)
    return randint(min_value,max_value)

def total(iterable):
    """
    Calculates the total of all items in an interable. Returns 0 if empty
    """
    if len(iterable) == 0:
        return 0
    else:
        total = 0
        index = 0
        for item in iterable:
            total += iterable[index]
            index += 1
        return total

def make_random_fighter_stats(number_of_profiles, number_of_attributes=4):
    """
    Accepts an integer for the desired number of random fighter stats and
    returns a list that size of tuple profiles (of default length 4). The tuples 
    contain a value of 1 to 5 inclusive
    """
    fighter_array = []
    for profile in range(0,number_of_profiles):
        new_profile = []
        for attribute in range(0,number_of_attributes):
            new_profile.append(next_number(
                total(new_profile),
                number_of_attributes - len(new_profile),
                number_of_attributes
                ))
        fighter_array.append(tuple(new_profile))
    return fighter_array

def test_fighter_stat_generator():
    TESTS = 1000
    failed = 0
    frequency = {}
    fighter_array = make_random_fighter_stats(TESTS)
    print(f"FIRST: {fighter_array[0]}")
    for fighter in fighter_array:
        if total(fighter) != 12:
            failed += 1
        for value in fighter:
            value_str = str(value)
            if value_str in frequency:
                frequency[value_str] += 1
            else:
                frequency[value_str] = 1
    print("REPORT:")
    print(f"FAILURES: {failed}")
    print("FREQUENCY:")
    print(frequency)



# Need a function to make random weapons and equipment

# Need a function to clear the database of equipment
