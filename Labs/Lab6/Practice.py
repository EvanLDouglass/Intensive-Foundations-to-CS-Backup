# Question 1

#### Signature
# count_occurrences :: (Integer[], Integer) => Integer
#### Tests
# count_occurrences([3,4,3,2,11,11,13], 3) => 2
# count_occurrences([4], 2) => 0
# count_occurrences([3,4,5,6,7], 7) => 1
#
def count_occurrences(int_list, num):
    count = 0
    for n in int_list:
        if n == num:
            count += 1
    return count


def snippet():
    prompt = "Enter an integer (-99 to quit): "
    number = int(input(prompt))
    tracking_list = []

    while number != -99:
        tracking_list.append(number)
        number = int(input(prompt))

    length = len(tracking_list)
    adjusted_len = length
    total = 0
    for num in tracking_list:
        if -50 < num < 100:
            total += num
        else:
            adjusted_len -= 1
    
    avg = total / adjusted_len

    print("You entered", length, "numbers. Discounting outliers, the average was", avg)


#### Signature
# weighted_avg :: (Integer[], Float[]) => Float
#### Tests
# weighted_avg([4, 4, 4], [.25, .25, .5]) => 4.0
# weighted_avg([3, 4, 2, 5, 1], [.1 , .3, .15, .4, .05]) => 3.85
#
def weighted_avg(scores, weights):
    avg = 0
    for i in range(len(scores)):
        weighted_score = scores[i] * weights[i]
        avg += weighted_score
    return avg


# ========== Tests ========== #
def test_count_occurrences():
    l1 = [3,4,3,2,11,11,13,5,2,6,7,4,5,9,0,10]
    l2 = []
    assert(count_occurrences(l1, 3) == 2)
    assert(count_occurrences(l1, 6) == 1)
    assert(count_occurrences(l1, 33) == 0)
    assert(count_occurrences(l2, 5) == 0)

def test_weighted_avg():
    assert(weighted_avg([4, 4, 4], [.25, .25, .5]) == 4.0)
    assert(round(weighted_avg([3, 4, 2, 5, 1], [.1 , .3, .15, .4, .05]), 2) == 3.85)
    assert(weighted_avg([], []) == 0.0)
