owl_numbers = []

for num in range(0,10000):
    digits = str(num)
    sum_of_digits = sum([int(digit) for digit in digits])
    this_total = num + sum_of_digits
    if this_total not in owl_numbers:
        owl_numbers.append(this_total)

# for each integer, see if it's in list of owl numbers 
for number_digits in range(1, 10000, 100):

    # get string representation when not in owl numbers
    this_number_set = [str(n) for n in range(number_digits, number_digits + 99) if n not in owl_numbers]

    # join with comma
    number_block = ", ".join(this_number_set)

    # print block
    print(number_block)