for outer_number in range(2,101):
    prime = True
    for inner_number in range(2, outer_number):
        if outer_number % inner_number == 0:
            prime = False
            break
    if prime:
        print(outer_number)