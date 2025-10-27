character_list = "0123456789abcdefghijklmnopqrstuvwxyz"

def value(character):
    return character_list.index (character)

def base_to_decimal(number, base):
    chars = list(number)
    dec_val = value(chars[-1])
    for char in range(len(chars)-2, -1, -1):
        dec_val = dec_val + value(chars[char]) * base**(len(chars) - (char +1))
    return dec_val

def decimal_to_base(number, base):
    mutable_num = number
    base_val = ""
    while mutable_num != 0:
        val = mutable_num / base - int(mutable_num / base)
        val = character_list[int(val * base)] 
        base_val = str(val) + base_val
        mutable_num = int(mutable_num / base) 
    return base_val

number = input("Enter a number")
starting_base = input("What is the original base of this number?")
ending_base = input("What base do you want to convert to?")

decimal_number = base_to_decimal(number, int(starting_base))
final_number = decimal_to_base(decimal_number, int(ending_base))

print(final_number)