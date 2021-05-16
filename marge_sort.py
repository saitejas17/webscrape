def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        left_list = dataset[:mid]
        right_list = dataset[mid:]

        mergesort(left_list)
        mergesort(right_list)
        i = 0
        j = 0
        k = 0

        # while both arrays have content
        while i < len(left_list) and j < len(right_list):
            if left_list[i][1] < right_list[j][1]:
                dataset[k] = left_list[i]
                i += 1
            else:
                dataset[k] = right_list[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(left_list):
            dataset[k] = left_list[i]
            i += 1
            k += 1

        # if the right array still has values, add them
        while j < len(right_list):
            dataset[k] = right_list[j]
            j += 1
            k += 1
    return dataset
