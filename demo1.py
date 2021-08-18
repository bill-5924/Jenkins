lst =  [1, 3, 5, 7, 3, 4, 5, 6]

def get_max_element(input_lst):
    '''
    get input list max element
    '''
    max_value = input_lst[0]
    for item in input_lst:
        if item > max_value:
            max_value = item
    return max_value

def get_lst_avg(input_lst):
    '''
    get the list average
    '''
    total_num = 0
    for item in input_lst:
        total_num += item
    avg = total_num/len(input_lst)
    lst_avg = round(avg, 2)
    return lst_avg

def del_repeat_element(input_lst):
    '''
    delete the input_lst repeat element
    '''
    new_lst = []
    for item in input_lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

def sort_lst(input_lst, min_to_max=True):
    '''
    sort the input_lst
    '''
    sorted_lst = []
    for index, item in enumerate(input_lst):
        for index2 in range(1, len(input_lst)-index):
            if input_lst[index2] < input_lst[index2-1]:
                tmp = input_lst[index2]  # a, b = b, a
                input_lst[index2] = input_lst[index2-1]
                input_lst[index2-1] = tmp
        sorted_lst = input_lst
    if min_to_max:
        return sorted_lst
    sorted_lst.reverse()
    return sorted_lst

print('list max element is: ', get_max_element(lst))
print('list average is: ', get_lst_avg(lst))
no_repeat_lst = del_repeat_element(lst)
print('no repeat list: ', no_repeat_lst)
print('sorted list(min to max): ' ,sort_lst(no_repeat_lst))
print('sorted list(max to min): ' ,sort_lst(no_repeat_lst, False))