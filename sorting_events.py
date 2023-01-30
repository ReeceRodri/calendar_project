
# Transform the events time to an appropriate form for sorting and vise versa 
def transform_time(rows, pre_sorting_factor):
    if pre_sorting_factor :
        for row in rows:
            row[1] = [int(i) for i in row[1].split(':')]
        return rows
    else:
        for row in rows:
            row[1] = ':'.join([str(i) for i in row[1]])
        return rows


# Swap two values 
def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2],list[pos1]
    return list 


# Creating a bubble sorting algorithm
def buble_sort(list):
    
    swapped = True
    while swapped:
        swapped = False 
        
        for i in range(len(list)-1):
            
            if list[i][1][0] > list[i+1][1][0]:
                list = swap(list, i, i+1)
                swapped = True
            elif list[i][1][0] == list[i+1][1][0]:
                if list[i][1][1] > list[i+1][1][1]:
                    list =swap(list, i, i+1)
                    swapped = True
    return list


# Main function for sorting events by time
def sort_by_time(transforming_list):

    transforming_trans = transform_time(transforming_list, True)

    buble_sort_1 = buble_sort(transforming_trans)
    result = transform_time(buble_sort_1, False)
    return result