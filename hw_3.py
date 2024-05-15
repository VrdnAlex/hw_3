from random import randint

def generate_unique_numbers(min, max, quantity):
    if not (1 <= min <= max <= 1000) and (quantity <= max - min + 1):
        return []
    result_array = set()
    
    while len(result_array) != quantity:
            result_array.add(randint(min, max))
    return sorted(list(result_array))
        
min = 1
max = 49
quantity = 6

lottery_numbers = generate_unique_numbers(min, max, quantity)
print("Your lottery numbers:", lottery_numbers)
