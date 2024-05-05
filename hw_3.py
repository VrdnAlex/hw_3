from random import randint, sample

def generate_unique_numbers(min, max, quantity):
    if (1 <= min <= max <= 1000) and (quantity <= max - min + 1):
        result_array = set()
        while len(result_array) != quantity:
            result_array.add(randint(min, max))
        return sorted(list(result_array))
    else:
        return []

lottery_numbers = generate_unique_numbers(min, max, quantity)
print("Your lottery numbers:", lottery_numbers)