# set N here
number_times = 10
series_sum = 0.0
if_add = True

# loop over numbers from 1 to N
for num in range(1,number_times * 2,2):

    if if_add:
        series_sum += (1/num)
    else:
        series_sum -= (1/num)

    if_add = not if_add

    pi = 4 * series_sum

    print("After {0:3} iterations pi approximates to {1:7.6}".format(int((num+1)/2),pi))