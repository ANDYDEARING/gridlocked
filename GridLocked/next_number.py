from random import randint

def next_number(total_so_far, numbers_remaining, set_length):
    target_number = (3 * set_length) - total_so_far
    if target_number < 1:
        print("You messed up")
        return
    else:
        min_value = max(target_number-(5*(numbers_remaining-1)) ,1)
        max_value = min(target_number-(1*(numbers_remaining-1)) ,5)
        return randint(min_value,max_value)
i = 0
while i<10:
    print(next_number(245,50,100))
    i = i+1



