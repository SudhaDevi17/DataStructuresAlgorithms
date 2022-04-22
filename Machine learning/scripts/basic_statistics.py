
from collections import Counter
input_list = [2, 1, 3, 4, 4, 5, 6, 7]

def mode(input_list):
    sorted_list = sorted(input_list)

    dict = Counter(sorted_list)
    mode = sorted(dict.items(), key = lambda value : value[1], reverse= True )[0][0]
    return mode

def getMode(input_list):
    from collections import Counter

    sorted_input= sorted(input_list)
    dict = Counter(sorted_input)
    print(sorted(dict.items(), key = lambda val : val[1], reverse= True ))
    mode = sorted(dict.items(), key = lambda val : val[1], reverse= True )[0][0]
    return mode

def getMedian(input_list):
    n = len(input_list)
    sorted_list  = sorted(input_list)
    middle_index = n//2

    if n%2==0:
        left_middle_index = middle_index-1
        right_middle_index = middle_index
        middle = (sorted_list[left_middle_index] + sorted_list[right_middle_index])/2
    else:
        middle  = sorted_list[middle_index]
    # print('even {}'.format( 44//2))
    # print('odd {}' .format(23//2))
    return middle

#TEST MODE
print(mode(input_list))
print(getMode(input_list))

#TEST MEDIAN
# print(getMedian([3,5,7,8]))
# print(getMedian([2,4,6]))