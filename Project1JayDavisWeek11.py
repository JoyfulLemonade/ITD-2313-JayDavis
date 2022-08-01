def sequentialSearch(target, lyst):
    position = 0
    while position < len(lyst):
        if target < lyst[position]:
            return -1
        elif target == lyst[position]:
                return position
        position += 1
        return -1
